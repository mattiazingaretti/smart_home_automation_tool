import asyncio
from client import MCPClient
import os
from dotenv import load_dotenv

load_dotenv()  

async def main():

    client = MCPClient()
    try:
        await client.connect_to_server(os.getenv("MCP_SERVER_URL"))
        await client.chat_loop()
    finally:
        await client.cleanup()
        await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())