# una forma de almacenar varios valores en una misma variable

# LISTAS = (JS arrays)

colores =['azul', 'negro', 'amarillo', 'purpura']
misc=['eduardo', 18,False,14.5,'2015-04-14',['1',2,3]]

# imprimir la primera posicion
print(colores[1])

#imprimir la ultima posicion de la lista


print(colores[len(colores)-1])
print(colores[-1])

# imprimir desde la 0 hasta la <2

print(colores[0:2])

#imprimir desde la posicion 1

print(colores[1:])

#la forma de copiar el contenido y ya no utlizar la misma posicion de mmoria para ambas variables es :
# en js se usaria colores2 = [...colores]
colores2 = colores[:]
colores2[0] = "violeta"
print(colores)


nombre = "juanito"
print(nombre[1])
# solamente se puede usar la posiciones de una variable str pra leer mas no para modificar su contenido
#nombre[1] = "e"

#metodo para agregar un nuevo elemento a una lista
colores.append('indigo')
print(colores)

# metodo para eliminar un valor si existe lo eliminara sino indicara un error
colores.remove("azul")
print(colores)

#el metodo pop ademas de aliminarlo lo podemos almacenar en una variable
colore_eliminado = colores.pop(0)
print(colores)
print(colore_eliminado)

# otro metodo para eliminar un valor de una lista
del colores[0]
print(colores)

# metodo para resetear toda la lista y dejarla en blanco
colores.clear()
print(colores)

# --------------------------------------------------------------------
# TUPLAS => coleccion de elements ordenada NOSE PUEDE MODIFICAR LUEGO DE CREACION
notas = (10,16,17,11,5,1,5,5,5)
print(notas[0])
print(notas[-1])

# print (notas.length()) esto es para JS
print(len(notas))

# la cantidad de elemtos de la tupla notas es 6 elementos
print("la cantidad de elementos de la tupla notas es {} elementos".format(len(notas)))
print(f"la cantidad de elementos de la tupla notas es {len(notas)} elementos")
print(f"la cantidad de elementos de la tupla notas es", len(notas),"elementos")


# ver si hay elementos repetidos en una tupla
print(notas.count(5))

#-------------------------------------------------------------------------------

# CONJUNTOS => coleccion de elementos DESORDENADA osea que una vez que la creemos no podremos acceder 
#sus posiciones ya sea ordenada aleatoriamente

estaciones = {"VERANO", "OTOÑO", "PRIMAVERA","INVIERNO"}
print(estaciones)
estaciones.add("OTOÑOVERANO")
print(estaciones)

# elmetodo in sirve para validad si un valr esta dentro de una coleccion de datos
print("OTOÑOVERANO" in estaciones)
# ESTO NO SE PUEDE HACER EN LOS CONJUNTOS
#print(estaciones[1])


#------------------------------------------------------------------------------------

# DICCIONARIOS => coleccion de elementos que estan INDEXADOS, que nosotros manejamos el mnombre de su llave

persona = {
   'id':1,
   'nombre':'Juancito',
   "relacion": "soltero",
   "fecha_nacimiento": "1992/08/04",
   "hobbies": [
       {
           "nombre":"Futbol",
           "conocimiento":"Intermedio"

       },
       {
           "nombre":"Drones",
           "conocimiento":"Basico"
       }
   ]
  

}
print(persona['nombre'])
print(persona['hobbies'][0]['conocimiento']) # en JS seria => persona.hobbies[0].conocimiento

persona['apellido'] = "Martinez"
# en python si la llave del diccionario no exite lanzara un error y hara que el programa no continue
# print(persona['sexo'])

persona.pop("id")
print(persona)



libro = {
    "nombre": "Harry Potter",
    "autor": "J.K. Rowling",
    "editorial": "Blablabla",
    "año": 2018,
    "idiomas": [
        {
            "nombre": "portuges"
        },
        {
            "nombre": "ingles",
            "nombre": "ingles britanico"
        },
        {
            "nombre": "frances"
        },
        {
            "nombre": "aleman"
        },
    ],
    "calificacion": 5,
    "imdb": "00asd12-asd878-a4s5d4a5-a45sd4a5sd",
    "tomos": ("La piedra filosofal", "La camara secreta", "El vuelo del fenix")
}
print(libro["año"])


# EJERCICIO 1
# devolver el autor del libro

print(libro["autor"])

# EJERCICIO 2
# devolver el segundo tomo

print(libro["tomos"][1])

# EJERCICIO 3
# devolver la catidad de idiomas del libro

print(len(libro["idiomas"]))

# EJERCICIO 4
# inidicar si esta o no esta el idioma ruso

# no se puede hacer sin un bucle