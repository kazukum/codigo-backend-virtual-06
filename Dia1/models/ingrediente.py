
from config.conexion_bd import base_de_datos
from sqlalchemy import Column, types,orm



class IngredientesModel(base_de_datos.Model):
    __tablename__="ingredientes"

    
    ingredienteId =Column(name ="id", primary_key=True,autoincrement=True,unique=True, nullable =False,type_=types.Integer)

    ingredienteNombre = Column(name="nombre",type_=types.String(length=45))

    recetas =orm.relationship("RecetaModel",backref="recetaIngrediente")
    def __init__(self, nombre):
        self.ingredienteNombre = nombre

    