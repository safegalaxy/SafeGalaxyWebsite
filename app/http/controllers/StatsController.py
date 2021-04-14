"""A StatsController Module."""

from masonite.request import Request
from masonite.controllers import Controller
import app.helpers.utilities as utilities
from web3 import Web3
import simplejson as json
from decimal import *
import requests
from datetime import datetime, timezone
from bs4 import BeautifulSoup
import requests


class StatsController(Controller):
    """StatsController Controller Class."""

    def stats(self, request: Request):
        action = request.input("action")

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

        # For CMC
        if action == "cir-supply":
            return total_cir_supply

        else:
            dead = Web3.fromWei(burn, "nanoether")
            price_one_bnb = Web3.fromWei(wbnb_to_busd[1], "wei")

            new_dead = '{:,}'.format(round(dead, 2))

            decimal = 1000000000

            # total supply market cap calc, not cir supply
            market_cap_usd = total_supply / float(wbnb_to_safe[1]) / decimal * float(price_one_bnb)

            cap_usd = '{:,}'.format(round(market_cap_usd, 2))

            response = requests.get("https://api.dex.guru/v1/tokens/0x6b51231c43b1604815313801db5e9e614914d6e4-bsc")

            status_code = response.status_code
            r_json = response.json()

            print(status_code)
            print(r_json)

            volume_24hr_direction = "up"
            if float(r_json["volumeChange24h"]) < 0.0:
                volume_24hr_direction = "down"

            price_24hr_direction = "up"
            if float(r_json["priceChange24h"]) < 0.0:
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
                "liquidity_generated": '{:,}'.format(round(r_json["liquidityUSD"], 2)),
                "market_cap": cap_usd,
                "volume_24hr": '{:,}'.format(round(r_json["volume24hUSD"], 2)),
                "volume_24hr_change": str(abs(round(r_json["volumeChange24h"], 2))),
                "volume_24hr_direction": volume_24hr_direction,
                "tokens_burned": new_dead,
                "current_price": format(float(r_json["priceUSD"]), '.15f'),
                "price_24hr_change": str(abs(round(r_json["priceChange24h"], 2))),
                "price_24hr_direction": price_24hr_direction,
                "timestamp_unix": int(datetime.now().timestamp()),
                "timestamp_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S %Z"),
            }

            request.header("Content-Type", "application/json")
            request.header("Cache-Control", "max-age=60")
            request.header("Last-Modified", datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT'))

            return json.dumps(stats)
