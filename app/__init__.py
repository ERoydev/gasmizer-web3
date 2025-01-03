from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from .routes import HelloWorld, GetGasPrices, GetGasHistory


def create_app():
    app = Flask(__name__)
    api = Api(app)
    CORS(app)  # Enable Cross-Origin Resource Sharing

    api.add_resource(HelloWorld, "/")
    api.add_resource(GetGasPrices, "/gas/")
    api.add_resource(GetGasHistory, "/gas-history/")

    return app
