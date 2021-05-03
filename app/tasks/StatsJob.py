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
import cloudscraper
from requests_html import HTMLSession


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

        # print(market_cap_usd)
        # print(total_cir_supply)
        # print(total_supply)
        # print(format(float(market_cap_usd / total_supply), '.25f'))

        dex_guru_url = "https://api.dex.guru/v1/tokens/0x6b51231c43b1604815313801db5e9e614914d6e4-bsc"
        bogcharts_url = "https://charts.bogged.finance/?token=0x6b51231c43B1604815313801dB5E9E614914d6e4"

        session = HTMLSession(
            browser_args=[
                '--no-sandbox',
                '--single-process',
                '--disable-dev-shm-usage',
                '--disable-gpu',
                '--no-zygote'
            ]
        )

        r = session.get(bogcharts_url)

        bogged_status_code = r.status_code

        # bogged_call_success = False
        if bogged_status_code == 200:
            # bogged_call_success = True

            r.html.render(sleep=15, keep_page=True)

            html_content = r.html.html

            soup = BeautifulSoup(html_content, "html.parser")

            print(soup.find_all("h4"))

            scifi_nota_price = float(soup.find_all("h4")[1].text.split("$")[-1])
            price_24hr = float(soup.find_all("h4")[2].text.split("%")[0])
            volume_24hr = float(soup.find_all("h4")[3].text.split("$")[-1].replace(",", ""))
            liquidity_generated = float(soup.find_all("h4")[4].text.split("$")[-1].replace(",", ""))

            print("bogged charts price")
            print(scifi_nota_price)
            print(price_24hr)
            print(volume_24hr)
            print(liquidity_generated)

            if scifi_nota_price == 0:
                stat_record = self.dynamodb_get(1)["Item"]
                print(stat_record)
                current_long_price = stat_record["current_price"]
                price_24hr = stat_record["price_24hr_change"]
                volume_24hr = stat_record["volume_24hr"]
                liquidity_generated = stat_record["liquidity_generated"]

            else:
                current_long_price = format(float(scifi_nota_price), '.15f')
        else:
            stat_record = self.dynamodb_get(1)["Item"]
            print(stat_record)
            current_long_price = stat_record["current_price"]
            price_24hr = stat_record["price_24hr_change"]
            volume_24hr = stat_record["volume_24hr"]
            liquidity_generated = stat_record["liquidity_generated"]

        scraper = cloudscraper.create_scraper()
        response = scraper.get(dex_guru_url, timeout=2)

        status_code = response.status_code
        print(status_code)

        if status_code != 200:
            return f"Error with Dex Guru API code: {status_code}"

        r_json = response.json()

        print(r_json)

        volume_24hr_direction = "up"
        if float(r_json["volumeChange24h"]) < 0.0:
            volume_24hr_direction = "down"

        price_24hr_direction = "up"
        if float(price_24hr) < 0.0:
            price_24hr_direction = "down"

        holders_url = "https://bscscan.com/token/0x6b51231c43b1604815313801db5e9e614914d6e4"

        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }

        req = requests.get(holders_url, headers)

        soup = BeautifulSoup(req.content, "html.parser")

        body_tags = "".join([str(s) for s in soup.find_all('div', id=lambda x: x and x.endswith('tokenHolders'))])

        soup = BeautifulSoup(body_tags, "html.parser")

        stats = {
            "holders": soup.get_text().split()[1],
            "liquidity_generated": '{:,}'.format(round(liquidity_generated, 2)),
            "market_cap": cap_usd,
            "volume_24hr": '{:,}'.format(round(volume_24hr, 2)),
            "volume_24hr_change": str(abs(round(r_json["volumeChange24h"], 2))),
            "volume_24hr_direction": volume_24hr_direction,
            "tokens_burned": new_dead,
            "current_price": current_long_price,
            "price_24hr_change": str(abs(round(price_24hr / 100, 2))),
            "price_24hr_direction": price_24hr_direction,
            "timestamp_unix": int(datetime.now().timestamp()),
            "timestamp_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S %Z"),
        }

        print(stats)

        dynamo_response = self.dynamodb_update(1, stats)

        print(dynamo_response)

    def dynamodb_get(self, last_id):
        dynamodb = boto3.resource(
            "dynamodb",
            aws_access_key_id=env("AWS_CLIENT"),
            aws_secret_access_key=env("AWS_SECRET"),
            region_name="us-east-1",
            endpoint_url="https://dynamodb.us-east-1.amazonaws.com"
        )
        table = dynamodb.Table("last_price")
        response = table.get_item(
            Key={
                "last_id": last_id,
            },
        )
        return response

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
                current_price = :var1, \
                holders = :var2, \
                liquidity_generated = :var3, \
                market_cap = :var4, \
                price_24hr_change = :var5, \
                price_24hr_direction = :var6, \
                timestamp_unix = :var7, \
                timestamp_utc = :var8, \
                tokens_burned = :var9, \
                volume_24hr = :var10, \
                volume_24hr_change = :var11, \
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
