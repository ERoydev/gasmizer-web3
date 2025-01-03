from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from .routes import HelloWorld, GetGasPrices, GetGasHistory


def create_app():
    app = Flask(__name__)
    api = Api(app)
    CORS(app)  # Enable Cross-Origin Resource Sharing

    network = "Ethereum" # Default network on initialization, oracle_service has a request to change it.

    api.add_resource(HelloWorld, "/")
    api.add_resource(GetGasPrices, "/<string:network>/gas-prices/")
    api.add_resource(GetGasHistory, "/<string:network>/gas-history/")

    return app
