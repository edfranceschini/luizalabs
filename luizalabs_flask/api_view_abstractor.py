# coding=utf-8
import json
from luizalabs_flask import db
from flask import Response, request
from flask_restful import Resource
from flask_restful import reqparse
from flask_sqlalchemy import Pagination
from sqlalchemy.exc import IntegrityError


class Api_view(Resource):
    '''
    Classe abastratora de resposta da API
    '''

    # Override init para gerar variavel de tipo de objeto
    def __init__(self):

        super(Api_view, self).__init__()


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
            response = self.format_response(self.model.query.get(id))
        else:
            response = self.format_response(
                self.model.query.paginate(page, per_page, error_out=False))

        return Response(json.dumps(response[0]),
                        status=response[1],
                        mimetype=response[2])

    def post(self):
        return self.db_parser()


    def put(self):
        return self.db_parser(update=True)


    def delete(self):
        return self.db_parser(delete=True)


    def db_parser(self, update=False, delete=False):

        columns = self.model._get_columns(self.model)  # todo !Melhorar isso!
        post_data = request.get_json()
        valid = self.validate(columns, post_data)

        if valid:
            save_data = self.model(**post_data)

            if not update and not delete:

                db.session.add(save_data)
                try:
                    db.session.commit()
                    db.session.close()
                    return Response(json.dumps({"message": 'Criado'}), 201)
                except IntegrityError:
                    return Response(json.dumps({"message":'Registro já existe.'
                                    ' Para atualiza utilize o método PUT.'}),
                                    409)

            if update:

                # todo: Melhorar isso
                unique_field = self.model.handle_unique_column(self.model)
                unique_search = {unique_field: post_data[unique_field]}
                record = self.model.query.filter_by(
                    **unique_search).update(post_data)
                db.session.commit()
                return Response(json.dumps({"message": 'Atualizado'}), 200)

            if delete:

                record = self.model.query.filter_by(**post_data).first()
                if not record:
                    return Response(json.dumps(
                        {"message": 'Registro não encontrado'}), 400)
                db.session.delete(record)
                db.session.commit()
                return Response(
                    json.dumps({"message": 'Registro excluído'}), 200)

        return Response(json.dumps(
            {"message": 'Erro nos parametros de entrada.'}), 400)


    def validate(self, col, data):
        """
        Metodo pode ser melhorado para uma verificação mais concistente.
        porém está aqui somente para mostrar o desvio para validação.
        :param col:
        :param data:
        :return bolean:
        """
        print(col)
        print(data)
        if self.model.relations_exists:
        # validar se todos os campos existem (menos o ID):
            for c in col:  # todo Refactorar pois não está elegante
                if c != 'id':
                    try:
                        data[c]
                    except:
                        return False
            return True
        return False


    def format_response(self, object):
        data = []
        mimetype = 'application/json'
        if object is not None:
            if type(object) != Pagination:
                data = object.serialize
            else:
                for item in object.items:
                    data.append(item.serialize)
            status = 200
        else:
            data = ['Not found- 404']
            status = 404
        return (data,
                status,
                mimetype)


