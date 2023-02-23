import asyncio
import aiohttp
import os
from web3 import Web3

ALCHEMY_BASE_URL = "https://eth-mainnet.g.alchemy.com/v2/"

async def get_block_data(block_no:str = "latest"):
    api_key = os.environ["ALCHEMY_API_KEY"]
    url = ALCHEMY_BASE_URL + api_key
    payload = {
        "id": 1,
        "jsonrpc": "2.0",
        "method": "eth_getBlockByNumber",
        "params": ['0x1b4', True]
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload, headers=headers) as resp:
            print(await resp.text())

    # w3 = Web3(Web3.HTTPProvider(url))

    # print(w3.eth.get_block(block_no))




async def main():
    await get_block_data()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())