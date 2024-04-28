from .params import USER_NAME, PASSWORD, DB
from pymongo import MongoClient


db_url = f"mongodb+srv://{USER_NAME}:{PASSWORD}@{DB}.w85pkzq.mongodb.net/?retryWrites=true&w=majority&appName=library"

client = MongoClient(db_url)

db = client[DB]



