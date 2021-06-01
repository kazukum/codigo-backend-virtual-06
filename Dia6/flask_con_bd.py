
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import math

# esto sirbe para que si tenemos un archivo .env jale todas las variables como si fuesen variables de entorno

from dotenv import load_dotenv
from os import environ



load_dotenv()

app = Flask(__name__)
app.config ["MYSQL_HOST"] = environ.get("HOST")
app.config ["MYSQL_USER"] = environ.get("USER")
app.config ["MYSQL_PASSWORD"] = environ.get("PASSWORD")
app.config ["MYSQL_DB"] = environ.get("DATABASE")
app.config ["MYSQL_PORT"] = int(environ.get("PORT"))



mysql = MySQL(app)

@app.route("/alumnos")
def gestion_alumnos():
    # primero creo mi cursor que se conectara a la BD
    cur = mysql.connection.cursor()
    # registro la sentencia ya sea un DDL o DML
    cur.execute("SELECT * FROM ALUMNOS")
    # capturo la informacion a partir de la consulta



    alumnos = cur.fetchall()
    alumnos_dict =[]
    for alumno in alumnos:
        alumno_dict={
            "id": alumno[0],
            "matricula": alumno[1],
            "nombre" : alumno[2],
            "apellido":alumno[3],
            "localidad": alumno[4],
            "fecha_nacimiento":alumno[5]
 



        }
        alumnos_dict.append(alumno_dict)
    
    return{
        "data":alumnos_dict
    }



@app.route("/alumnos_paginados", methods= ["GET"])
def alumnos_paginados():
    print(request.args)
    if(request.args.get("pagina")and request.args.get("porPagina")):
        #HELPER
        porPagina = int(request.args.get("porPagina"))
        pagina = int(request.args.get("pagina"))
        limit = porPagina
        offset = (pagina -1) * porPagina # esta formula funciona para todas los BD aprenderse bien
        cur = mysql.connection.cursor()

        # %s cadena (lo vuelve string)
        # %d integral
        # %f flotante
        # %.<digitos> numeros flotantes con una cantidad fija de decimales
        cur.execute("SELECT * FROM alumnos LIMIT %s OFFSET %s" % (limit,offset))
        resultado = cur.fetchall()
        print(len(resultado))
        print(resultado)

        # ahora hacemos los datos de paginacion
        cur.execute("SELECT count(*) from alumnos")
        total = int(cur.fetchone()[0])
        itemsPorPagina =porPagina  if total >= porPagina else total
        totalPaginas = math.ceil(total / itemsPorPagina)
        if pagina > 1:
            paginaPrevia = pagina -1 if pagina <= totalPaginas  else None
        else:
            paginaPrevia = None
        if totalPaginas > 1:
            paginaContinua = pagina + 1 if pagina < totalPaginas else None
        else:
            paginaContinua = None
    

    return {
        "data" : resultado,
        "paginacion": {
            "total":total, #total de paginas
            "pagina":itemsPorPagina, #pagina actual
            "paginaPrevia":request.host_url + "alumnos_paginados?pagina={}&porPagina={}".format(paginaPrevia,porPagina) if paginaPrevia else None, 
            "paginacontinua":paginaContinua + "alumnos_paginados?pagina={}&porPagina={}".format(request.host_url, paginaContinua) if paginaContinua else None, #pagina continua
            "totalPaginas":totalPaginas,# total paginas
        }
    }
#pagina en paginaPrevia  request.host_url o request.host para que muestre la url


app.run(debug=True)    