from flask import Flask, request, jsonify, send_from_directory, session, redirect
import sqlite3

app = Flask(__name__, static_folder=".", static_url_path="")
app.secret_key = "your_secret_key_here"  # Required for session management

def get_db_connection():
    conn = sqlite3.connect("db/recipes.db")
    conn.row_factory = sqlite3.Row
    return conn

# Protect homepage
@app.route("/")
def home():
    if "user" not in session:
        return redirect("/login.html")
    return send_from_directory(".", "index.html")


# Protect Add Recipe page
@app.route("/AddRecipe.html")
def add_recipe_page():
    if "user" not in session:
        return redirect("/login.html")
    return send_from_directory(".", "AddRecipe.html")

# Signup page (open)
@app.route("/signup.html")
def signup_page():
    return send_from_directory(".", "signup.html")


# Login page (open)
@app.route("/login.html")
def login_page():#
    if "user" in session:
        return redirect("/")
    return send_from_directory(".", "login.html")

@app.route("/check-login")
def check_login():
    return jsonify({"logged_in": "user" in session})



# Login logic
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM User WHERE Email = ? AND password = ?",
        (data["username"], data["password"])
    )
    user = cursor.fetchone()
    conn.close()

    if user:
        session["user"] = data["username"]
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"message": "Invalid credentials"}), 401

# Logout route
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login.html")

# Add new recipe
@app.route("/add-recipe", methods=["POST"])
def add_recipe():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Recipe 
        (Title, Instructions, Description, Prep_Time, Cook_Time, Servings, Created_By, Label)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data["name"],
        data["instructions"],
        data["ingredients"],
        data["prep"],
        data["cook"],
        data["servings"],
        session.get("user"),
        data["category"]
    ))
    conn.commit()
    conn.close()
    return jsonify({"message": "Recipe added successfully"})

# Add new user
@app.route("/sign-up", methods=["POST"])
def add_user():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO User (Email, password)
        VALUES (?, ?)
    """, (
        data["username"],
        data["password"],
    ))
    conn.commit()
    conn.close()
    return jsonify({"message": "User added successfully"})

# Get all recipes (protected)
@app.route("/recipes")
def get_recipes():
    if "user" not in session:
        return redirect("/login.html")
    conn = get_db_connection()
    rows = conn.execute("SELECT * FROM Recipe").fetchall()
    conn.close()
    return jsonify([dict(row) for row in rows])

if __name__ == "__main__":
    app.run(debug=True)
