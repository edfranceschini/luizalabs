from luizalabs_flask import db
from datetime import datetime as dt

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
class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=False, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=dt.now)

    def __repr__(self):
        return '<Cliente %r>' % self.name

    def get(self, id):
        return Cliente.query.filter_by(id=id).first()


    def favoritos(self):
        pass

#  tabela de produtos
class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    price = db.Column(db.Float)

    def __repr__(self):
        return '<Produto %r>' % self.name

