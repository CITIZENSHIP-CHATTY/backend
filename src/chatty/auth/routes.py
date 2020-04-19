from aiohttp import web


from chatty.auth import auth


auth = [
    web.post('/api/auth/registration', auth.registration),
    web.post('/api/auth/login', auth.login),
]
