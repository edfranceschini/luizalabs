# coding=utf-8
from .api_view_abstractor import Api_view
from .models import Favorito


class Favorito(Api_view):
    model = Favorito


# Contorno para usar o mesmo endopoint como recuro em URL diferentes
# somento para listagem.
class Favoritos(Favorito):

    pass