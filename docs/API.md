# API Documentation

This document provides detailed information about the API endpoints available in the Traffic Accident Data Monitor application.

## Authentication Endpoints

### User Registration
- **URL:** `/register`
- **Method:** `GET`, `POST`
- **Description:** Handles user registration
- **POST Parameters:**
  - `username` (string, required): User's chosen username
  - `email` (string, required): User's email address
  - `password` (string, required): User's password
  - `confirm_password` (string, required): Password confirmation
- **Success Response:**
  - Redirects to `/login` on successful registration
- **Error Response:**
  - Returns registration page with error message

### User Login
- **URL:** `/login`
- **Method:** `GET`, `POST`
- **Description:** Authenticates a user and creates a session
- **POST Parameters:**
  - `email` (string, required): User's email address
  - `password` (string, required): User's password
- **Success Response:**
  - Redirects to homepage with active session
- **Error Response:**
  - Returns login page with error message

### Forgot Password
- **URL:** `/forgot_password`
- **Method:** `GET`, `POST`
- **Description:** Handles password reset requests
- **POST Parameters:**
  - `email` (string, required): User's email address
- **Success Response:**
  - Returns success message
- **Error Response:**
  - Returns error message

### Logout
- **URL:** `/logout`
- **Method:** `GET`
- **Description:** Logs out the current user and ends session
- **Success Response:**
  - Redirects to homepage

## Application Pages

### Homepage
- **URL:** `/`
- **Method:** `GET`
- **Description:** Displays the main landing page
- **Authentication:** Not required

### Traffic Map
- **URL:** `/map`
- **Method:** `GET`
- **Description:** Interactive map displaying real-time traffic data with markers
- **Authentication:** Recommended for full access

### Accident Information
- **URL:** `/accident_info`
- **Method:** `GET`
- **Description:** Displays detailed accident information and statistics
- **Authentication:** Recommended

### Traffic Data Dashboard
- **URL:** `/traffic_data`
- **Method:** `GET`
- **Description:** Comprehensive traffic statistics and analytics dashboard
- **Authentication:** Recommended

### Traffic Simulation
- **URL:** `/traffic_simulation`
- **Method:** `GET`
- **Description:** Interactive traffic merging simulation
- **Authentication:** Not required

### Traffic Light Simulator
- **URL:** `/traffic_light`
- **Method:** `GET`
- **Description:** Interactive traffic light control simulation
- **Authentication:** Not required

## API Endpoints

### Get User Data
- **URL:** `/api/user`
- **Method:** `GET`
- **Description:** Retrieves current logged-in user information
- **Authentication:** Required (session-based)
- **Success Response:**
  ```json
  {
    "username": "john_doe",
    "email": "john@example.com"
  }
  ```
- **Error Response:**
  ```json
  {
    "error": "User not logged in"
  }
  ```

## Error Handling

All endpoints implement proper error handling and will return appropriate HTTP status codes:

- `200 OK` - Successful request
- `400 Bad Request` - Invalid parameters
- `401 Unauthorized` - Authentication required
- `404 Not Found` - Endpoint not found
- `500 Internal Server Error` - Server error

## Session Management

The application uses Flask sessions for user authentication. Sessions are created upon successful login and destroyed upon logout. The session includes:

- User ID
- Username
- Login timestamp

## Security Considerations

- All passwords are hashed before storage
- Sessions use secure secret keys
- CSRF protection should be implemented for production
- Use HTTPS in production environments
