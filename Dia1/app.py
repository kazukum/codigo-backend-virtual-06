from os import environ
from flask import Flask, request

# para usar las variables declaradas en el archivo .env
from dotenv import load_dotenv
from os import environ

from flask_restful import Api
from controllers.postre import PostresController
from config.conexion_bd import base_de_datos
from models.postre import PostreModel
from models.preparacion import PreparacionModel
from models.ingrediente import IngredientesModel
from models.receta import RecetaModel



load_dotenv()



app = Flask(__name__)
api = Api(app)

app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DATABASE_URI")


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# ininciar la BD para dale la credenciales definidas en el config
base_de_datos.init_app(app)

# crea todas las tablas definidas en los modelos en el proyecto
base_de_datos.create_all(app=app)
@app.route("/")
def initial_controller():
    return{
        "message":"Bienvenido a mi API de receta de Postres 🎂"
    }


# DEFINO Las rutas usando flask restful
api.add_resource(PostresController,"/postres")



if __name__ == "__main__":
    app.run(debug=True)



# --------------------------------------------------------------
# esto es para editar las tablas siempre comentarlo despues de utilizarlo

# tener cuidado elimina tablas
# base_de_datos.dop_all(app=app)