import hashlib
import os

from datetime import datetime, timedelta

import jwt

from chatty import db


async def validation_credentials(data: dict) -> bool:
    try:
        username = data['username']
        password = data['password']
        password_confirm = data['password_confirm']
    except KeyError:
        return False

    user = await db.collection('users').find_one({'username': username})
    if user:
        return False

    if password != password_confirm or len(password) < 8:
        return False

    return True


async def encrypt_password(password: str) -> str:
    salt = password.encode() + os.environ['SECRET'].encode()
    return hashlib.sha512(salt).hexdigest()


async def check_password(password: str, password_hash: str) -> bool:
    return await encrypt_password(password) == password_hash


async def generate_jwt_token(data) -> str:
    duration = datetime.now() + timedelta(days=os.environ['JWT_DAYS'])

    token = jwt.encode(
        {
            '_id': str(data['_id']),
            'duration': int(duration.strftime('%s'))
        }, os.environ['SECRET']
    )
    return token.decode('UTF-8')
