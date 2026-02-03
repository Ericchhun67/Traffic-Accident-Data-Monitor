window.addEventListener("load", () => {
  const canvas = document.getElementById("stopSignCanvas");
  const ctx = canvas.getContext("2d");

  const WIDTH = canvas.width;
  const HEIGHT = canvas.height;
  const center = { x: WIDTH / 2, y: HEIGHT / 2 };

  const roadWidth = 220;
  const roadHalf = roadWidth / 2;
  const laneOffset = 34;
  const laneWidth = 24;
  const intersectionHalf = 70;
  const stopLineOffset = 12;

  const baseSpeed = 2.2;
  const minStopMs = 700;
  const spawnIntervalMs = 1400;
  const spawnClearance = 92;

  let cars = [];
  let arrivalCounter = 0;
  let carIdCounter = 0;
  let activeCarId = null;
  let spawnEnabled = true;

  const directionVectors = {
    north: { x: 0, y: -1 },
    south: { x: 0, y: 1 },
    east: { x: 1, y: 0 },
    west: { x: -1, y: 0 },
  };

  const stopLines = {
    north: center.y + intersectionHalf + stopLineOffset,
    south: center.y - intersectionHalf - stopLineOffset,
    east: center.x - intersectionHalf - stopLineOffset,
    west: center.x + intersectionHalf + stopLineOffset,
  };

  const spawnPoints = {
    north: {
      x: center.x - laneOffset - laneWidth / 2,
      y: HEIGHT + 70,
      w: laneWidth,
      h: 46,
    },
    south: {
      x: center.x + laneOffset - laneWidth / 2,
      y: -70,
      w: laneWidth,
      h: 46,
    },
    east: {
      x: -70,
      y: center.y - laneOffset - laneWidth / 2,
      w: 46,
      h: laneWidth,
    },
    west: {
      x: WIDTH + 70,
      y: center.y + laneOffset - laneWidth / 2,
      w: 46,
      h: laneWidth,
    },
  };

  const colors = ["#2f80ed", "#eb5757", "#f2c94c", "#27ae60", "#9b51e0"]; 

  function createCar(direction) {
    const spawn = spawnPoints[direction];
    return {
      id: ++carIdCounter,
      direction,
      x: spawn.x,
      y: spawn.y,
      w: spawn.w,
      h: spawn.h,
      speed: baseSpeed,
      state: "approach",
      stopTime: null,
      arrivalOrder: null,
      enteredIntersection: false,
      color: colors[carIdCounter % colors.length],
      label: direction.charAt(0).toUpperCase() + carIdCounter,
    };
  }

  function canSpawn(direction) {
    const spawn = spawnPoints[direction];
    const sameDir = cars.filter((car) => car.direction === direction && car.state !== "exit");
    if (sameDir.length === 0) return true;

    if (direction === "north") {
      const nearest = sameDir.reduce((maxCar, car) => (car.y > maxCar.y ? car : maxCar));
      return spawn.y - nearest.y > spawnClearance;
    }

    if (direction === "south") {
      const nearest = sameDir.reduce((minCar, car) => (car.y < minCar.y ? car : minCar));
      return nearest.y - spawn.y > spawnClearance;
    }

    if (direction === "east") {
      const nearest = sameDir.reduce((minCar, car) => (car.x < minCar.x ? car : minCar));
      return nearest.x - spawn.x > spawnClearance;
    }

    const nearest = sameDir.reduce((maxCar, car) => (car.x > maxCar.x ? car : maxCar));
    return spawn.x - nearest.x > spawnClearance;
  }

  function spawnCars() {
    if (!spawnEnabled) return;
    ["north", "south", "east", "west"].forEach((direction) => {
      if (Math.random() < 0.45 && canSpawn(direction)) {
        cars.push(createCar(direction));
      }
    });
  }

  function reachedStopLine(car) {
    if (car.direction === "north") {
      return car.y <= stopLines.north;
    }
    if (car.direction === "south") {
      return car.y + car.h >= stopLines.south;
    }
    if (car.direction === "east") {
      return car.x + car.w >= stopLines.east;
    }
    return car.x <= stopLines.west;
  }

  function clampToStopLine(car) {
    if (car.direction === "north") {
      car.y = stopLines.north;
    } else if (car.direction === "south") {
      car.y = stopLines.south - car.h;
    } else if (car.direction === "east") {
      car.x = stopLines.east - car.w;
    } else {
      car.x = stopLines.west;
    }
  }

  function isInIntersection(car) {
    const carCenterX = car.x + car.w / 2;
    const carCenterY = car.y + car.h / 2;
    return (
      carCenterX >= center.x - intersectionHalf &&
      carCenterX <= center.x + intersectionHalf &&
      carCenterY >= center.y - intersectionHalf &&
      carCenterY <= center.y + intersectionHalf
    );
  }

  function shouldGo(car, now) {
    if (activeCarId !== null) return false;
    const stoppedCars = cars.filter((c) => c.state === "stopped");
    if (stoppedCars.length === 0) return false;

    stoppedCars.sort((a, b) => a.arrivalOrder - b.arrivalOrder);
    const firstCar = stoppedCars[0];
    return firstCar.id === car.id && now - car.stopTime >= minStopMs;
  }

  function updateCars() {
    const now = performance.now();

    cars.forEach((car) => {
      const vector = directionVectors[car.direction];

      if (car.state === "approach") {
        car.x += car.speed * vector.x;
        car.y += car.speed * vector.y;

        if (reachedStopLine(car)) {
          clampToStopLine(car);
          car.state = "stopped";
          car.stopTime = now;
          car.arrivalOrder = ++arrivalCounter;
        }
      } else if (car.state === "stopped") {
        if (shouldGo(car, now)) {
          car.state = "crossing";
          activeCarId = car.id;
        }
      } else {
        car.x += car.speed * vector.x;
        car.y += car.speed * vector.y;

        if (car.state === "crossing") {
          if (isInIntersection(car)) {
            car.enteredIntersection = true;
          } else if (car.enteredIntersection) {
            car.state = "exit";
            activeCarId = null;
          }
        }
      }
    });

    cars = cars.filter(
      (car) =>
        car.x > -120 &&
        car.x < WIDTH + 120 &&
        car.y > -120 &&
        car.y < HEIGHT + 120
    );
  }

  function drawRoad() {
    ctx.fillStyle = "#e6edf5";
    ctx.fillRect(0, 0, WIDTH, HEIGHT);

    ctx.fillStyle = "#2b2b2b";
    ctx.fillRect(center.x - roadHalf, 0, roadWidth, HEIGHT);
    ctx.fillRect(0, center.y - roadHalf, WIDTH, roadWidth);

    ctx.strokeStyle = "#f0d84c";
    ctx.lineWidth = 3;
    ctx.setLineDash([18, 14]);

    ctx.beginPath();
    ctx.moveTo(center.x - laneOffset, 0);
    ctx.lineTo(center.x - laneOffset, HEIGHT);
    ctx.moveTo(center.x + laneOffset, 0);
    ctx.lineTo(center.x + laneOffset, HEIGHT);
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(0, center.y - laneOffset);
    ctx.lineTo(WIDTH, center.y - laneOffset);
    ctx.moveTo(0, center.y + laneOffset);
    ctx.lineTo(WIDTH, center.y + laneOffset);
    ctx.stroke();

    ctx.setLineDash([]);

    ctx.strokeStyle = "#ffffff";
    ctx.lineWidth = 4;

    ctx.beginPath();
    ctx.moveTo(center.x - roadHalf, stopLines.north);
    ctx.lineTo(center.x + roadHalf, stopLines.north);
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(center.x - roadHalf, stopLines.south);
    ctx.lineTo(center.x + roadHalf, stopLines.south);
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(stopLines.east, center.y - roadHalf);
    ctx.lineTo(stopLines.east, center.y + roadHalf);
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(stopLines.west, center.y - roadHalf);
    ctx.lineTo(stopLines.west, center.y + roadHalf);
    ctx.stroke();
  }

  function drawOctagon(cx, cy, size) {
    const step = (Math.PI * 2) / 8;
    ctx.beginPath();
    for (let i = 0; i < 8; i += 1) {
      const angle = step * i + Math.PI / 8;
      const x = cx + size * Math.cos(angle);
      const y = cy + size * Math.sin(angle);
      if (i === 0) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    }
    ctx.closePath();
    ctx.fill();
  }

  function drawStopSigns() {
    const signOffset = intersectionHalf + 36;
    const signSize = 16;

    const positions = [
      { x: center.x - signOffset, y: center.y - signOffset },
      { x: center.x + signOffset, y: center.y - signOffset },
      { x: center.x - signOffset, y: center.y + signOffset },
      { x: center.x + signOffset, y: center.y + signOffset },
    ];

    positions.forEach((pos) => {
      ctx.fillStyle = "#c0392b";
      drawOctagon(pos.x, pos.y, signSize);
      ctx.fillStyle = "#ffffff";
      ctx.font = "bold 10px Poppins, sans-serif";
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillText("STOP", pos.x, pos.y + 1);
    });
  }

  function drawCars() {
    cars.forEach((car) => {
      ctx.fillStyle = car.color;
      ctx.fillRect(car.x, car.y, car.w, car.h);

      ctx.fillStyle = "rgba(255,255,255,0.75)";
      if (car.w > car.h) {
        ctx.fillRect(car.x + 6, car.y + 5, car.w - 12, car.h - 10);
      } else {
        ctx.fillRect(car.x + 5, car.y + 6, car.w - 10, car.h - 12);
      }
    });
  }

  function drawHud() {
    ctx.fillStyle = "#1f2937";
    ctx.font = "14px Poppins, sans-serif";
    ctx.textAlign = "left";
    ctx.textBaseline = "top";

    const queue = cars
      .filter((car) => car.state === "stopped")
      .sort((a, b) => a.arrivalOrder - b.arrivalOrder)
      .map((car) => car.label);

    ctx.fillText(`Queue: ${queue.length ? queue.join(" -> ") : "none"}`, 18, 16);

    const activeCar = cars.find((car) => car.id === activeCarId);
    ctx.fillText(`Crossing: ${activeCar ? activeCar.label : "none"}`, 18, 36);
  }

  function animate() {
    ctx.clearRect(0, 0, WIDTH, HEIGHT);
    drawRoad();
    drawStopSigns();
    updateCars();
    drawCars();
    drawHud();
    requestAnimationFrame(animate);
  }

  const toggleSpawnBtn = document.getElementById("toggleSpawn");
  const resetBtn = document.getElementById("resetSim");

  toggleSpawnBtn.addEventListener("click", () => {
    spawnEnabled = !spawnEnabled;
    toggleSpawnBtn.textContent = spawnEnabled ? "Pause Spawns" : "Resume Spawns";
  });

  resetBtn.addEventListener("click", () => {
    cars = [];
    activeCarId = null;
    arrivalCounter = 0;
  });

  setInterval(spawnCars, spawnIntervalMs);
  animate();
});
