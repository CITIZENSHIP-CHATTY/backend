from motor.motor_asyncio import AsyncIOMotorClient

from chatty import utils
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


async def create_user(data):
    await collection('users').insert_one({
        'username': data['username'],
        'password': await utils.encrypt_password(data['password']),
    })
