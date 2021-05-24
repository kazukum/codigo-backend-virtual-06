
#metodo que sirve para ingresar datos por la terminal
edad = input("Ingresa tu edad: ")
print(type(edad))

# para convertir datos simplemente indicamos a que tipo de dato queremos convertir,
#y si se puede se realizara exitosamente, sino, lanzara un error
edadEntero = int(edad)
print(type(edadEntero))
edad = int(input("Ingresa otra vez tu edad: "))