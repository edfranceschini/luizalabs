import json
from flask import Response, abort
from flask_sqlalchemy import BaseQuery


class CustomBaseQuery(BaseQuery):

    def get_or_415(self, ident):
        model_class_name = ''
        try:
            model_class_name = self._mapper_zero().class_.__name__
        except Exception as e:
            print(e)

        rv = self.get(ident)
        if not rv:
            error_message = json.dumps({'message': model_class_name + ' ' + str(ident) + ' not found'})
            abort(Response(error_message, 415))
        return rv


