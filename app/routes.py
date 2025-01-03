from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort
from .services.oracle_service import OwlracleAPI
from flask import request

class GetGasPrices(Resource):
    def get(self):
        oracle_instance = OwlracleAPI()
        gas_prices = oracle_instance.get_gas_prices()
        return gas_prices

class GetGasHistory(Resource):
    def get(self):
        oracle_instance = OwlracleAPI()
        gas_history = oracle_instance.get_gas_history()
        return gas_history

class ChooseNetwork(Resource):
    def post(self):
        data = request.get_json() # Get Json data from the body
        network_name = data.get('network_name')
        
        oracle_instance = OwlracleAPI()
        oracle_instance.change_network()


class HelloWorld(Resource):
    def get(self):
        return "Hello, World!"