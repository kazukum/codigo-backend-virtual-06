

from os import name
from config.conexion_bd import base_de_datos


from sqlalchemy import Column, types, orm

class PostreModel(base_de_datos.Model):

    # para cambiar el nombre de la tabla en la BD
    __tablename__="postres"

    postreId = Column(name ="id", primary_key=True,autoincrement=True,unique=True,type_=types.Integer)

    postreNombre = Column(name="nombre",type_=types.String(length=45))

    postrePorcion = Column(name="porcion",type_=types.String(length=25))

    preparaciones = orm.relationship("PreparacionModel", backref="preparacionPostre", lazy =True)
    def __init__(self,nombre,porcion):
        self.postreNombre = nombre
        self.postrePorcion = porcion
