# Architecture Documentation

## Overview

The Traffic Accident Data Monitor is a web-based application built with Flask that provides real-time traffic monitoring, accident analytics, and interactive simulations. The application follows a modular architecture with clear separation of concerns.

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        Frontend Layer                        │
│  (HTML Templates, CSS, JavaScript, Leaflet.js)              │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      │ HTTP Requests
                      │
┌─────────────────────▼───────────────────────────────────────┐
│                     Flask Application                        │
│                        (app.py)                              │
│  ┌────────────────────────────────────────────────────────┐ │
│  │              Route Handlers                            │ │
│  │  - Authentication Routes                               │ │
│  │  - Page Routes                                         │ │
│  │  - API Endpoints                                       │ │
│  └───────────────────┬────────────────────────────────────┘ │
└────────────────────┬─┴─────────────────────────────────────┘
                     │
                     │ Function Calls
                     │
┌────────────────────▼──────────────────────────────────────┐
│                  Backend Utilities Layer                   │
│                     (utils/)                               │
│  ┌──────────────────────────────────────────────────────┐ │
│  │  • db_handler.py       - Database operations         │ │
│  │  • user_handler.py     - User authentication         │ │
│  │  • stats_handler.py    - Statistics processing       │ │
│  │  • map_handler.py      - Map data preparation        │ │
│  │  • data_fetcher.py     - External data fetching      │ │
│  │  • alert_handler.py    - Alert generation            │ │
│  │  • simulation_handler  - Traffic simulation logic    │ │
│  │  • traffic_light_handler - Traffic light control     │ │
│  └───────────────────┬──────────────────────────────────┘ │
└────────────────────┬─┴────────────────────────────────────┘
                     │
                     │ SQL Queries
                     │
┌────────────────────▼──────────────────────────────────────┐
│                   Data Layer                               │
│                  SQLite Database                           │
│  - Users Table                                             │
│  - Traffic Data Table                                      │
│  - Accident Data Table                                     │
│  - City Data Table                                         │
└────────────────────────────────────────────────────────────┘
```

## Component Details

### 1. Frontend Layer

#### Templates (`templates/`)
- **base.html**: Base template with common layout and navigation
- **index.html**: Homepage template
- **login.html**: User login page
- **register.html**: User registration page
- **map.html**: Interactive traffic map
- **traffic_data.html**: Traffic statistics dashboard
- **accident_info.html**: Accident information page
- **traffic_simulation.html**: Traffic simulation page
- **traffic_light.html**: Traffic light simulator page
- **forgot_password.html**: Password recovery page

#### Static Assets (`static/`)
- **css/**: Stylesheet files for each page
- **js/**: JavaScript files for interactive features
  - `map.js`: Leaflet map initialization and interaction
  - `traffic_light.js`: Traffic light simulation logic
  - `traffic_simulation.js`: Traffic merging simulation

### 2. Application Layer (`app.py`)

The main Flask application that orchestrates all components:

- **Route Handlers**: Define URL endpoints and handle HTTP requests
- **Session Management**: Manages user authentication state
- **Template Rendering**: Renders HTML templates with dynamic data
- **Error Handling**: Catches and handles exceptions gracefully

### 3. Backend Utilities Layer (`utils/`)

Modular utility functions organized by responsibility:

#### Database Handler (`db_handler.py`)
- Initializes database schema
- Provides CRUD operations for all tables
- Manages database connections with context managers
- Functions: `init_db()`, `get_all_traffic_data()`, `get_city_data()`, `get_accident_data()`

#### User Handler (`user_handler.py`)
- User registration and authentication
- Password hashing and verification
- Password reset functionality
- Functions: `register_user()`, `login_user()`, `get_user_by_email()`, `reset_password()`

#### Statistics Handler (`stats_handler.py`)
- Calculates traffic statistics
- Aggregates accident data
- Generates summary reports
- Functions: `overall_summary()`, `summarize_city_traffic()`, `summarize_accidents()`

#### Map Handler (`map_handler.py`)
- Prepares geospatial data for map visualization
- Formats data for Leaflet.js consumption
- Functions: `prepare_map_data()`

#### Data Fetcher (`data_fetcher.py`)
- Fetches external traffic data
- Generates mock data for development
- Functions: `get_traffic_data()`

#### Alert Handler (`alert_handler.py`)
- Analyzes traffic patterns
- Generates alerts for anomalies
- Functions: `generate_alerts()`

#### Simulation Handler (`simulation_handler.py`)
- Controls traffic simulation logic
- Manages vehicle movement
- Functions: `run_simulation_step()`

#### Traffic Light Handler (`traffic_light_handler.py`)
- Manages traffic light states
- Controls timing sequences
- Functions: `get_intersection_state()`

### 4. Data Layer

SQLite database with the following tables:

#### Users Table
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
```

