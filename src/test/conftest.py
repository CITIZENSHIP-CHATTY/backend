import asyncio

import pytest

from chatty.main import create_app


@pytest.fixture
def loop():
    return asyncio.get_event_loop()


@pytest.fixture
async def client(aiohttp_client):
    return await aiohttp_client(create_app())
