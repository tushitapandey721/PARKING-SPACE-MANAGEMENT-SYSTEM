from pymongo import MongoClient
from datetime import datetime

# Connect to MongoDB Atlas
client = MongoClient("mongodb+srv://tush61270:TushitaP@cluster0.o2pxr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["parkingDB"]

# Collections
users_col = db["users"]
slots_col = db["slots"]

# Clear existing data (optional)
users_col.delete_many({})
slots_col.delete_many({})

# Sample users
users = [
    {"username": "admin", "password": "admin123", "role": "admin"},
    {"username": "user1", "password": "pass1", "role": "user"},
    {"username": "user2", "password": "pass2", "role": "user"}
]

# Sample parking slots
slots = [
    {"slot_number": f"A{i+1}", "status": "available", "booked_by": "", "timestamp": None}
    for i in range(10)
]

# Insert data
users_col.insert_many(users)
slots_col.insert_many(slots)

print("Sample users and slots inserted successfully.")
