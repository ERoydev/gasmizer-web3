from flask_restful import Resource
from .services import get_gas_price, get_gas_prediction

class GasPrice(Resource):
    def get(self):
        price = get_gas_price()  # Call the function to fetch gas prices
        return price

class GasPrediction(Resource):
    def get(self):
        prediction = get_gas_prediction()  # Call the function to predict gas fee windows
        return prediction
