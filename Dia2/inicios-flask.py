

from flask import Flask, request

# __name__ => muestra si el archivo en el cual se esta llamando a la clase Flask, es el archivo
# principal del proyecto, para eviar que la instancia de la clase de Flask se puede crear varias veces

# si estamos en el archivo pincipal nos imprimira => __main__, caso contrario imprimira otra cosa

# print(__name__)
app = Flask(__name__)
productos =[]

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
        productos.append(data)
        return{
            "mensage": "producto creado exitosamente",
            "content": data
        },200
    elif request.method == "GET":
        return{
            "message": "Estos son los productos registrados",
            "content": productos
        },404

    
@app.route("/productos/<int:id>", methods=["PUT","DELETE","GET"])

def gestion_producto(id):
    print(id)
    
    if len(productos)<= id:
         return{
                "message": "Producto no encontrado"
        },404
    # tarea 
    # buscar segun la posicion el producto, si el producto no existe retornar un estado 404, sin embago  si si exite retornar el producto y un estado 200
    if request.method == "GeT":
       # try:
       #    return{
       #         "content": productos[id]
       #    },200
       # except:
        #    return{
        #        "message": "Producto no encontrado"
        #    },404
        # METODO 2
        return{
             "content": productos[id]
        },200

    elif request.method == "DELETE":
        productos.pop(id)
        return{
            "message": "Producto eliminado exitosamente"
        }
    elif request.method == "PUT":
        data = request.get_json()
        productos[id]= data
        return{
            "message":"Productos actualizado exitosamente",
            "content" : productos[id]
        },201

    

@app.route("/productos/buscar")
def buscar_productos():
    print(request.args.get("nombre"))
    return "ok"



# debug = True => que cada cez que se hagamos un cambio y lo guardemos automaticamente se reinicaira
# mi servidor con los nuevos cambios
app.run(debug=True)



# todo codigo que pogamos despues del metodo run NUNCA se ejecutara porque el metodo run() hace que,
# solgado mi programa levantando un servidor

# ----------print("Servira esto?")