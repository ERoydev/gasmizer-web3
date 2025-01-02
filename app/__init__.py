from flask import Flask
from flask_cors import CORS
from flask_restful import Api

def create_app():
    app = Flask(__name__)
    CORS(app)  # Enable Cross-Origin Resource Sharing
    api = Api(app)

    from .routes import GasPrice, GasPrediction
    api.add_resource(GasPrice, '/api/gas-price')
    api.add_resource(GasPrediction, '/api/gas-prediction')

    return app
