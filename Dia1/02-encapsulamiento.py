class Vehiculo:
    def __init__(self, largo,ancho,motor,enMarcha=False):
        self.largo = largo
        self.ancho = ancho
        self.motor = motor
        self.enMarcha = enMarcha
        #si deseamos que el artributo sea privado(solamente puede ser accedido dentro de la propia clase tendremos que solocar el doble sub gruion antes de definir su nombre, y si por el contrario, queremos que sea publico, no colocaremos el doble sub guion)
        self.__ruedas = 4

    def encender(self, estado =True):
        self.enMarcha = estado
        chequeo = self.__chequeo_interno()
        if chequeo == True:
            return "el coche esta listo"
        else:
            return "El coche tiene problemas para encender"


    def __chequeo_interno(self):
        """Metodo que solamente se podra ejecutar dentro de la misma clase y no fuera de ella ni tampoco ser accedida """
        self.gasolina =90
        self.aceite ="ok"
        self.temperatura =20
        self.kilomatraje =192956
        if(self.gasolina > 20 and self.aceite =="ok" and self.temperatura <80 and self.kilomatraje <10000000):
            return True
        else:
            return False

#objeVehiculo = Vehiculo(4.50,1.80,3000)
#print(objeVehiculo.largo)

#print (objeVehiculo.encender())
#print(objeVehiculo.enMarcha)

#bjeVehiculo.__chequeo_interno()


class Persona:
    def __init__(self, nombre,apellido,correo,passoword):
        self.nombre = nombre
        self.apellido =apellido
        self.correo =correo
        self.passoword =self.__encriptar_passoword(passoword)

    def __encriptar_passoword(self, passoword):
        return "sefdffgfkjhgfkhh" + passoword + "fdfdfgfg"

objePersona =Persona("Eduardo","De Rivero", "ederiveroman@gmail.com","123456")

print(objePersona.passoword)
#objePersona.__encriptar_passoword("Hola mundo")  # es para que no pueda acceder