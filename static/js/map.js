document.addEventListener("DOMContentLoaded", () => {
    console.log(" map.js loaded and running");

    // Make sure Leaflet is available
    if (typeof L === "undefined") {
        console.error(" Leaflet (L) is not defined. Check your leaflet.js script tag.");
        return;
    }

    // Initialize the map (centered roughly on the US)
    const map = L.map('map').setView([37.09, -95.71], 4);

    // Add OpenStreetMap tiles
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; OpenStreetMap contributors'
    }).addTo(map);

    console.log("✅ Tile layer added to map");

    // Example city data with AQI values
    const cityData = [
        { name: "Los Angeles", lat: 34.05, lon: -118.25, aqi: 72 },
        { name: "San Francisco", lat: 37.77, lon: -122.42, aqi: 65 },
        { name: "New York", lat: 40.71, lon: -74.01, aqi: 90 },
        { name: "Chicago", lat: 41.88, lon: -87.63, aqi: 110 },
        { name: "Houston", lat: 29.76, lon: -95.37, aqi: 130 },
        { name: "Miami", lat: 25.76, lon: -80.19, aqi: 70 },
        { name: "Seattle", lat: 47.61, lon: -122.33, aqi: 45 },
        { name: "San Jose", lat: 37.34, lon: -121.89, aqi: 50 },
        { name: "Fremont", lat: 37.55, lon: -121.98, aqi: 75 },
        { name: "Palo Alto", lat: 37.44, lon: -122.16, aqi: 85 },
    ];

    // Get color based on AQI
    function getColor(aqi) {
        if (aqi <= 50) return "green";
        if (aqi <= 100) return "yellow";
        return "red";
    }

    // Add markers for each city
    cityData.forEach(city => {
        const marker = L.circleMarker([city.lat, city.lon], {
            radius: 10,
            color: getColor(city.aqi),
            fillColor: getColor(city.aqi),
            fillOpacity: 0.8
        }).addTo(map);

        marker.bindPopup(`
            <b>${city.name}</b><br>
            AQI: ${city.aqi}<br>
            Status: ${city.aqi <= 50 ? 'Good' : city.aqi <= 100 ? 'Moderate' : 'Unhealthy'}
        `);
    });
});