#### Traffic Data Table
```sql
CREATE TABLE traffic_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    location TEXT NOT NULL,
    latitude REAL,
    longitude REAL,
    volume INTEGER,
    speed REAL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
```

#### Accident Data Table
```sql
CREATE TABLE accident_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    location TEXT NOT NULL,
    latitude REAL,
    longitude REAL,
    severity TEXT,
    date TIMESTAMP,
    description TEXT
)
```

## Data Flow

### User Authentication Flow
1. User submits credentials via login form
2. Flask receives POST request at `/login`
3. `login_user()` validates credentials against database
4. Session is created with user information
5. User is redirected to homepage

### Traffic Map Display Flow
1. User navigates to `/map`
2. Flask calls `prepare_map_data()` to fetch traffic data
3. `db_handler` queries traffic_data table
4. Data is formatted as GeoJSON
5. Template renders with Leaflet.js
6. JavaScript initializes map and places markers

### Statistics Generation Flow
1. User navigates to `/traffic_data`
2. Flask calls multiple handler functions:
   - `overall_summary()` for general stats
   - `summarize_city_traffic()` for city-specific data
   - `summarize_accidents()` for accident trends
3. Statistics are calculated from database
4. Template renders charts and tables

## Security Architecture

### Authentication
- Session-based authentication using Flask sessions
- Secure session cookies
- Password hashing (implementation details in user_handler.py)

### Database Security
- Parameterized queries to prevent SQL injection
- Context managers for proper connection handling
- Input validation on all user inputs

### Best Practices
- Environment variables for sensitive configuration
- HTTPS recommended for production
- CSRF protection should be added for production use

## Scalability Considerations

### Current Limitations
- SQLite suitable for small to medium applications
- Single-server deployment

### Future Improvements
- Migrate to PostgreSQL for better concurrency
- Add caching layer (Redis) for frequent queries
- Implement API rate limiting
- Add load balancing for horizontal scaling
- Implement real-time updates with WebSockets

## Development Workflow

1. **Local Setup**: Clone repository, install dependencies
2. **Database Initialization**: Automatic on first run via `init_db()`
3. **Development Server**: Run with `python app.py`
4. **Testing**: Manual testing recommended
5. **Deployment**: Configure production settings, use WSGI server (e.g., Gunicorn)

## Technologies Used

- **Backend**: Python 3.8+, Flask 2.3+
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3, JavaScript ES6+
- **Mapping**: Leaflet.js 1.9+
- **HTTP Requests**: requests library

## File Structure Summary

```
Traffic-Accident-Data-Monitor/
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── LICENSE                         # MIT License
├── README.md                       # Project documentation
├── CONTRIBUTING.md                 # Contribution guidelines
├── CODE_OF_CONDUCT.md             # Community standards
├── .gitignore                      # Git ignore rules
├── docs/                           # Documentation
│   ├── API.md                     # API documentation
│   └── ARCHITECTURE.md            # This file
├── static/                         # Static assets
│   ├── css/                       # Stylesheets
│   └── js/                        # JavaScript files
├── templates/                      # HTML templates
└── utils/                          # Backend utilities
    ├── __init__.py
    ├── db_handler.py
    ├── user_handler.py
    ├── stats_handler.py
    ├── map_handler.py
    ├── data_fetcher.py
    ├── alert_handler.py
    ├── simulation_handler.py
    └── traffic_light_handler.py
```
