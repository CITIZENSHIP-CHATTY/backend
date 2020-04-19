from aiohttp import web

from chatty import api

routes = [
    web.get('/api/ping', api.ping),
]
