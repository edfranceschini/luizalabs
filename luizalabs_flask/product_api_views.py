# coding=utf-8

import json
from flask import Response
from flask_restful import Resource
from flask_restful import reqparse
from flask_sqlalchemy import Pagination
from luizalabs_flask.models import Cliente, Produto


class Product(Resource):
    '''
    classe para gerenciar requisições de produtos na API
    '''

    def get(self, id=None):

        # Verifica parametros no request
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int, help='Page')
        parser.add_argument('per_page', type=int, help='Items per page')
        args = parser.parse_args()

        # Explícito é melhor que implícito
        if args['per_page'] is None:
            per_page = 10
        else:
            per_page = args['per_page']
        if args['page'] is None:
            page = 1
        else:
            page = args['page']

        if id is not None:
            response = self.format_response(Produto.query.get(id))
        else:
            response = self.format_response(
                Produto.query.paginate(page, per_page))

        return Response(json.dumps(response[0]),
                        status=response[1],
                        mimetype=response[2])

    def post(self):
        pass

    def put(self):
        pass

    def format_response(self, produto):
        data = []
        mimetype = 'application/json'
        if produto is not None:
            if type(produto) != Pagination:
                data = produto.serialize
            else:
                for item in produto.items:
                    data.append(item.serialize)
            status = 200
        else:
            data = ['Not found- 404']
            status = 404
        return (data,
                status,
                mimetype)

    @staticmethod
    def _get_next_id():
        return Produto.query.last().id+1


# Contorno para usar o mesmo endopoint como recuro em URL diferentes
# somento para listagem.
class Products(Product):

    def post(self):
        return json('Metodo não permitido', 400)

    def put(self):
        return json('Metodo não permitido', 400)