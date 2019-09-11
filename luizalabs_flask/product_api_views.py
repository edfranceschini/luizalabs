# coding=utf-8
import json
from .api_view_abstractor import Api_view
from .models import Produto


class Product(Api_view):
    model = Produto


# Contorno para usar o mesmo endopoint como recuro em URL diferentes
# somento para listagem.
class Products(Product):

    pass