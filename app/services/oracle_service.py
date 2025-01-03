from decouple import config
import requests
from flask import jsonify
from ..utils.response_schema import return_json_response


class OwlracleAPI:
    NETWORKS = {
        "Ethereum": "eth",
        "Binance Smart Chain": "bsc",
        "Polygon": "poly",
        "Avalanche": "avax",
        "Arbitrum": "arb",
        "Optimism": "opt",
        "Fantom": "ftm",
        "Cronos": "cro",
        "Base": "base",
        "Aurora": "aurora",
        "Celo": "celo",
        "Moonriver": "movr",
        "Linea": "linea",
        "Blast": "blast",
        "Harmony": "one",
        "Goerli": "goerli",
        "Sepolia": "sepolia",
        "PulseChain": "pulse"
    }

    def __init__(self, network=NETWORKS["Ethereum"]):
        self.network = network
        self.api_key = config('OWLRACLE_API_KEY')

    def get_gas_prices(self):
        api_url = f'https://api.owlracle.info/v4/{self.network}/gas?apikey={self.api_key}'

        res = requests.get(api_url)

        if res.status_code == 200:
            data = res.json()
            return return_json_response(f"Gas prices fetched successfully.", data, 200)

        else:
            return return_json_response(f"Failed to fetch gas prices.", {}, 500)

    def get_gas_history(self):
        api_url = f'https://api.owlracle.info/v4/{self.network}/history'

        res = requests.get(api_url)

        if res.status_code == 200:
            data = res.json()
            return return_json_response(f"Gas history fetched successfully.", data, 200)

        else:
            return return_json_response(f"Failed to fetch gas history.", {}, 500)

    def post_change_network(self, network):
        if network not in self.NETWORKS:
            return return_json_response(
                f"Invalid network. Available networks: {', '.join(self.NETWORKS.keys())}",
                {},
                400,)

        self.network = network
        return return_json_response(f"Network changed successfully.", {}, 200)
