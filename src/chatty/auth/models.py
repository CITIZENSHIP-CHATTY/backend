from pydantic import BaseModel

from chatty import utils
from chatty.db import collection


class User(BaseModel):
    username: str
    password: str

    @staticmethod
    async def get_by_username(username):
        return await collection('users').find_one({'username': username})

    @staticmethod
    async def create(data):
        password = await utils.encrypt_password(data['password'])
        data = {'username': data['username'], 'password': password}
        user = User(**data)

        await collection('users').insert_one(data)

        return user.username
