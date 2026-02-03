document.addEventListener("DOMContentLoaded", () => {
    console.log("map.js loaded and running");

    const statusEl = document.getElementById("map-status");

    // Make sure Leaflet is available
    if (typeof L === "undefined") {
        console.error("Leaflet (L) is not defined. Check your leaflet.js script tag.");
        if (statusEl) {
            statusEl.textContent = "Map failed to load: Leaflet missing.";
        }
        return;
    }

    // Initialize the map (centered roughly on the US)
    const map = L.map("map").setView([39.5, -98.35], 4);

    // Add OpenStreetMap tiles
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        attribution: "&copy; OpenStreetMap contributors",
    }).addTo(map);

    const trafficLayer = L.layerGroup().addTo(map);
    const accidentLayer = L.layerGroup().addTo(map);

    function setStatus(message) {
        if (!statusEl) return;
        if (message) {
            statusEl.textContent = message;
            statusEl.style.display = "block";
        } else {
            statusEl.style.display = "none";
        }
    }

    function normalizeLevel(level) {
        return String(level || "").trim().toLowerCase();
    }

    function trafficColor(level) {
        const normalized = normalizeLevel(level);
        if (["none", "no", "clear", "low"].includes(normalized)) return "green";
        if (["light", "medium", "moderate"].includes(normalized)) return "#f5c542";
        return "red";
    }

    function trafficLabel(level) {
        const normalized = normalizeLevel(level);
        if (["none", "no", "clear", "low"].includes(normalized)) return "No Traffic";
        if (["light", "medium", "moderate"].includes(normalized)) return "Light Traffic";
        if (normalized) return "Heavy Traffic";
        return "Unknown";
    }

    function accidentIcon() {
        return L.divIcon({
            className: "accident-marker",
            html: "!",
            iconSize: [18, 18],
            iconAnchor: [9, 9],
            popupAnchor: [0, -8],
        });
    }

    function addPoint(point) {
        const lat = Number(point.latitude);
        const lon = Number(point.longitude);
        if (!Number.isFinite(lat) || !Number.isFinite(lon)) return;

        const city = point.city || "Unknown";
        const state = point.state && point.state !== "Unknown" ? point.state : "";
        const locationLabel = state ? `${city}, ${state}` : city;

        const level = point.traffic_level || point.trafficLevel || "";
        const color = trafficColor(level);
        const accidents = Math.max(0, Number(point.accidents) || 0);
        const avgSpeed = point.avg_speed ? `${point.avg_speed} mph` : "N/A";
        const accidentType = point.accident_type ? point.accident_type : "N/A";

        const marker = L.circleMarker([lat, lon], {
            radius: 9,
            color,
            fillColor: color,
            fillOpacity: 0.85,
            weight: 2,
        }).addTo(trafficLayer);

        marker.bindPopup(`
            <b>${locationLabel}</b><br>
            Traffic: ${trafficLabel(level)}<br>
            Accidents: ${accidents}<br>
            Avg Speed: ${avgSpeed}<br>
            Accident Type: ${accidentType}
        `);

        if (accidents > 0) {
            const accidentMarker = L.marker([lat, lon], { icon: accidentIcon() }).addTo(accidentLayer);
            accidentMarker.bindPopup(`
                <b>${locationLabel}</b><br>
                Accident Reported: ${accidents}<br>
                Traffic: ${trafficLabel(level)}
            `);
        }

        return L.latLng(lat, lon);
    }

    async function loadMapData() {
        setStatus("Loading map data...");
        try {
            const response = await fetch("/api/map_data");
            if (!response.ok) throw new Error("Map data request failed");
            const payload = await response.json();
            const points = Array.isArray(payload.data) ? payload.data : [];

            trafficLayer.clearLayers();
            accidentLayer.clearLayers();

            const bounds = [];
            points.forEach((point) => {
                const latLng = addPoint(point);
                if (latLng) bounds.push(latLng);
            });

            if (bounds.length) {
                map.fitBounds(bounds, { padding: [30, 30], maxZoom: 7 });
                setStatus("");
            } else {
                setStatus("No map data available yet. Add traffic records to see markers.");
            }
        } catch (error) {
            console.error("Map data load failed:", error);
            setStatus("Unable to load map data. Check the API connection.");
        }
    }

    loadMapData();

    window.addEventListener("resize", () => {
        map.invalidateSize();
    });

    setTimeout(() => map.invalidateSize(), 300);
});
