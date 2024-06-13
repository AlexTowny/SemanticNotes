from fastapi import FastAPI
import pymongo
import os

app = FastAPI()
db_url = os.environ['MONGODB_URL']

@app.on_event("startup")
def startup_db_connection():
    app.mongodb_client = pymongo.MongoClient(db_url)
    




@app.get("/")
async def root():
    db = app.mongodb_client["storage"]
    notes = db['notes']
    d = len(db.list_collection_names())
    return {"message": "Hello World",
            "db":os.environ['MONGODB_URL'],
            "notes-count":d}