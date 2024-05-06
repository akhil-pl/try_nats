from nats.aio.client import Client as NATS
import asyncio

async def message_handler(msg):
    subject = msg.subject
    data = msg.data.decode()
    print(f"Microservice 1 received message on subject '{subject}': {data}")

async def run():
    nc = NATS()
    await nc.connect("nats://nats:4222")
    await nc.subscribe("subject1", cb=message_handler, queue="microservice1")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
    loop.run_forever()
