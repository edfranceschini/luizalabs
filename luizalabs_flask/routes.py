from flask_restful import Api
from luizalabs_flask import app
from .product_api_views import Product, Products


api = Api(app)

api.add_resource(Product, '/api/product/<int:id>')
api.add_resource(Products, '/api/product/')

