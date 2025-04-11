🚗 Parking Space Management System

A smart and user-friendly web application for managing parking spaces efficiently using Flask and MongoDB. This system allows users to register, log in, book parking slots for a limited time, and gives admins full control to monitor and manage parking activities.

---

## 📌 Features

- 🧾 **User Registration & Login** (with role-based access)
- 📋 **Admin Dashboard**
  - View all parking slots
  - Reset/release slots
  - Monitor bookings
- 🧍‍♂️ **User Dashboard**
  - View available (🟩) and occupied (🟥) slots
  - Book a parking slot (only one per user)
  - Provide name and vehicle number during booking
- ⏱️ **Auto Release Mechanism**
  - Slot booking expires after 1 hour automatically
- 🎨 **Futuristic Frontend Design**
  - Responsive and visually clean UI using HTML, CSS, and JavaScript
- 🔐 **Secure Authentication** using Flask-Login

---

## 🛠️ Tech Stack

| Layer       | Technology                  |
|-------------|-----------------------------|
| Backend     | Python, Flask, Flask-Login, Flask-CORS |
| Database    | MongoDB                     |
| Frontend    | HTML, CSS, JavaScript       |
| Deployment  | (Optional) Render / Heroku / Localhost |

---

## 📁 Project Structure

PARKING-SPACE-MANAGEMENT-SYSTEM/ ├── static/ │ └── (CSS, JS files) ├── templates/ │ ├── login.html │ ├── admin_dashboard.html │ ├── user_dashboard.html │ ├── home.html │ ├── slots.html │ └── admin.html ├── app.py ├── requirements.txt └── README.md

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/tushitapandey721/PARKING-SPACE-MANAGEMENT-SYSTEM.git
cd PARKING-SPACE-MANAGEMENT-SYSTEM
2. Create and Activate Virtual Environment (Optional but recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Setup MongoDB
Ensure MongoDB is running locally or use a MongoDB Atlas URI.

Update your app.py MongoDB URI with your credentials:

python
Copy
Edit
client = MongoClient("mongodb://localhost:27017/")  # or your MongoDB Atlas URI
5. Run the App
bash
Copy
Edit
python app.py
Then open your browser at: http://127.0.0.1:5000

🧪 Testing
Register a user and try booking a slot.

Log in as admin to reset slots.

Wait for 1 hour or simulate expiry to test auto-release.

🔐 Default Admin Login (if hardcoded or pre-initialized)
txt
Copy
Edit
Username: admin
Password: admin123
You can also register new users and assign them admin role via the database.


🚀 Future Enhancements
Email notifications on booking

QR code-based slot access

Real-time updates with WebSockets

Mobile app version

📄 License
This project is open-source and available under the MIT License.

🙋‍♀️ Author
Tushita Pandey
