<h1 align="center">🚦 Traffic & Accident Data Monitor</h1>

<p align="center">
  <strong>Real-time traffic monitoring, accident analytics, and interactive transportation dashboards</strong>
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=2800&pause=900&color=F97316&center=true&vCenter=true&width=850&lines=Monitor+traffic+conditions+in+real+time;Analyze+accident+patterns+and+trends;Visualize+traffic+data+with+interactive+maps;Explore+dashboards+for+smarter+city+planning" alt="Typing animation" />
</p>

<p align="center">
  <a href="https://github.com/Ericchhun67/Traffic-Accident-Data-Monitor">
    <img src="https://img.shields.io/github/stars/Ericchhun67/Traffic-Accident-Data-Monitor?style=social" alt="GitHub stars" />
  </a>
  <img src="https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python badge" />
  <img src="https://img.shields.io/badge/Flask-Web%20App-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask badge" />
  <img src="https://img.shields.io/badge/Leaflet.js-Maps-199900?style=for-the-badge&logo=leaflet&logoColor=white" alt="Leaflet badge" />
  <img src="https://img.shields.io/badge/License-MIT-FACC15?style=for-the-badge" alt="MIT license badge" />
</p>

---

## Overview

**Traffic & Accident Data Monitor** helps users explore traffic flow, accident patterns, congestion areas, and simulation-based insights.

The project combines a Python and Flask backend with frontend visualizations, RESTful API routes, user authentication, traffic simulations, and data analytics. It is designed as a real-world full-stack project focused on transportation, safety, and smart city planning.

## Features

### Traffic Monitoring

- View traffic conditions through interactive map-based visualizations
- Explore accident locations and traffic density data
- Filter and analyze traffic-related information by location or condition

### Accident Analytics

- Analyze accident trends and traffic safety patterns
- View key statistics through charts and dashboards
- Identify high-risk areas and recurring traffic issues

### Traffic Simulation

- Run traffic flow simulations
- Test traffic light behavior and road merging scenarios
- Explore how different traffic conditions affect congestion

### User Management

- User registration and login
- Session-based authentication
- User-specific access to dashboard features

### Backend System

- Flask-based server architecture
- SQLite database for persistent storage
- Modular utility handlers for data, alerts, users, maps, and simulations
- RESTful API endpoints for frontend/backend communication

## Tech Stack

| Area | Technologies |
|------|-------------|
| Backend | Python, Flask |
| Frontend | HTML, CSS, JavaScript |
| Database | SQLite |
| Maps | Leaflet.js |
| Data Processing | pandas, NumPy |
| Architecture | Modular handlers, MVC-style structure |

## Quick Start

### Prerequisites

- Python 3.8+
- pip
- A modern web browser

### Installation

```bash
git clone https://github.com/Ericchhun67/Traffic-Accident-Data-Monitor.git
cd Traffic-Accident-Data-Monitor
pip install -r requirements.txt
python app.py
Open the app in your browser:

http://localhost:5000
Project Structure
Traffic-Accident-Data-Monitor/
├── app.py
├── requirements.txt
├── utils/
│   ├── db_handler.py
│   ├── stats_handler.py
│   ├── alert_handler.py
│   ├── user_handler.py
│   ├── map_handler.py
│   ├── simulation_handler.py
│   └── traffic_light_handler.py
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   └── map.html
├── static/
│   ├── css/
│   └── js/
└── img/
API Endpoints
Method	Endpoint	Description
POST	/register	Register a new user
POST	/login	Log in an existing user
GET	/logout	Log out the current user
GET	/api/traffic-data	Fetch traffic data
GET	/api/accidents	Fetch accident statistics
GET	/api/alerts	Fetch active alerts
POST	/api/simulate	Run a traffic simulation step
Use Cases
Analyze traffic and accident patterns
Support smart city and transportation planning
Study traffic flow and congestion behavior
Experiment with traffic light timing and simulations
Build a foundation for real-time traffic monitoring systems
Future Improvements
Add real-time traffic API integration
Improve dashboard filtering and search
Add advanced predictive analytics
Expand test coverage
Improve responsive UI design
Add deployment support
Contributing
Contributions are welcome.

Fork the repository
Create a new branch
Make your changes
Commit your work
Open a pull request
License
This project is licensed under the MIT License.

Author
Created by Eric Chhun.

If you find this project useful, consider starring the repository.
