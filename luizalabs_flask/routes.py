from flask_restful import Api
from luizalabs_flask import app
from .product_api_views import ProductApi


api = Api(app)

api.add_resource(ProductApi, '/api/product/<int:id>')

