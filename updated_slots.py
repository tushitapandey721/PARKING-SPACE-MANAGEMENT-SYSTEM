from pymongo import MongoClient

# Connect to your MongoDB
client = MongoClient("mongodb+srv://tush61270:TushitaP@cluster0.o2pxr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["parkingDB"]
slots_col = db["slots"]

# Add 'vehicle_number' field if not already present
result = slots_col.update_many(
    {"vehicle_number": {"$exists": False}},
    {"$set": {"vehicle_number": ""}}
)

print(f"Updated {result.modified_count} documents.")
