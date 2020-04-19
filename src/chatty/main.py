import logging
import os

from aiohttp import web

from chatty.middlewares import auth_middleware
from chatty.api.routes import api
from chatty.auth.routes import auth


def create_app():
    app = web.Application(
        middlewares=[
            auth_middleware
        ]
    )
    app.add_routes(auth)
    app.add_routes(api)
    return app


if __name__ == "__main__":
    logging.basicConfig(level=os.getenv('LOGGING_LEVEL', 'INFO'))
    web.run_app(create_app())
