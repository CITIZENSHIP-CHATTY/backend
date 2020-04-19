from aiohttp import web

from auth import views

authrouters = [
    web.post('/api/auth/registration', views.registration),
    web.post('/api/auth/login', views.login),
]
