import jwt
import os

from aiohttp import web


@web.middleware
async def auth_middleware(request, handler):
    request.user = None
    token = request.headers.get('Authorization', None)
    if token:
        try:
            payload = jwt.decode(token, os.environ['SECRET'])
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            return web.json_response({"message": "Credentials not correctly encoded."}, status=400)

        request.user = payload['_id']
    return await handler(request)
