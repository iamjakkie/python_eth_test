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
        "params": [block_no, False]
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload, headers=headers) as resp:
            resp_json = await resp.json()
            res = resp_json["result"]
            print(res["gasLimit"])
            print(res["gasUsed"])
            print(res["number"])
            print(res["difficulty"])
            print(res["totalDifficulty"])


async def get_signature(provider: str, signature: str):
    url = provider+signature

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            resp_json = await resp.json()
            print(resp_json)



async def main():
    await get_block_data()

    provider_4byte = "https://www.4byte.directory/api/v1/signatures/?text_signature="
    await get_signature(provider_4byte, "balanceOf()")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())