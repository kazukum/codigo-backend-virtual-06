# Operadores de comparacion
# == es igual que / en python no hay el triple doble igual es para javascript 
# ≠  diferente que
# <, >, menor que, mayor que
# <=, >=, mnor o igugal que, mayor o igual que

numero1, numero2 = 10, 20
print(numero1 < numero2)

# if(persona < 18 // nacionalidad == "colombiano"){...}

# operadores logicos

# and (en JS es &&) => sirve para validar que la dos condiciones sean verdaderas
# if (condicion1 AND condicion2  AND condicion3){ingresara si todas son verdaera}

# or (en JS es //) => sirve para validad que al menos una de las condiciones sea verdadera
# if(condicion1 OR condicion2  condicion3){ingresara si al menos una es verdadera}

#not (en JS es !) => invierte el resultado

print((10>5) and (10>11)) # retorna V y F entonces todo seria Falso
print((10 >= 10) or (10>11)) # retorna V o F entonces todo seria verdadero
print(not(10 >= 10) or (10>20)) # retorna si es V aora es F resultado todo es falso

# operadores de identidad
# is => es 
# is not => no es
# sirve para ver si estan apuntando a la misma direccion de memoria

frutas =['MANZANA', 'PERA']
frutas2 = frutas
print(frutas is frutas2)


# dos tipos de variables => variables MUTABLES y las variables INMUTABLES
# mutables => es cuando nosotros hacemos una copia de esa variable, la copia tambien se esta alojando en el mismo espacio de memoria
# listas, tuplas, diccionarios, conjuntos

# imnutables => es cuando hacemos una copia esta copia se alojara en otra posicion de memoria
# son => string, int, boolean, etc

nombres =['eduardo','raul', 'carlos', 'estefani']
nombres_alumnos = nombres
nombres_alumnos[0]= ['carmen']

nacionalidad = "ecuatoriana"
nacionalidad2= nacionalidad
nacionalidad2= "brazileña"
print(nombres)
print(nacionalidad)
print(nacionalidad is nacionalidad2)
print(nombres is nombres_alumnos)

# sirve para poder ubicar el identificador unico de esa variable en todo el compilador de python
print(id(nombres))
