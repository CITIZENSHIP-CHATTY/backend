import jwt
from aiohttp.web_response import json_response

from settings import SECRET_KEY


async def auth_middleware(app, handler):
    async def middleware(request):
        request.user = None
        token = request.headers.get('Authorization', None)
        if token:
            try:
                payload = jwt.decode(token, SECRET_KEY)
            except (jwt.DecodeError, jwt.ExpiredSignatureError):
                return json_response({"message": "Credentials not correctly encoded."}, status=400)

            request.user = payload['_id']

        return await handler(request)

    return middleware
