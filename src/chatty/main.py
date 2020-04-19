import logging
import os

from aiohttp import web

from auth.middleware import auth_middleware
from auth.routes import authrouters
from chatty.routes import routes


def create_app():
    app = web.Application(
        middlewares=[auth_middleware]
    )
    app.add_routes(routes)
    app.add_routes(authrouters)
    return app


if __name__ == "__main__":
    logging.basicConfig(level=os.getenv('LOGGING_LEVEL', 'INFO'))
    web.run_app(create_app())
