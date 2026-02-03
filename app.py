#
# app.py
#
# Eric Chhun
# 10/16/2025
# Main Flask application for the Traffic & Accident Data Monitor system.
# This app visualizes real-time traffic and accident data, user analytics,
# and interactive traffic simulations.
# It connects to backend utilities for fetching live data, managing databases,
# generating charts, and controlling animations. Each route corresponds to a
# key feature page within the website’s design (Home, Map, Analytics, Simulation, Emergency).
# 


"""
app.py
----------------------------------------
Main Flask application for Traffic & Accident Data Monitor.

pusodo-code:
    create a login system with user authentication
    create routes for homepaage, login, register, forgot password, logout
    Create API endpoints for user data retrieveal and traffic statistics
    handle errors and sessions appropriately by using exception handling
    end file

Handles:
- User authentication (login, register, forgot password)
- Home/dashboard rendering
- Session management
- API endpoints for user data retrieveal 
- error handling
- Functions:
    - index()
    - login()
    - register()
    - forgot_password()
    - logout()
    - get_user()
"""

from flask import Flask, jsonify, request, session, render_template, url_for, redirect

from utils.db_handler import init_db, get_all_traffic_data
from utils.stats_handler import overall_summary, summarize_city_traffic
from utils.alert_handler import generate_alerts
from utils.user_handler import register_user, login_user, get_user_by_email, logout_user, reset_password
from utils.map_handler import prepare_map_data
from utils.simulation_handler import run_simulation_step
from utils.traffic_light_handler import get_intersection_state
from utils.stats_handler import summarize_city_traffic, summarize_accidents, overall_summary
import os

# set up the Flask app 
app = Flask(__name__, static_folder='static', template_folder='templates')
# Set secret key for session management
app.secret_key = os.environ.get("SECRET_KEY", "supersecretkey") 


# Initialize database
try: # handle any init errors
    init_db() # initialize DB tables
    print("[INFO] Database initialized successfully.")
except Exception as e: # catch errors and log
    # print error message
    print(f"[ERROR] Database init failed: {e}")


# user authentication route
@app.route("/register", methods=["GET", "POST"])
# A function to handle user registration
def register():
    """Registers a new user."""
    """ Handles user registration requests from both GET and POST methods"""
    if request.method == "POST":
        username = request.form["username"]
        email = request.form.get("email", " ")
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]
        
        if password != confirm_password:
            return render_template("register.html", error="Passwords do not match")
        
        result = register_user(username, email, password)
        print("registration result:", result)
        
        if result["status"] == "success":
            return redirect(url_for("login"))
        else:
            # show error message on registration page
            return render_template("register.html", error=result["message"])
    return render_template("register.html")
   

# authentication route for user login 
@app.route("/login", methods=["GET", "POST"])
# A function to handle user login 
def login():
    """Logs a user in and starts a session."""
    """ Handles user login requests from both GET and POST methods """
    # if POST request, process login from data
    if request.method == "POST":
        # get username and password from form data
        username = request.form["username"]
        password = request.form["password"]
        # call login_user function to authenticate and store in result variable
        result = login_user(username, password)
        # if login successful, store user in session and render homepage
        if result["status"] == "success":
            session["user"] = username
            # render homepage with welcome message
            return render_template("index.html", username=username, message="Login successful!")
        else:
            # on failure, show error message on login page
            return render_template("login.html", error=result["message"])
    # for GET request, just render the index page 
    return render_template("login.html")
    

# route for user logout
@app.route("/logout", methods=["POST"])
# A function to handle user logout
def logout():
    """Logs out the current user."""
    # call logout_user function to clear session data
    logout_user(session)
    return redirect(url_for("login"))
   

# Route for password recovery
@app.route("/forgot_password", methods=["GET", "POST"])
# A function to handle password recovery requests
def forgot_password():
    """ handles password recovery requests """
    # if POST request, process password reset form data 
    if request.method == "POST":
        # get email from form data
        email = request.form["email"]
        # call reset_password function to handle password reset
        result = reset_password(email)
        # test result and show appropriate message
        print("password reset result:", result)
        # return message on the forgot password page
        return render_template("forgot_password.html", message=result["message"])
    # for GET request, just render the forgot password page
    return render_template("forgot_password.html")
    
    
# route for traffic map
@app.route("/map", methods=["GET"])
def map_view():
    return render_template("map.html")

    
# route for fetching traffic map data (API)
@app.route("/api/map_data", methods=["GET"])
def api_map_data():
    """ Returns structured traffic data for map. """
    try:
        city_filter = request.args.get("city", None)
        # fetch traffic data from map_handler.py
        map_data = prepare_map_data(city_filter)
        
        # return JSON resonse to frontend
        return jsonify ( {
            "success": True,
            "count": len(map_data),
            "data": map_data
        }), 200
    except Exception as e:
        # print an error message to the console
        print(f"Error: Map data retrieval failed: {e} ")
        return jsonify ({
            "success": False,
            "error": str(e),
            "message": "Failed to load map data."
        }), 500


@app.route('/traffic_data', methods=['GET'])
def traffic_data():
    query = request.args.get('query', '').strip()
    
    if query:
        city_summary = summarize_city_traffic(query)
        accident_summary = summarize_accidents(7) # last 7 days
        overall = overall_summary()
        
        return render_template("traffic_data.html",
            query=query,
            city_summary=city_summary,
            accident_summary=accident_summary,
            overall=overall
        )
    else:
        # show the global summary if no city search
        overall = overall_summary()
        return render_template(
             "traffic_data.html",
            query=None,
            city_summary=None,
            accident_summary=None,
            overall=overall
        )

  
  

