from pymongo import MongoClient
from redis import Redis
from dotenv import load_dotenv
import os

load_dotenv("application.env")

client = MongoClient(os.getenv("MONGODB_DATASOURCE_URL"))
db = client[os.getenv("MONGODB_DATASOURCE_DATABASE")] 
r = Redis(host='localhost', port=6379, db=0)