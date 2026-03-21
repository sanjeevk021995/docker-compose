from fastapi import FastAPI
from app.cache import Cache
import time

app = FastAPI()


@app.get("/")
async def hello():
    return {"message": "Hello World 🚀"}


@app.get("/data")
async def get_data():
    cache_key = "sample_data"

    # Try cache
    cached = await Cache.get(cache_key)
    if cached:
        return {
            "source": "cache",
            "data": cached
        }

    # Simulate DB/API call
    data = {
        "value": "This is fresh data",
        "timestamp": time.time()
    }

    # Store in cache
    await Cache.set(cache_key, data, expire=30)

    return {
        "source": "db",
        "data": data
    }