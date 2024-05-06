from nats.aio.client import Client as NATS
import asyncio

async def message_handler(msg):
    subject = msg.subject
    data = msg.data.decode()
    print(f"Microservice 2 received message on subject '{subject}': {data}")

async def run():
    nc = NATS()
    await nc.connect("nats://nats:4222")
    await nc.subscribe("subject2", cb=message_handler)
    print(f"Listening for messages on subject 'your_subject'")
    # Keep the service running indefinitely
    await asyncio.Future()  # This never completes

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
    loop.close()
    loop.run_forever()
