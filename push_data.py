from pymongo import MongoClient
import certifi
from urllib.parse import quote_plus

username = "AshikHasanRedoy"
password = "Ashik@12345"
encoded_password = quote_plus(password)

uri = f"mongodb+srv://{username}:{encoded_password}@cluster0.ncgxgid.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(
    uri,
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=10000
)

try:
    client.admin.command("ping")
    print("✅ Successfully connected to MongoDB!")
except Exception as e:
    print("❌ Connection error:", e)