''' Task Module Description '''
from masonite.scheduler.Task import Task
import app.helpers.utilities as utilities
from masonite import env
from web3 import Web3
import simplejson as json
from decimal import *
import requests
import boto3
from datetime import datetime, timezone
from bs4 import BeautifulSoup
from hyper.contrib import HTTP20Adapter
from requests_html import HTMLSession, AsyncHTMLSession
import asyncio

class StatsJob(Task):
    ''' Task description '''

    run_every = '1 minute'

    def handle(self):

        print("TEST")
        w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))

        safegalaxy_addr, safegalaxy_abi = utilities.get_safegalaxy_auth()
        pancake_swap_addr, pancake_swap_abi = utilities.get_pancake_swap_auth()
        wbnb = utilities.get_wrapped_bnb_addr()
        busd = utilities.get_binance_usd_addr()

        # setup client for requests
        pancake_router = w3.eth.contract(pancake_swap_addr, abi=pancake_swap_abi)

        wbnb_to_busd = pancake_router.functions.getAmountsOut(1, [wbnb, busd]).call()
        wbnb_to_safe = pancake_router.functions.getAmountsOut(1000000000, [wbnb, safegalaxy_addr]).call()

        # setup client for requests
        safegalaxy = w3.eth.contract(safegalaxy_addr, abi=safegalaxy_abi)
        total_supply = safegalaxy.functions.totalSupply().call()
        burn = safegalaxy.functions.balanceOf("0x000000000000000000000000000000000000dEaD").call()

        total_cir_supply = (total_supply - burn)

        dead = Web3.fromWei(burn, "nanoether")
        price_one_bnb = Web3.fromWei(wbnb_to_busd[1], "wei")

        new_dead = '{:,}'.format(round(dead, 2))

        decimal = 1000000000

        # total supply market cap calc, not cir supply
        market_cap_usd = total_supply / float(wbnb_to_safe[1]) / decimal * float(price_one_bnb)

        cap_usd = '{:,}'.format(round(market_cap_usd, 2))

        print(market_cap_usd)
        print(total_cir_supply)
        print(total_supply)
        print(format(float(market_cap_usd / total_supply), '.25f'))

        dex_guru_url = "https://api.dex.guru/v1/tokens/0x6b51231c43b1604815313801db5e9e614914d6e4-bsc"
        headers = {
            # ":authority": "api.dex.guru",
            # ":method": "GET",
            # ":path": "/v1/tokens/0x6b51231c43b1604815313801db5e9e614914d6e4-bsc",
            # ":scheme": "https",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            # "accept-encoding": "gzip, deflate, br",
            # "accept-language": "en-US,en;q=0.9",
            "cache-control": "no-cache",
            # "pragma": "no-cache",
            # "referer": "https://api.dex.guru/v1/tokens/0x6b51231c43b1604815313801db5e9e614914d6e4-bsc",
            # "cookie": "__cfduid=df4bab96a3784e4bfb4c25ea8ea889e171618819996; Path=/; Domain=dex.guru; Secure; HttpOnly; Expires=Wed, 19 May 2021 08:13:16 GMT;",
            # "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36",
            # "user-agent": "PostmanRuntime/7.26.10",
            # "sec-ch-ua": "\"Google Chrome\";v=\"89\", \"Chromium\";v=\"89\", \";Not A Brand\";v=\"99\"",
            # "sec-ch-ua-mobile": "?0",
            # "sec-fetch-dest": "document",
            # "sec-fetch-mode": "navigate",
            # "sec-fetch-site": "same-origin",
            # "sec-fetch-user": "?1",
        }

        # adapter = HTTP20Adapter(headers=headers)
        # s = requests.Session()
        # s.mount('https://', adapter)

        # print(adapter)
        # print(s)

        session = HTMLSession(browser_args=["--no-sandbox", '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68'])

        r = session.get(dex_guru_url)

        r.html.render(keep_page=True)  # this call executes the js in the page
        r.session.close()

        # asession = AsyncHTMLSession()

        # async def get_page():
        #     r = await asession.get(link)
        #     return r

        # results = asession.run(get_page)

        # response = requests.get(dex_guru_url, headers=headers, timeout=10)
        # response = s.get(dex_guru_url, timeout=10)

        print(r)

        # status_code = response.status_code
        # print(status_code)

        # if status_code != 200:
        #     return f"Error with Dex Guru API code: {status_code}"


        # r_json = response.json()

        # print(r_json)

        # volume_24hr_direction = "up"
        # if float(r_json["volumeChange24h"]) < 0.0:
        #     volume_24hr_direction = "down"

        # price_24hr_direction = "up"
        # if float(r_json["priceChange24h"]) < 0.0:
        #     price_24hr_direction = "down"

        # holders_url = "https://bscscan.com/token/0x6b51231c43b1604815313801db5e9e614914d6e4"

        # headers = {
        #     'Access-Control-Allow-Origin': '*',
        #     'Access-Control-Allow-Methods': 'GET',
        #     'Access-Control-Allow-Headers': 'Content-Type',
        #     'Access-Control-Max-Age': '3600',
        #     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        # }

        # req = requests.get(holders_url, headers)

        # soup = BeautifulSoup(req.content, "html.parser")

        # body_tags = "".join([str(s) for s in soup.find_all('div', id=lambda x: x and x.endswith('tokenHolders'))])

        # soup = BeautifulSoup(body_tags, "html.parser")

        # stats = {
        #     "holders": soup.get_text().split()[1],
        #     "liquidity_generated": '{:,}'.format(round(r_json["liquidityUSD"], 2)),
        #     "market_cap": cap_usd,
        #     "volume_24hr": '{:,}'.format(round(r_json["volume24hUSD"], 2)),
        #     "volume_24hr_change": str(abs(round(r_json["volumeChange24h"], 2))),
        #     "volume_24hr_direction": volume_24hr_direction,
        #     "tokens_burned": new_dead,
        #     "current_price": format(float(r_json["priceUSD"]), '.15f'),
        #     "price_24hr_change": str(abs(round(r_json["priceChange24h"], 2))),
        #     "price_24hr_direction": price_24hr_direction,
        #     "timestamp_unix": int(datetime.now().timestamp()),
        #     "timestamp_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S %Z"),
        # }

        # print(stats)

        # dynamo_response = self.dynamodb_update(1, stats)

        # print(dynamo_response)

    def dynamodb_update(self, last_id, stats):
        dynamodb = boto3.resource(
            "dynamodb",
            aws_access_key_id=env("AWS_CLIENT"),
            aws_secret_access_key=env("AWS_SECRET"),
            region_name="us-east-1",
            endpoint_url="https://dynamodb.us-east-1.amazonaws.com"
        )
        table = dynamodb.Table("last_price")
        response = table.update_item(
            Key={
                "last_id": last_id,
            },
            UpdateExpression="set \
                current_price = :var1 \
                holders = :var2 \
                liquidity_generated = :var3 \
                market_cap = :var4 \
                price_24hr_change = :var5 \
                price_24hr_direction = :var6 \
                timestamp_unix = :var7 \
                timestamp_utc = :var8 \
                tokens_burned = :var9 \
                volume_24hr = :var10 \
                volume_24hr_change = :var11 \
                volume_24hr_direction = :var12",
            ExpressionAttributeValues={
                ':var1': stats["current_price"],
                ':var2': stats["holders"],
                ':var3': stats["liquidity_generated"],
                ':var4': stats["market_cap"],
                ':var5': stats["price_24hr_change"],
                ':var6': stats["price_24hr_direction"],
                ':var7': stats["timestamp_unix"],
                ':var8': stats["timestamp_utc"],
                ':var9': stats["tokens_burned"],
                ':var10': stats["volume_24hr"],
                ':var11': stats["volume_24hr_change"],
                ':var12': stats["volume_24hr_direction"],
            },
        )

        return response
