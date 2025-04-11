from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from flask_cors import CORS
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from datetime import datetime
from bson.objectid import ObjectId
import utils
from flask import session

app = Flask(__name__)
app.secret_key = 'supersecretkey'
CORS(app)

# MongoDB Setup
client = MongoClient("mongodb+srv://tush61270:TushitaP@cluster0.o2pxr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["parkingDB"]
users_col = db["users"]
slots_col = db["slots"]

# Insert 5 slots only if none exist
if slots_col.count_documents({}) == 0:
    slots_col.insert_many([
        {
            "status": "available",
            "booked_by": "",
            "vehicle_number": "",
            "timestamp": None
        } for _ in range(5)
    ])

# Flask-Login Setup
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, user_doc):
        self.id = str(user_doc["_id"])
        self.username = user_doc["username"]
        self.role = user_doc["role"]

@login_manager.user_loader
def load_user(user_id):
    user_doc = users_col.find_one({"_id": ObjectId(user_id)})
    return User(user_doc) if user_doc else None

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        user = users_col.find_one({"username": username, "password": password})
        if user:
            login_user(User(user))
            return redirect(url_for('dashboard'))
        return "<h3 style='color:red; text-align:center;'>Invalid credentials.</h3><p style='text-align:center;'><a href='/login'>Try Again</a></p>"
    
    return render_template("login.html")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    utils.auto_release_expired_slots()
    slots = list(slots_col.find())
    message = session.pop('success_message', None)  # Retrieve and remove message

    if current_user.role == 'admin':
        return render_template('admin.html', slots=slots)
    else:
        return render_template('slots.html', slots=slots, message=message)


@app.route('/book/<slot_id>', methods=['POST'])
@login_required
def book_slot(slot_id):
    name = request.form['name'].strip()
    vehicle_number = request.form['vehicle_number'].strip()

    # Prevent duplicate bookings by same user or same vehicle
    existing = slots_col.find_one({
        "status": "occupied",
        "$or": [
            {"booked_by": name},
            {"vehicle_number": vehicle_number}
        ]
    })

    if existing:
        return "<h3 style='color:red; text-align:center;'>You or this vehicle already have a booked slot.</h3><p style='text-align:center;'><a href='/dashboard'>Back to Dashboard</a></p>"

    slot = slots_col.find_one({"_id": ObjectId(slot_id)})
    if slot["status"] == "available":
        slots_col.update_one(
            {"_id": ObjectId(slot_id)},
            {"$set": {
                "status": "occupied",
                "booked_by": name,
                "vehicle_number": vehicle_number,
                "timestamp": datetime.utcnow()
            }}
        )
        session['success_message'] = "Successfully booked slot!"

    return redirect(url_for('dashboard'))


@app.route('/reset/<slot_id>')
@login_required
def reset_slot(slot_id):
    if current_user.role == "admin":
        slots_col.update_one(
            {"_id": ObjectId(slot_id)},
            {"$set": {
                "status": "available",
                "booked_by": "",
                "vehicle_number": "",
                "timestamp": None
            }}
        )
    return redirect(url_for('dashboard'))

@app.route('/reset_all')
@login_required
def reset_all_slots():
    if current_user.role == "admin":
        slots_col.update_many(
            {},
            {"$set": {
                "status": "available",
                "booked_by": "",
                "vehicle_number": "",
                "timestamp": None
            }}
        )
    return redirect(url_for('dashboard'))

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username'].strip()
    password = request.form['password']
    role = 'user'

    if users_col.find_one({"username": username}):
        return "<h3 style='color:red; text-align:center;'>User already exists. Please log in.</h3><p style='text-align:center;'><a href='/login'>Go to Login</a></p>"

    users_col.insert_one({
        'username': username,
        'password': password,
        'role': role
    })
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
