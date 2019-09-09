from flask_restful import Resource, Api
from luizalabs_flask import app

api = Api(app)

class ApiRoot(Resource):

    def get(self):
        pass

    def post(self):
        pass


@app.route('/')
def hello_world():
    return 'Hello World!'

api.add_resource(ApiRoot, '/api/v1/')
# api.add_resource()

