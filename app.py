from datetime import datetime as dt
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = ''
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

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

if __name__ == '__main__':
    app.run()
