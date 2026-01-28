window.onload = () => {
  console.log("🚦 Traffic Light Simulation Initialized");

  // Get the canvas and context
  const canvas = document.getElementById("trafficCanvas");
  const ctx = canvas.getContext("2d");

  // Canvas dimensions
  const WIDTH = canvas.width;
  const HEIGHT = canvas.height;

  // Initial light state
  let lightState = {
    east_west: "GREEN",
    north_south: "RED",
  };

  // Car properties
  const cars = [
    { x: 50, y: 250, width: 50, height: 25, color: "blue", speed: 2 },
    { x: -150, y: 300, width: 50, height: 25, color: "red", speed: 2 },
    { x: -300, y: 350, width: 50, height: 25, color: "yellow", speed: 2 },
  ];

  // ==========================================================
  // DRAWING FUNCTIONS
  // ==========================================================

  // Draw background road
  function drawRoad() {
    ctx.fillStyle = "black";
    ctx.fillRect(0, 240, WIDTH, 100);

    // lane divider lines
    ctx.strokeStyle = "yellow";
    ctx.lineWidth = 4;
    ctx.setLineDash([25, 15]);
    ctx.beginPath();
    ctx.moveTo(0, 290);
    ctx.lineTo(WIDTH, 290);
    ctx.stroke();
    ctx.setLineDash([]);
  }

  // Draw cars
  function drawCars() {
    cars.forEach((car) => {
      ctx.fillStyle = car.color;
      ctx.fillRect(car.x, car.y, car.width, car.height);
    });
  }

  // Draw the traffic light
  function drawTrafficLight() {
    const lightX = WIDTH - 120;
    const lightY = 100;

    // Light pole box
    ctx.fillStyle = "#1c1c1c";
    ctx.fillRect(lightX, lightY, 60, 160);

    // Red
    ctx.beginPath();
    ctx.arc(lightX + 30, lightY + 30, 20, 0, Math.PI * 2);
    ctx.fillStyle = lightState.east_west === "RED" ? "red" : "#5a0000";
    ctx.fill();

    // Yellow
    ctx.beginPath();
    ctx.arc(lightX + 30, lightY + 80, 20, 0, Math.PI * 2);
    ctx.fillStyle = lightState.east_west === "YELLOW" ? "yellow" : "#5a5a00";
    ctx.fill();

    // Green
    ctx.beginPath();
    ctx.arc(lightX + 30, lightY + 130, 20, 0, Math.PI * 2);
    ctx.fillStyle = lightState.east_west === "GREEN" ? "limegreen" : "#003a00";
    ctx.fill();
  }

  // ==========================================================
  // LOGIC FUNCTIONS
  // ==========================================================

  // Update car motion based on light state
  function updateCars() {
    cars.forEach((car) => {
      // Stop zone before traffic light
      const stopLine = WIDTH / 2 - 100;

      if (lightState.east_west === "RED" && car.x + car.width > stopLine) {
        // stop the car
        car.speed = 0;
      } else if (lightState.east_west === "YELLOW" && car.x + car.width > stopLine - 30) {
        // slow down
        car.speed = 0.5;
      } else {
        // go
        car.speed = 2;
      }

      car.x += car.speed;
      if (car.x > WIDTH + 60) {
        car.x = -60; // reset when off-screen
      }
    });
  }

  // Fetch current light state from Flask backend
  async function fetchTrafficLightState() {
    try {
      const response = await fetch("/api/traffic_light_state");
      const data = await response.json();
      lightState = data;
    } catch (error) {
      console.error("⚠️ Error fetching traffic light state:", error);
    }
  }

  // ==========================================================
  // MAIN ANIMATION LOOP
  // ==========================================================
  function animate() {
    ctx.clearRect(0, 0, WIDTH, HEIGHT);
    drawRoad();
    drawCars();
    drawTrafficLight();
    updateCars();
    requestAnimationFrame(animate);
  }

  // ==========================================================
  // RUN SIMULATION
  // ==========================================================
  animate();
  setInterval(fetchTrafficLightState, 2000);
};