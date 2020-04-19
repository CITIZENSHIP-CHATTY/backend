from aiohttp import web


async def ping(request):
    return web.json_response({'message': 'pong'}, status=200)
