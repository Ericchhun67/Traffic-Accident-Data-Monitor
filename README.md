# 🚦 Traffic Accident Data Monitor

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.3+-green.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

A comprehensive Flask-powered Traffic & Accident Data Monitor that visualizes live traffic flow, accident trends, and city statistics. This project showcases modern web development with Python analytics, interactive Leaflet.js maps, real-time data processing, and engaging traffic simulations.

## 🌟 Features

- 🚗 **Real-time Traffic Visualization** - Interactive map displaying live traffic flow and density
- 📊 **Accident Analytics Dashboard** - Dynamic charts and statistics for accident trends
- 🚦 **Traffic Light Simulator** - Realistic traffic signal control system simulation  
- 🛣️ **Traffic Merging Simulation** - Visual representation of vehicle merging behavior
- 🔐 **User Authentication System** - Complete login, registration, and password recovery
- 🗄️ **SQLite Database** - Efficient data storage and retrieval
- 📱 **Responsive Design** - Works seamlessly across desktop and mobile devices

## 🛠️ Technology Stack

- **Backend:** Python, Flask
- **Database:** SQLite3
- **Frontend:** HTML5, CSS3, JavaScript
- **Mapping:** Leaflet.js
- **Data Processing:** Python statistics module
- **HTTP Requests:** requests library

## 📋 Prerequisites

Before running this application, ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package manager)
- Git

## 🚀 Installation & Setup

Follow these simple steps to get the application running:

```bash
# Clone the repository
git clone https://github.com/Ericchhun67/Traffic-Accident-Data-Monitor.git

# Navigate to the project directory
cd Traffic-Accident-Data-Monitor

# Install required dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

The application will start on `http://localhost:5000` by default.

## 📁 Project Structure

```
Traffic-Accident-Data-Monitor/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── templates/                  # HTML templates
│   ├── base.html              # Base template
│   ├── index.html             # Homepage
│   ├── login.html             # Login page
│   ├── register.html          # Registration page
│   └── ...
├── utils/                      # Backend utility modules
│   ├── db_handler.py          # Database operations
│   ├── user_handler.py        # User authentication
│   ├── stats_handler.py       # Statistics processing
│   ├── map_handler.py         # Map data preparation
│   └── ...
├── js/                         # JavaScript files
└── *.css                       # Stylesheet files
```

## 🎯 Usage

1. Start the application using `python app.py`
2. Open your browser and navigate to `http://localhost:5000`
3. Create an account or login with existing credentials
4. Explore the various features:
   - View real-time traffic data on the interactive map
   - Analyze accident statistics and trends
   - Experiment with traffic simulations

## 📸 Screenshots

### Homepage
![Homepage](https://github.com/user-attachments/assets/10cc7ab6-80ea-461e-a59e-b72eb9a01746)

### Sign Up Page
<img width="2054" height="1074" alt="Sign Up Page" src="https://github.com/user-attachments/assets/cdc64d3b-fdbc-437b-b28d-3ba625d701bb" />

### Login Page
<img width="2054" height="1074" alt="Login Page" src="https://github.com/user-attachments/assets/483b6fce-96a6-4cca-a63a-5de19ffa5d19" />

### Accident Statistics Dashboard
<img width="2054" height="1074" alt="Accident Statistics" src="https://github.com/user-attachments/assets/50c79c5f-4412-4c86-ba7b-f4f719598697" />

### Traffic Simulator
<img width="2054" height="1074" alt="Traffic Simulator" src="https://github.com/user-attachments/assets/06369cea-8fb6-4dc5-9177-fd2a7bc55df7" />

[📺 Live Demo Video](https://imgur.com/a/0CQvSeR)

### Traffic Light Simulator
<img width="2054" height="1074" alt="Traffic Light Simulator" src="https://github.com/user-attachments/assets/587a029d-a3b1-4e82-b0c4-87b9ecc10ec3" />

[📺 Live Demo Video](https://imgur.com/a/9CQZ0AY)

## 🔧 API Endpoints

- `GET /` - Homepage
- `GET /login` - Login page
- `POST /login` - Authenticate user
- `GET /register` - Registration page
- `POST /register` - Create new user account
- `GET /forgot_password` - Password recovery page
- `POST /forgot_password` - Reset user password
- `GET /logout` - Logout user
- `GET /api/user` - Get current user data
- `GET /map` - Interactive traffic map
- `GET /accident_info` - Accident information page
- `GET /traffic_data` - Traffic statistics page
- `GET /traffic_simulation` - Traffic merging simulation
- `GET /traffic_light` - Traffic light simulator

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**!

Please read our [Contributing Guidelines](CONTRIBUTING.md) before submitting a pull request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Eric Chhun**

- GitHub: [@Ericchhun67](https://github.com/Ericchhun67)

## 🙏 Acknowledgments

- Flask framework for the robust backend
- Leaflet.js for interactive mapping capabilities
- The open-source community for inspiration and support

## 📞 Support

If you have any questions or need help, please:
- Open an [issue](https://github.com/Ericchhun67/Traffic-Accident-Data-Monitor/issues)
- Check our [Contributing Guidelines](CONTRIBUTING.md)

## ⭐ Star History

If you find this project useful, please consider giving it a star! It helps others discover the project.

---

Made with ❤️ by Eric Chhun
