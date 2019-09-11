# coding=utf-8
from flask_restful import Api
from luizalabs_flask import app
from .product_api_views import Product, Products
from .client_api_views import Customer, Customers
from .favorite_api_views import Favorito, Favoritos


api = Api(app)

api.add_resource(Product, '/api/product/<int:id>')
api.add_resource(Products, '/api/product/')

api.add_resource(Customer, '/api/customer/<int:id>')
api.add_resource(Customers, '/api/customer/')

api.add_resource(Favorito, '/api/favorite/<int:id>')
api.add_resource(Favoritos, '/api/favorites/')