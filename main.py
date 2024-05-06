from fastapi import FastAPI, HTTPException
from nats.aio.client import Client as NATS
from nats.aio.errors import NatsError
# from nats.aio.utils import new_inbox
# import aiohttp
import asyncio

app = FastAPI()

async def setup_nats():
    nc = NATS()
    await nc.connect("nats://nats:4222")
    # Enable JetStream
    js = nc.jetstream()
    return nc, js


# Endpoint to publish a NATS message with a given subject
@app.get("/publish/subject1")
async def publish_message():
    try:
        nc, js = await setup_nats()
        await js.publish("subject1", b"Hello NATS!")
        return {"message": "Message published successfully"}
    except NatsError as e:
        raise HTTPException(status_code=500, detail=f"Failed to publish message: {e}")

# Endpoint to publish a NATS message with a subject and data
@app.get("/publish/subject2/{data}")
async def publish_message_with_data(data: str):
    try:
        nc, js = await setup_nats()
        await nc.publish('subject2', data.encode())
        print("message published")
        return {"message": "Message published successfully"}
    except NatsError as e:
        raise HTTPException(status_code=500, detail=f"Failed to publish message: {e}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
