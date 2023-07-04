from motor.motor_asyncio import AsyncIOMotorClient


async def get_db():
    client = AsyncIOMotorClient("mongodb://academia:academia@localhost:27017")
    return client.academia
