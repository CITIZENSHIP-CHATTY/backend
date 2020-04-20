from motor.motor_asyncio import AsyncIOMotorClient

from settings import MONGODB_URL

DB = None
CLIENT = None


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
