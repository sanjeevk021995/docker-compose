import redis.asyncio as redis
import json
import os

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = 6379

redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)


class Cache:
    @staticmethod
    async def get(key: str):
        data = await redis_client.get(key)
        if data:
            return json.loads(data)
        return None

    @staticmethod
    async def set(key: str, value, expire: int = 60):
        await redis_client.set(key, json.dumps(value), ex=expire)

    @staticmethod
    async def delete(key: str):
        await redis_client.delete(key)