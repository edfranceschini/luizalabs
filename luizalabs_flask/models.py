
from luizalabs_flask import db
from datetime import datetime as dt
from .database_handler import  CustomBaseQuery


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


#  tabela de produtos
class Produto(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=True, nullable=True)
    price = db.Column(db.Float)
    image = db.Column(db.String(256), nullable=True)
    brand = db.Column(db.String(128), nullable=True)
    reviewScore = db.Column(db.Float, nullable=True)
    created = db.Column(db.DateTime, nullable=True, default=dt.now)

    def __repr__(self):
        return '<Produto %r>' % self.title

    @property
    def serialize(self):
        return{
            'id': self.id,
            'title': self.title,
            'price': self.price,
            'image': self.image,
            'brand': self.brand,
            'reviewScore': self.reviewScore,
            'created': dump_datetime(self.created)
        }


def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return [value.strftime("%Y-%m-%d"), value.strftime("%H:%M:%S")]
