from os import environ
from flask import Flask, request

# para usar las variables declaradas en el archivo .env
from dotenv import load_dotenv
from os import environ
load_dotenv()



app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DATABASE_URI")



@app.route("/")
def initial_controller():
    return{
        "message":"Bienvenido a mi API de receta de Postres 🎂"
    }




if __name__ == "__main__":
    app.run(debug=True)