import jwt
from aiohttp import web

from settings import SECRET_KEY


@web.middleware
async def auth_middleware(request, handler):
    request.user = None
    token = request.headers.get('Authorization', None)
    if token:
        try:
            payload = jwt.decode(token, SECRET_KEY)
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            return web.json_response({"message": "Credentials not correctly encoded."}, status=400)

        request.user = payload['_id']
    return await handler(request)
