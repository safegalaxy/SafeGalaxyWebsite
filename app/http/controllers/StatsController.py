"""A StatsController Module."""

from masonite.request import Request
from masonite.controllers import Controller
import app.helpers.utilities as utilities
from web3 import Web3
import simplejson
from decimal import *


class StatsController(Controller):
    """StatsController Controller Class."""

    def stats(self, request: Request):
        action = request.input("action")

        w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))

        safegalaxy_addr, safegalaxy_abi = utilities.get_safegalaxy_auth()
        # pancake_swap_addr, pancake_swap_abi = utilities.get_pancake_swap_auth()
        # wbnb = utilities.get_wrapped_bnb_addr()
        # busd = utilities.get_binance_usd_addr()

        # setup client for requests
        # pancake_router = w3.eth.contract(pancake_swap_addr, abi=pancake_swap_abi)

        # wbnbtobusd = pancake_router.functions.getAmountsOut(1, [wbnb, busd]).call()
        # wbnbtosafe = pancake_router.functions.getAmountsOut(1000000000, [wbnb, safe]).call()

        # setup client for requests
        safegalaxy = w3.eth.contract(safegalaxy_addr, abi=safegalaxy_abi)
        totalSupply = safegalaxy.functions.totalSupply().call()
        burn = safegalaxy.functions.balanceOf("0x000000000000000000000000000000000000dEaD").call()

        total_cir_supply = (totalSupply - burn)

        # circ = Web3.fromWei(total_cir_supply, "nanoether")
        # dead = Web3.fromWei(burn, "nanoether")
        # oneBNB = Web3.fromWei(wbnbtosafe[1], "nanoether")
        # price1BNB = Web3.fromWei(wbnbtobusd[1],"wei")
        # priceFOR1BNB = str((price1BNB / oneBNB))
        # priceFOR1sg = priceFOR1BNB.replace(".0", ".0000000")

        # newcirc = '{:,}'.format(round(circ,2))
        # newdead = '{:,}'.format(round(dead,2))

        # decimal = 1000000000
        # marketcapbnb = total_cir_supply / float(wbnbtosafe[1]) / decimal
        # marketcapusd = total_cir_supply / float(wbnbtosafe[1]) / decimal * float(price1BNB)

        # capbnb = '{:,}'.format(round(marketcapbnb, 2))
        # capusd = '{:,}'.format(round(marketcapusd, 2))

        # Total Circulating Supply is {newcirc}
        # Total Burn Supply is {newdead}
        # Marketcap is {capbnb} in BNB
        # Marketcap is ${capusd} in USD

        # For CMC
        if action == "cir-supply":
            return total_cir_supply
