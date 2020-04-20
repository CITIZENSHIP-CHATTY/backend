import logging

from aiohttp import web
from aiohttp.web_response import json_response

from chatty.api.models import Room


async def ping(request):
    return web.json_response({'message': 'pong'}, status=200)


async def create_room(request):
    owner_id = request.user
    if not owner_id:
        return json_response({"message": 'You need to authorize'}, status=200)

    data = request.json()

    room = await Room.create(data)
    return json_response({'Created room id': data}, status=200)
