
from flask import Flask, request


# __name__ => muestra si el archivo en el cual se esta llamando a la clase Flask, es el archivo
# principal del proyecto, para eviar que la instancia de la clase de Flask se puede crear varias veces

# si estamos en el archivo pincipal nos imprimira => __main__, caso contrario imprimira otra cosa

# print(__name__)
app = Flask(__name__)


# un decorador es un patron de software que se utiliza para modificar el funcionmiento de una
# de una funcion o clase en particular sin la necesidad de emplear otro metodo con la herencia
@app.route("/")
def inicio():
    print("Me hicieron un llamado")
    return "saludos del mi API"



@app.route("/productos", methods=["GET","POST"])
def gestion_productos():
   # print(request.method)

    if request.method == "POST":
        data = request.get_json()
        print(data)
        return{
            "mensage": "producto creado exitosamente"
        }
    elif request.method == "GET":
        return{
            "message": "Estos son los productos registrados"
        }

    


# debug = True => que cada cez que se hagamos un cambio y lo guardemos automaticamente se reinicaira
# mi servidor con los nuevos cambios
app.run(debug=True)



# todo codigo que pogamos despues del metodo run NUNCA se ejecutara porque el metodo run() hace que,
# solgado mi programa levantando un servidor

# ----------print("Servira esto?")