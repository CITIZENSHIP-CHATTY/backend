from chatty import utils
from aiohttp import web

from chatty.auth.models import User


async def registration(request):
    auth_data = await request.json()
    if not await utils.validation_credentials(auth_data):
        return web.json_response({"message": "Invalid credentials"}, status=400)

    await User.create(auth_data)
    return web.json_response({"message": "Registration successfully"}, status=200)


async def login(request):
    auth_data = await request.json()
    try:
        username = auth_data['username']
        password = auth_data['password']
    except KeyError:
        return web.json_response({"message": "Username or password were not provided"}, status=400)

    user = await User.get_by_username(username)
    if not user:
        return web.json_response({"message": "User with such name does not exists"}, status=400)

    if not await utils.check_password(password, user['password']):
        return web.json_response({'message': "Password incorrect"})

    token = await utils.generate_jwt_token(user)

    return web.json_response({"token": token}, status=200)
