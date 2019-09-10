from flask import Response
from flask import jsonify
from flask_restful import Resource
from luizalabs_flask.models import Cliente, Produto


class ProductApi(Resource):
    '''
    classe para gerenciar requisições de produtos na API
    '''

    def get(self, id):
        response = self.format_response(Produto.query.get(id))
        print(response[0])
        return Response(response[0],
                        status=response[1],
                        mimetype=response[2])

    def post(self):
        pass

    def put(self):
        pass

    def format_response(self, produto):
        data = 'Not found- 404'
        status = 404
        mimetype = 'application/json'
        if produto is not None:
            data = produto.serialize
            status = 200
        return (data,
                status,
                mimetype)

    @staticmethod
    def _get_next_id():
        return Produto.query.last().id+1
