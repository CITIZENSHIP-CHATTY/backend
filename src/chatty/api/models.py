import logging
from datetime import datetime
from typing import List

from bson import ObjectId
from pydantic import BaseModel, Field

from chatty.auth.models import User
from chatty.db import collection


class Message(BaseModel):
    body: str
    owner: User
    created: datetime = Field(default_factory=datetime.utcnow)


class Room(BaseModel):
    name: str = Field(...)
    description: str = 'Default description'
    owner: User
    messages: List[Message] = None
    created: datetime = Field(default_factory=datetime.utcnow)

    @staticmethod
    async def get_by_id(room_id):
        pass

    @staticmethod
    async def create(data):
        await collection('rooms').insert_one(data)

    @staticmethod
    async def update(data):
        pass
