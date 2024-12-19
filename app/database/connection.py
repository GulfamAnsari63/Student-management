from pymongo import MongoClient

# MongoDB Atlas Configuration
MONGO_URI = "mongodb+srv://main_user63:107213208@cluster0.pbj2n.mongodb.net/student_management"
DATABASE_NAME = "student_management"

client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
