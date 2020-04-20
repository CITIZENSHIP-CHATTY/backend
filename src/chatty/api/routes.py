from aiohttp import web

from chatty.api import api

api = [
    web.get('/api/ping', api.ping),
    web.get('/api/create_room', api.create_room)
]
