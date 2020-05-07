from motor.motor_asyncio import AsyncIOMotorClient

DB = None
CLIENT = None
MONGODB_URL = "mongodb://chatty-db/"


def client():
    global CLIENT
    if CLIENT is None:
        CLIENT = AsyncIOMotorClient(MONGODB_URL)
    return CLIENT


def db():
    global DB
    if DB is None:
        DB = client()['chatty']
    return DB


def collection(coll_name):
    return db()[coll_name]
