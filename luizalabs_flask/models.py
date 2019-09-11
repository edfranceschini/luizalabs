# coding=utf-8
from luizalabs_flask import db
from .database_handler import CustomModel



#  tabela auxiliar para relacionamentos Many-to-many
favoritos = db.Table('favoritos',
                     db.Column('cliente_id',
                               db.Integer,
                               db.ForeignKey('cliente.id'),
                               primary_key=True),
                     db.Column('produto_id',
                               db.Integer,
                               db.ForeignKey('produto.id'),
                               primary_key=True)
                     )

#  tabela de clientes
class Cliente(db.Model, CustomModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=False, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)

    def __repr__(self):
        return '<Cliente %r>' % self.name

    def get(self, id):
        return Cliente.query.filter_by(id=id).first()



#  tabela de produtos
class Produto(db.Model, CustomModel):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=True, nullable=True)
    price = db.Column(db.Float)
    image = db.Column(db.String(256), nullable=True)
    brand = db.Column(db.String(128), nullable=True)
    reviewScore = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return '<Produto %r>' % self.title


