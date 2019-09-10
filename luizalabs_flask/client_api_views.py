# coding=utf-8
from .api_view_abstractor import Api_view
from .models import Cliente


class Customer(Api_view):
    model = Cliente


# Contorno para usar o mesmo endopoint como recuro em URL diferentes
# somento para listagem.
class Customers(Customer):

    pass