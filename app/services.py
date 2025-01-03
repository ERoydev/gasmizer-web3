import requests
from decouple import config

def get_gas_price():
    # Example: Fetching gas price from GasNow API
    url = "https://api.gasnow.org/v3/gas/price?token=YOUR_API_KEY"
    response = requests.get(url)
    data = response.json()
    return {"standard": data["data"]["standard"], "fast": data["data"]["fast"], "low": data["data"]["low"]}

def get_gas_prediction():
    # Example: Basic prediction logic (this can be replaced with AI models later)
    return {"prediction": "Best time to transact is from 10 PM to 2 AM."}

def get_gas_prices():
    network = 'eth' # could be any supported network
    key = config('OWLRACLE_API_KEY')
    res = requests.get(f'https://api.owlracle.info/v4/{network}/gas?apikey={key}')
    data = res.json()
    print(data)