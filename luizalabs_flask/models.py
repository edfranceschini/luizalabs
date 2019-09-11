# coding=utf-8
from luizalabs_flask import db
from .database_handler import CustomModel



#  tabela auxiliar para relacionamentos Many-to-many
class Favorito(db.Model, CustomModel):

    cliente_id = db.Column(
        db.Integer,
        db.ForeignKey('cliente.id'),
        primary_key=True)
    produto_id = db.Column(
        db.Integer,
        db.ForeignKey('produto.id'),
        primary_key=True)

    def __repr__(self):
        return '<Favorito %r>' % self.cliente_id

    @property
    def relations_exists(self):
        cliente = Cliente.query.filter_by(id=self.cliente_id).first()
        produto = Produto.query.filter_by(id=self.produto_id).first()
        if not cliente or not produto:
            return False
        return True


#  tabela de clientes
class Cliente(db.Model, CustomModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=False, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)

    def __repr__(self):
        return '<Cliente %r>' % self.name

    def get(self, id):
        return Cliente.query.filter_by(id=id).first()

    @property
    def relations_exists(self):
        return True

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

    @property
    def relations_exists(self):
        return True