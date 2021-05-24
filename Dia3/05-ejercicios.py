# ejemplo:
# Para evitar que en cada impresion se ejecute en una nueva linea, se puede agregar el parametro end y este indicara como queremos que actue al finalizar la linea, su valor por defecto es \n, pero si le cambiamos a * entonces, al finalizar la impresion, colocara un asterisco en vez de un salto de linea
#for numero in range(5):
 #   print(numero, end="*")

# Escriba una funcion que le pida al usuario ingresar la altura y el ancho de un rectangulo y
# que lo dibuje usando *, ejemplo:
# altura: 5
# ancho: 4
# Resultado:
# ****
# ****
# ****
# ****
# ****

#anchura = int(input("Ingrese Altura del rectangulo: "))
#altura = int(input("Ingrese Anchura del rectangulo: "))


#for i in range(anchura):
#    for j in range(altura):
#        print("* ", end="")

#    print()

 
def rectangulo(ancho, alto):
    for A in range(alto):
        for B in range(ancho):
            print("* ", end="")
        print()

anchura = int(input("Anchura del rectángulo: "))
altura = int(input("Altura del rectángulo: "))
rectangulo(anchura, altura)


#---------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------


# Escribir una funcion que nosotros le ingresemos el lado de un octagono y que lo dibuje
# Ejemplo:
# Lados: 5
#       *****
#      *******
#     *********
#    ***********
#   *************
#   *************
#   *************
#   *************
#   *************
#    ***********
#     *********
#      *******
#       *****








n = int(input("Ingrese el numero para el OCTOGONO: "))



for  i in range(n+1):
   for j in range(n-i):
       print(" ", end ="")
   for k in range(2*i-1):
        print("*",end="")
   print("")
   
for  i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print("")   





#---------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------

# De acuerdo a la altura que nosotros ingresemos, nos tiene que dibujar el triangulo
# invertido
# Ejemplo
# Altura: 4
# ****
# ***
# **
# *


#---------------------------------------------------------------
# triangulo parado
#def triangulo(lad):
#    for i in range(lad):
#        print("* " * i)
#    print()    

#lados = int(input("Introduca el numero"))
#triangulo(lados)

#------------------------------------------------------------


#----------------------------

#num = 10
#for i in range(num,0,-1):
#    for j in range(i):
#        print("* ",end="")

#   print("-") 

#----------------------------





def triangulo(lado):
    for i in range(lado,0,-1):
        for j in range(i):
            print("* ", end="")

        print()

lados_triangulo = int(input("Ingrese el Lado del triangulo: "))
triangulo(lados_triangulo)        









# Ingresar un numero entero y ese numero debe de llegar a 1 usando la serie de Collatz
# si el numero es par, se divide entre dos
# si el numero es impar, se multiplica por 3 y se suma 1
# la serie termina cuando el numero es 1
# Ejemplo 19
# 19 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 12



def collatz(num):
    sec =[num]
    while num  > 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
        
        sec.append(num)

    return sec 

secuencia = collatz(int(input("ingresa el numero: ")))

for i in secuencia:
    print(i, end=" ")

# Una vez resuelto todos los ejercicios, crear un menu de seleccion que permita escoger
# que ejercicio queremos ejecutar hasta que escribamos "salir" ahi recien va a terminar
# de escoger el ejercicio