# A route to get current logged-in user info
@app.route("/api/user", methods=["GET"])
# a function to get current user infomation
def get_current_user():
    """Gets the logged-in user's information."""
    # if user is logged in session, return their username
    if "user" in session:
        return jsonify({"logged_in": True, "username": session["user"]})
    # else return not logged in message
    return jsonify({"logged_in": False, "message": "No active user session."})

# route for overall traffic & accident statistics
@app.route("/api/stats/overall", methods=["GET"])
# A function to get overall traffic & accident statistics of the system
def get_overall_stats():
    """Returns overall traffic & accident statistics."""
    # get excetion handling for any errors
    try:
        # call overall_summary function from stats_handler.py file
        stats = overall_summary()
        # if no stats found, return 404 error message
        if not stats:
            # get the not found message as JSON response
            return jsonify({"success": False, "message": "No traffic data found."}), 404
        return jsonify({"success": True, "data": stats}), 200
    # catch any exceptions and return '500' error message
    except Exception as e:
        # return error message as JSON response
        return jsonify({"success": False, "error": str(e)}), 500

# route for city-specific traffic statistics
@app.route("/api/stats/city/<city>", methods=["GET"])
# A function to get traffic statistics for a specific city
def get_city_stats(city):
    """Returns traffic statistics for a specific city."""
    # handle exceptions for any errors in processing
    try:
        # call summarize_city_traffic function from stats_handler.py file and store 
        # it in stats variable
        stats = summarize_city_traffic(city)
        # if no stats found for the city, return '404' error message
        if not stats:
            return jsonify({"success": False, "message": f"No data found for {city}."}), 404
        return jsonify({"success": True, "data": stats}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


# route for accident info page
@app.route("/accident_info", methods=["GET"])
# A function to render the Accident History & Trends page
def accident_info():
    """Displays the Accident History & Trends page."""
    return render_template("accident_info.html")
    

car_positions = [0, 150, 300] # initial car positions

# route for traffic simulation page
@app.route("/simulation")
# A function to render the Traffic Simulation page
def run_simulation():
    """ Renders the Traffic Simulation page"""
    global car_positions
    state = run_simulation_step(car_positions)
    car_positions = state["car_positions"]
    return jsonify(state)
    
@app.route("/traffic_simulation")
def traffic_simulation():
    return render_template("traffic_simulation.html")


@app.route("/traffic_light")
def traffic_light():
    return render_template("traffic_light.html")

@app.route("/stop_sign_simulation")
def stop_sign_simulation():
    return render_template("stop_sign_simulation.html")
    
@app.route("/api/traffic_light_state")
def traffic_light_state():
    """ Returns current traffic light state at intersection """
    return jsonify(get_intersection_state())



# route for getting live alerts and notifications
@app.route("/api/alerts", methods=["GET"])
# A function to get live alerts for traffic congestion or accident spikes
def get_alerts():
    """Returns live alerts for traffic congestion or accident spikes."""
    try:
        # call generate_alerts function and store results in alerts variable
        alerts = generate_alerts()
        # return alerts as JSON response
        return jsonify({"success": True, "alerts": alerts}), 200
    # catch any exceptions and return '500' error message
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


# A route for health check of the API and database
@app.route("/api/health", methods=["GET"])
# A function to check the health of the API and database connection
def health_check():
    """Checks whether the database and API are functioning correctly."""
    try:
        # try to fetch some data from the database and store in data variable
        data = get_all_traffic_data()
        # if successful, return healthy status as JSON response
        return jsonify({
            "status": "healthy",
            "records_in_db": len(data),
            "message": "API and Database are operational "
        }), 200
    # catch any exceptions and return '500' error message and unhealthy status
    except Exception as e:
        # return unhealthy status as JSON response
        return jsonify({
            "status": "error",
            "message": f"Health check failed: {e}"
        }), 500

# route for handling 404 errors 
@app.errorhandler(404)
# A function to handle 404 Not Found errors 
def page_not_found(e):
    """Custom 404 Not Found page."""
    # return custom JSON response for 404 errors
    return jsonify({
        "success": False, # indicate failure
        "error": 404, # error code 
        "message": "The requested page or route was not found."
    }), 404

# route for handling 500 internal server errors
@app.errorhandler(500)
# A function to handle 500 and handle server errors
def server_error(e):
    """Custom 500 Internal Server Error page."""
    return jsonify({
        "success": False,
        "error": 500,
        "message": "An internal server error occurred. Please try again later."
    }), 500

# root route for homepage rendering
@app.route("/", methods=["GET"])
# A function to render the homepage 
def home():
    """Render the homepage as the default route."""
    username = session.get("user", "Guest")
    return render_template("index.html", username=username)

# root route for basic API status check
@app.route("/api", methods=["GET"])
def map_info():
    """Root API route."""
    return jsonify({
        "status": "online",
        "message": "Welcome to the Traffic & Accident Data Monitor API 🚦",
        "available_routes": {
            "auth": {
                "register": "/api/register",
                "login": "/api/login",
                "logout": "/api/logout",
                "forgot_password": "/api/forgot-password",
                "get_user": "/api/user"
            },
            "traffic": {
                "overall_stats": "/api/stats/overall",
                "city_stats": "/api/stats/city/<city>"
            },
            "alerts": "/api/alerts",
            "health": "/api/health"
        }
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(" Starting Traffic & Accident Data Monitor Server...")
    print(f" Running on: http://127.0.0.1:{port}")

    app.run(host="0.0.0.0", port=5002, debug=True)
