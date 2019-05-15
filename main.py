import aiohttp
import asyncio
import ujson
timeout = aiohttp.ClientTimeout(total=360)


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def get_data():
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.get('https://whattomine.com/coins/1.json') as btc:
            result_btc = await btc.json()
        async with session.get('https://whattomine.com/coins/162.json') as ethc:
            result_ethc = await ethc.json()
        async with session.get('https://whattomine.com/coins/151.json') as eth:
            result_eth = await eth.json()
        async with session.get('https://whattomine.com/coins/173.json') as ubq:
            result_ubq = await ubq.json()
        async with session.get('https://whattomine.com/coins/293.json') as grin:
            result_grin = await grin.json()
        async with session.get('https://whattomine.com/coins/4.json') as ltc:
            result_ltc = await ltc.json()
        async with session.get('https://whattomine.com/coins/34.json') as dash:
            result_dash = await dash.json()

        new_dict = {
            "btc": {
                "block_time": result_btc["block_time"],
                "difficulty24": result_btc["difficulty24"],
                "block_reward": result_btc["block_reward"],
                "last_block": result_btc["last_block"],
                "difficulty": result_btc["difficulty"],
                "nethash": result_btc["nethash"],
                "exchange_rate": result_btc["exchange_rate"],
                "exchange_rate_vol": result_btc["exchange_rate_vol"],
                "exchange_rate_curr": result_btc["exchange_rate_curr"],
                "market_cap": result_btc["market_cap"],
                "estimated_rewards": result_btc["estimated_rewards"],
                "btc_revenue": result_btc["btc_revenue"],
                "revenue": result_btc["revenue"],
                "cost": result_btc["cost"],
                "profit": result_btc["profit"]
            },
            "ethc": {
                "block_time": result_ethc["block_time"],
                "difficulty24": result_ethc["difficulty24"],
                "block_reward": result_ethc["block_reward"],
                "last_block": result_ethc["last_block"],
                "difficulty": result_ethc["difficulty"],
                "nethash": result_ethc["nethash"],
                "exchange_rate": result_ethc["exchange_rate"],
                "exchange_rate_vol": result_ethc["exchange_rate_vol"],
                "exchange_rate_curr": result_ethc["exchange_rate_curr"],
                "market_cap": result_ethc["market_cap"],
                "estimated_rewards": result_ethc["estimated_rewards"],
                "btc_revenue": result_ethc["btc_revenue"],
                "revenue": result_ethc["revenue"],
                "cost": result_ethc["cost"],
                "profit": result_ethc["profit"]
            },
            "eth": {
                "block_time": result_eth["block_time"],
                "difficulty24": result_eth["difficulty24"],
                "block_reward": result_eth["block_reward"],
                "last_block": result_eth["last_block"],
                "difficulty": result_eth["difficulty"],
                "nethash": result_eth["nethash"],
                "exchange_rate": result_eth["exchange_rate"],
                "exchange_rate_vol": result_eth["exchange_rate_vol"],
                "exchange_rate_curr": result_eth["exchange_rate_curr"],
                "market_cap": result_eth["market_cap"],
                "estimated_rewards": result_eth["estimated_rewards"],
                "btc_revenue": result_eth["btc_revenue"],
                "revenue": result_eth["revenue"],
                "cost": result_eth["cost"],
                "profit": result_eth["profit"]
            },
            "ubq": {
                "block_time": result_ubq["block_time"],
                "difficulty24": result_ubq["difficulty24"],
                "block_reward": result_ubq["block_reward"],
                "last_block": result_ubq["last_block"],
                "difficulty": result_ubq["difficulty"],
                "nethash": result_ubq["nethash"],
                "exchange_rate": result_ubq["exchange_rate"],
                "exchange_rate_vol": result_ubq["exchange_rate_vol"],
                "exchange_rate_curr": result_ubq["exchange_rate_curr"],
                "market_cap": result_ubq["market_cap"],
                "estimated_rewards": result_ubq["estimated_rewards"],
                "btc_revenue": result_ubq["btc_revenue"],
                "revenue": result_ubq["revenue"],
                "cost": result_ubq["cost"],
                "profit": result_ubq["profit"]
            },
            "grin": {
                "block_time": result_grin["block_time"],
                "difficulty24": result_grin["difficulty24"],
                "block_reward": result_grin["block_reward"],
                "last_block": result_grin["last_block"],
                "difficulty": result_grin["difficulty"],
                "nethash": result_grin["nethash"],
                "exchange_rate": result_grin["exchange_rate"],
                "exchange_rate_vol": result_grin["exchange_rate_vol"],
                "exchange_rate_curr": result_grin["exchange_rate_curr"],
                "market_cap": result_grin["market_cap"],
                "estimated_rewards": result_grin["estimated_rewards"],
                "btc_revenue": result_grin["btc_revenue"],
                "revenue": result_grin["revenue"],
                "cost": result_grin["cost"],
                "profit": result_grin["profit"]
            },
            "ltc": {
                "block_time": result_ltc["block_time"],
                "difficulty24": result_ltc["difficulty24"],
                "block_reward": result_ltc["block_reward"],
                "last_block": result_ltc["last_block"],
                "difficulty": result_ltc["difficulty"],
                "nethash": result_ltc["nethash"],
                "exchange_rate": result_ltc["exchange_rate"],
                "exchange_rate_vol": result_ltc["exchange_rate_vol"],
                "exchange_rate_curr": result_ltc["exchange_rate_curr"],
                "market_cap": result_ltc["market_cap"],
                "estimated_rewards": result_ltc["estimated_rewards"],
                "btc_revenue": result_ltc["btc_revenue"],
                "revenue": result_ltc["revenue"],
                "cost": result_ltc["cost"],
                "profit": result_ltc["profit"]
            },
            "dash": {
                "block_time": result_dash["block_time"],
                "difficulty24": result_dash["difficulty24"],
                "block_reward": result_dash["block_reward"],
                "last_block": result_dash["last_block"],
                "difficulty": result_dash["difficulty"],
                "nethash": result_dash["nethash"],
                "exchange_rate": result_dash["exchange_rate"],
                "exchange_rate_vol": result_dash["exchange_rate_vol"],
                "exchange_rate_curr": result_dash["exchange_rate_curr"],
                "market_cap": result_dash["market_cap"],
                "estimated_rewards": result_dash["estimated_rewards"],
                "btc_revenue": result_dash["btc_revenue"],
                "revenue": result_dash["revenue"],
                "cost": result_dash["cost"],
                "profit": result_dash["profit"]
            },
                    }
    return new_dict


def main():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(get_data())
    print(result)


if __name__ == '__main__':
    main()