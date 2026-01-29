<div align="center">

# 🚦 Traffic Accident Data Monitor

### Real-Time Traffic Analytics & Accident Visualization Platform

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

[🚀 Live Demo](https://imgur.com/a/0CQvSeR) • [📖 Documentation](#documentation) • [🤝 Contributing](#contributing)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Why This Project?](#-why-this-project)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Screenshots](#-screenshots)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 🌟 Overview

**Traffic Accident Data Monitor** is a comprehensive web-based platform that transforms raw traffic and accident data into actionable insights through interactive visualizations and real-time analytics. Built with Flask and modern web technologies, it provides city planners, researchers, and safety officials with powerful tools to understand traffic patterns, identify accident hotspots, and simulate traffic scenarios.

### 🎯 Key Highlights

- **Real-time Data Visualization**: Interactive maps powered by Leaflet.js display live traffic conditions and accident locations
- **Advanced Analytics**: Statistical analysis of accident trends across multiple cities with temporal insights
- **Traffic Simulations**: Dynamic traffic flow and intersection simulations to model real-world scenarios
- **User Authentication**: Secure login system with password recovery functionality
- **RESTful API**: Well-documented endpoints for programmatic data access
- **Responsive Design**: Modern, mobile-friendly interface built with HTML5, CSS3, and JavaScript

---

## 💡 Why This Project?

Traffic accidents are a leading cause of injuries and fatalities worldwide. This platform addresses critical needs in traffic safety by:

- **🔍 Identifying Patterns**: Discover accident hotspots and high-risk areas through data visualization
- **📈 Trend Analysis**: Track accident statistics over time to measure intervention effectiveness
- **🎓 Educational Tool**: Learn about traffic flow dynamics through interactive simulations
- **🛠️ Decision Support**: Provide data-driven insights for urban planning and traffic management
- **👥 Community Safety**: Help communities understand and improve local traffic safety

---

## ✨ Features

### Core Functionality

- 🗺️ **Interactive Traffic Map**
  - Real-time accident location markers
  - City-based filtering and search
  - Clustered markers for better visualization
  - Detailed accident information popups

- 📊 **Comprehensive Statistics Dashboard**
  - Overall traffic and accident summaries
  - City-specific analytics
  - Time-based trend analysis
  - Visual charts and graphs

- 🚦 **Traffic Light Simulator**
  - Realistic intersection traffic light cycles
  - Visual representation of traffic flow
  - Timing adjustments and controls
  - [View Demo](https://imgur.com/a/9CQZ0AY)

- 🚗 **Traffic Flow Simulation**
  - Vehicle merging patterns
  - Lane change dynamics
  - Speed variation modeling
  - Real-time animation

### User Management

- 🔐 **Authentication System**
  - Secure user registration
  - Login/logout functionality
  - Password hashing and validation
  - Session management

- 🔑 **Password Recovery**
  - Email-based password reset
  - Secure token generation
  - User-friendly recovery flow

### Developer Features

- 🔌 **RESTful API Endpoints**
  - `/api/map_data` - Traffic data for map visualization
  - `/api/stats/overall` - Global traffic statistics
  - `/api/stats/city/<city>` - City-specific data
  - `/api/user` - Current user information

- 🏗️ **Modular Architecture**
  - Separation of concerns with utility handlers
  - Easy to extend and maintain
  - Clean code structure
  - Comprehensive error handling

---

## 🛠️ Tech Stack

### Backend
- **Flask** - Python web framework
- **SQLite** - Lightweight database
- **Python 3.8+** - Core programming language

### Frontend
- **HTML5 & CSS3** - Modern markup and styling
- **JavaScript (ES6+)** - Interactive functionality
- **Leaflet.js** - Interactive mapping library
- **Chart.js** - Data visualization (implied)

### Architecture
- **MVC Pattern** - Model-View-Controller design
- **RESTful API** - Standard API architecture
- **Modular Design** - Utility handlers for different features
  - `db_handler.py` - Database operations
  - `stats_handler.py` - Statistical analysis
  - `map_handler.py` - Map data preparation
  - `user_handler.py` - User authentication
  - `simulation_handler.py` - Traffic simulations
  - `traffic_light_handler.py` - Intersection logic
  - `alert_handler.py` - Alert generation

---

## 📦 Installation

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ericchhun67/Traffic-Accident-Data-Monitor.git
   cd Traffic-Accident-Data-Monitor
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   If `requirements.txt` doesn't exist, install manually:
   ```bash
   pip install flask flask-session werkzeug
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the application**
   
   Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

### Configuration

- **Secret Key**: Set the `SECRET_KEY` environment variable for production
  ```bash
  export SECRET_KEY="your-secure-secret-key"
  ```

- **Database**: SQLite database is automatically initialized on first run

---

## 🎮 Usage

### Getting Started

1. **Register an Account**: Navigate to the registration page and create your account
2. **Login**: Use your credentials to access the platform
3. **Explore the Map**: View accident locations and filter by city
4. **Analyze Statistics**: Check the traffic data page for detailed analytics
5. **Run Simulations**: Test traffic scenarios with the simulation tools

### API Usage

Access traffic data programmatically:

```python
import requests

# Get overall statistics
response = requests.get('http://localhost:5000/api/stats/overall')
data = response.json()

# Get city-specific data
response = requests.get('http://localhost:5000/api/stats/city/Boston')
city_data = response.json()

# Get map data
response = requests.get('http://localhost:5000/api/map_data?city=Boston')
map_data = response.json()
```

---

## 📁 Project Structure

```
Traffic-Accident-Data-Monitor/
├── app.py                      # Main Flask application
├── templates/                  # HTML templates
│   ├── base.html              # Base template
│   ├── index.html             # Homepage
│   ├── login.html             # Login page
│   ├── register.html          # Registration page
│   ├── forgot_password.html   # Password recovery
│   ├── map.html               # Interactive map
│   ├── traffic_data.html      # Statistics dashboard
│   ├── traffic_simulation.html # Traffic simulator
│   └── traffic_light.html     # Traffic light simulator
├── utils/                      # Utility modules
│   ├── db_handler.py          # Database operations
│   ├── stats_handler.py       # Statistical analysis
│   ├── map_handler.py         # Map data handling
│   ├── user_handler.py        # User management
│   ├── simulation_handler.py  # Traffic simulations
│   ├── traffic_light_handler.py # Intersection logic
│   ├── alert_handler.py       # Alert generation
│   └── data_fetcher.py        # Data retrieval
├── *.css                       # Individual page stylesheets
├── js/                         # JavaScript files
├── img/                        # Image assets
└── README.md                   # This file
```

---

## 📸 Screenshots

### Homepage

<div align="center">
  <img src="https://github.com/user-attachments/assets/10cc7ab6-80ea-461e-a59e-b72eb9a01746" alt="Traffic Monitor Homepage" width="800"/>
  <p><em>Clean, intuitive homepage with easy navigation</em></p>
</div>

### User Registration

<div align="center">
  <img src="https://github.com/user-attachments/assets/cdc64d3b-fdbc-437b-b28d-3ba625d701bb" alt="Sign Up Page" width="800"/>
  <p><em>Secure user registration with validation</em></p>
</div>

### Login Interface

<div align="center">
  <img src="https://github.com/user-attachments/assets/483b6fce-96a6-4cca-a63a-5de19ffa5d19" alt="Login Page" width="800"/>
  <p><em>Simple and secure authentication</em></p>
</div>

### Accident Statistics Dashboard

<div align="center">
  <img src="https://github.com/user-attachments/assets/50c79c5f-4412-4c86-ba7b-f4f719598697" alt="Accident Stats" width="800"/>
  <p><em>Comprehensive statistics with city-based filtering</em></p>
</div>

### Traffic Flow Simulator

<div align="center">
  <img src="https://github.com/user-attachments/assets/06369cea-8fb6-4dc5-9177-fd2a7bc55df7" alt="Traffic Simulator" width="800"/>
  <p><em>Real-time traffic flow simulation - <a href="https://imgur.com/a/0CQvSeR">Watch Live Demo</a></em></p>
</div>

### Traffic Light Intersection Simulator

<div align="center">
  <img src="https://github.com/user-attachments/assets/587a029d-a3b1-4e82-b0c4-87b9ecc10ec3" alt="Traffic Light Simulator" width="800"/>
  <p><em>Interactive traffic light control - <a href="https://imgur.com/a/9CQZ0AY">Watch Live Demo</a></em></p>
</div>

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**!

### How to Contribute

1. **Fork the Project**
2. **Create your Feature Branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your Changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the Branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Development Guidelines

- Follow PEP 8 style guide for Python code
- Add comments for complex logic
- Update documentation for new features
- Test your changes thoroughly before submitting

### Ideas for Contributions

- 🌍 Add support for more cities and data sources
- 📱 Improve mobile responsiveness
- 🎨 Enhance UI/UX design
- 📊 Add more visualization types (heatmaps, time series)
- 🔔 Implement real-time notifications
- 🌐 Add internationalization (i18n)
- 🧪 Increase test coverage
- 📖 Improve documentation

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Contact

**Eric Chhun**

- GitHub: [@Ericchhun67](https://github.com/Ericchhun67)
- Project Link: [https://github.com/Ericchhun67/Traffic-Accident-Data-Monitor](https://github.com/Ericchhun67/Traffic-Accident-Data-Monitor)

---

## 🙏 Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - Web framework
- [Leaflet.js](https://leafletjs.com/) - Interactive maps
- [Font Awesome](https://fontawesome.com/) - Icons
- OpenStreetMap contributors for map data

---

<div align="center">

### ⭐ Star this repository if you find it helpful!

**Made with ❤️ by Eric Chhun**

[Back to Top ↑](#-traffic-accident-data-monitor)

</div>
