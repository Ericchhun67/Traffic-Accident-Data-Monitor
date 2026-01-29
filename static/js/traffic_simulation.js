console.log("🚦 Traffic Flow Simulation — accidents + slowdowns active");

const canvas = document.getElementById("trafficCanvas");
const ctx = canvas.getContext("2d");
canvas.width = window.innerWidth * 0.9;
canvas.height = window.innerHeight * 0.7;

let cars = [];
let accidentZones = [];

// Function to spawn cars on lanes
function spawnCar(lane) {
  const yPos =
    lane === "main"
      ? canvas.height / 2 - 25
      : lane === "merge"
      ? canvas.height / 2 + 60
      : canvas.height / 2 - 100;

  cars.push({
    x: lane === "merge" ? -80 : 50,
    y: yPos,
    lane,
    color: `hsl(${Math.random() * 360}, 70%, 55%)`,
    speed: 4,
    merging: lane === "merge",
    exiting: false,
  });
}

// Draw the road
function drawRoad() {
  ctx.fillStyle = "#1b1b1b";
  ctx.fillRect(0, canvas.height / 2 - 60, canvas.width, 120);

  // Dashed center line
  ctx.strokeStyle = "yellow";
  ctx.lineWidth = 4;
  for (let i = 0; i < canvas.width; i += 60) {
    ctx.beginPath();
    ctx.moveTo(i, canvas.height / 2);
    ctx.lineTo(i + 30, canvas.height / 2);
    ctx.stroke();
  }

  // Merge lane
  ctx.beginPath();
  ctx.moveTo(0, canvas.height / 2 + 120);
  ctx.lineTo(300, canvas.height / 2);
  ctx.lineTo(0, canvas.height / 2 + 60);
  ctx.closePath();
  ctx.fill();

  // Exit lane
  ctx.beginPath();
  ctx.moveTo(canvas.width - 300, canvas.height / 2);
  ctx.lineTo(canvas.width, canvas.height / 2 - 120);
  ctx.lineTo(canvas.width, canvas.height / 2 - 60);
  ctx.closePath();
  ctx.fill();
}

// Draw car
function drawCar(car) {
  ctx.fillStyle = car.color;
  ctx.fillRect(car.x, car.y, 60, 35);
}

// Draw accident zones
function drawAccidents() {
  accidentZones.forEach(zone => {
    ctx.fillStyle = "rgba(255, 0, 0, 0.6)";
    ctx.beginPath();
    ctx.arc(zone.x, zone.y, 50, 0, Math.PI * 2);
    ctx.fill();
  });
}

// Update cars
function updateCars() {
  cars.forEach(car => {
    // Check if near accident
    const nearAccident = accidentZones.some(zone => Math.abs(car.x - zone.x) < 150);

    // Adjust speed
    if (nearAccident) car.speed = 1; // slow down
    else car.speed = Math.min(car.speed + 0.1, 4); // gradually speed back up

    // Move
    car.x += car.speed;

    // Merge logic
    if (car.merging) {
      car.y -= 0.7;
      if (car.y <= canvas.height / 2 - 25) {
        car.merging = false;
        car.lane = "main";
      }
    }

    // Random exit logic
    if (!car.exiting && car.lane === "main" && car.x > canvas.width - 400 && Math.random() < 0.02) {
      car.exiting = true;
    }

    if (car.exiting) {
      car.y -= 1;
    }
  });

  // Remove cars leaving screen
  cars = cars.filter(car => car.x < canvas.width + 100 && car.y > -50);
}

// Trigger random accidents
function triggerAccidents() {
  if (Math.random() < 0.03 && accidentZones.length < 2) {
    const randomCar = cars[Math.floor(Math.random() * cars.length)];
    if (randomCar) {
      accidentZones.push({ x: randomCar.x + 30, y: randomCar.y + 20 });
      console.log("💥 Accident occurred at:", randomCar.x);

      // Remove after 6 seconds
      setTimeout(() => {
        accidentZones.shift();
      }, 6000);
    }
  }
}

// Animate everything
function animate() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  drawRoad();
  drawAccidents();
  updateCars();
  cars.forEach(drawCar);
  triggerAccidents();
  requestAnimationFrame(animate);
}

// Spawn cars every 2s
setInterval(() => {
  if (Math.random() < 0.7) spawnCar("main");
  if (Math.random() < 0.4) spawnCar("merge");
}, 2000);

animate();