from decouple import config
import requests
from flask import jsonify
from ..utils.response_schema import return_json_response


class OwlracleAPI:
    NETWORKS = {
        "eth": "Ethereum",
        "bsc": "Binance Smart Chain",
        "poly": "Polygon",
        "avax": "Avalanche",
        "arb": "Arbitrum",
        "opt": "Optimism",
        "ftm": "Fantom",
        "cro": "Cronos",
        "base": "Base",
        "aurora": "Aurora",
        "celo": "Celo",
        "movr": "Moonriver",
        "linea": "Linea",
        "blast": "Blast",
        "one": "Harmony",
        "goerli": "Goerli",
        "sepolia": "Sepolia",
        "pulse": "PulseChain",
    }

    def __init__(self, network=NETWORKS["eth"]):
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

    def change_network(self, network):
        self.network = network
