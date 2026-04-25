<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0F172A,50:2563EB,100:F97316&height=220&section=header&text=Traffic%20%26%20Accident%20Data%20Monitor&fontSize=38&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Real-Time%20Traffic%20Analytics%20%7C%20Accident%20Insights%20%7C%20Interactive%20Dashboards&descAlignY=58&descSize=16" alt="Traffic Accident Data Monitor animated header" />
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&duration=2800&pause=900&color=F97316&center=true&vCenter=true&width=850&lines=Monitor+traffic+conditions+in+real+time;Analyze+accident+patterns+and+trends;Visualize+data+with+interactive+dashboards;Simulate+traffic+scenarios+for+better+planning" alt="Typing animation" />
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

**Traffic & Accident Data Monitor** is a full-stack web application for monitoring traffic conditions, analyzing accident trends, and visualizing transportation data through interactive dashboards.

The project combines a Python and Flask backend with dynamic frontend visualizations to help users explore traffic flow, accident patterns, congestion areas, and simulation-based insights. It is designed for learning full-stack development while solving a real-world urban mobility problem.

## Why This Project?

- **Real-World Use Case**: Focuses on traffic safety, congestion, and accident analysis
- **Full-Stack Development**: Combines backend APIs, frontend dashboards, and data-driven UI
- **Interactive Maps**: Uses map-based visualizations for traffic and accident data
- **Analytics Focused**: Highlights trends, patterns, and key transportation metrics
- **Simulation Ready**: Supports experimenting with traffic scenarios and possible improvements

---

## Key Features

### Live Map Visualization

- Interactive traffic map powered by Leaflet.js
- Accident markers with location-based details
- Traffic density and congestion visualization
- Zoom, filter, and explore city-level traffic data

### Analytics Dashboard

- Accident trend analysis with charts and visual insights
- Traffic statistics and key performance indicators
- Historical accident and congestion pattern tracking
- Dashboard views for quick decision-making

### Intelligent Alert System

- Accident and congestion alert support
- Emergency-response-focused notifications
- Filterable alerts by severity, location, or traffic condition
- Designed to support real-time monitoring workflows


### 🚦 **Traffic Simulation Engine**
- Interactive traffic light simulator
- Road merging simulation with collision detection
- Test traffic management strategies
- Educational tool for understanding traffic dynamics

### 👥 **User Management**
- Secure user registration and login
- Password reset functionality
- Session-based authentication
- User-specific preferences and dashboards

### 💾 **Robust Data Backend**
- SQLite database for persistent storage
- Modular data handlers for easy maintenance
- Real-time data synchronization
- RESTful API endpoints for frontend-backend communication

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Backend** | Python, Flask, SQLite |
| **Frontend** | HTML5, CSS3, JavaScript, Leaflet.js |
| **Data Processing** | Python pandas/numpy |
| **Architecture** | Modular handlers, MVC pattern |

**Language Distribution:**
- Python: 55.7% (Backend logic & analytics)
- HTML: 16.4% (Structure)
- CSS: 16.5% (Styling)
- JavaScript: 11.4% (Frontend interactivity)

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip package manager
- Modern web browser

### Installation

```bash
# Clone the repository
git clone https://github.com/Ericchhun67/Traffic-Accident-Data-Monitor.git
cd Traffic-Accident-Data-Monitor

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

The application will be available at `http://localhost:5000`

---

## 📸 Screenshots

### 🏠 Dashboard & Homepage
![Homepage](https://github.com/user-attachments/assets/10cc7ab6-80ea-461e-a59e-b72eb9a01746)
*Main dashboard showing traffic overview and key metrics*

### 📝 User Registration
![Sign Up](https://github.com/user-attachments/assets/cdc64d3b-fdbc-437b-b28d-3ba625d701bb)
*Intuitive registration interface with validation*

### 🔐 Login Portal
![Login](https://github.com/user-attachments/assets/483b6fce-96a6-4cca-a63a-5de19ffa5d19)
*Secure authentication system*

### 📊 Accident Analytics
![Accident Stats](https://github.com/user-attachments/assets/50c79c5f-4412-4c86-ba7b-f4f719598697)
*Interactive charts showing accident trends and statistics*

### 🚗 Traffic Simulator
![Simulator](https://github.com/user-attachments/assets/06369cea-8fb6-4dc5-9177-fd2a7bc55df7)
*Real-time traffic flow simulation with vehicle dynamics*

[Live Demo](https://imgur.com/a/0CQvSeR)

### 🚦 Traffic Light Controller
![Traffic Light](https://github.com/user-attachments/assets/587a029d-a3b1-4e82-b0c4-87b9ecc10ec3)
*Intelligent traffic light timing optimization*

[Live Demo](https://imgur.com/a/9CQZ0AY)

---

## 📁 Project Structure

```
Traffic-Accident-Data-Monitor/
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── utils/
│   ├── db_handler.py              # Database operations
│   ├── stats_handler.py           # Analytics & statistics
│   ├── alert_handler.py           # Alert generation
│   ├── user_handler.py            # User management
│   ├── map_handler.py             # Map data processing
│   ├── simulation_handler.py       # Traffic simulation
│   ├── traffic_light_handler.py    # Traffic light logic
│   └── ...
├── templates/                      # HTML templates
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── map.html
│   └── ...
├── static/
│   ├── css/                        # Stylesheets
│   └── js/                         # JavaScript files
└── img/                            # Images & assets
```

---

## 🔧 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/register` | Register new user |
| POST | `/login` | User login |
| GET | `/logout` | User logout |
| GET | `/api/traffic-data` | Fetch real-time traffic data |
| GET | `/api/accidents` | Get accident statistics |
| GET | `/api/user/<id>` | Get user information |
| POST | `/api/simulate` | Run traffic simulation step |
| GET | `/api/alerts` | Fetch active alerts |

---

## 💡 Use Cases

- **City Planning**: Analyze traffic patterns to optimize infrastructure
- **Emergency Response**: Real-time incident tracking and response coordination
- **Traffic Engineering**: Test traffic light timing and road modifications
- **Research & Education**: Study traffic dynamics and accident patterns
- **Smart City Development**: Foundation for IoT and real-time monitoring systems

---
🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** changes (`git commit -m 'Add AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Areas for Contribution
- 🐛 Bug fixes and optimizations
- ✨ New features (real-time updates, advanced analytics)
- 📚 Documentation improvements
- 🧪 Test coverage
- 🎨 UI/UX enhancements

📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👤 About the Author

**Ericchhun67** - Full-stack developer interested in transportation systems and data visualization.

[GitHub Profile](https://github.com/Ericchhun67) | [Report Issues](https://github.com/Ericchhun67/Traffic-Accident-Data-Monitor/issues)

🌟 Show Your Support

If you find this project helpful, please:
- ⭐ **Star this repository**
- 🍴 **Fork** for your own use
- 💬 **Share** with your network
- 🐛 **Report issues** to improve the project

