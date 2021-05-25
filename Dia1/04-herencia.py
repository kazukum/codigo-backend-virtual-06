class Vehiculo:
    def __init__(self,marca,modelo, numero_ruedas, acelera= False):
        self.marca = marca
        self.modelo = modelo
        self.ruedas = numero_ruedas
        self.acelera=acelera

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.acelera = False

    def estado(self):
        return "Marca: {} \n Modelo: {} \n Aceleracion: {} \n Ruedas: {} ".format(
            self.marca,self.modelo,self.acelera, self.ruedas)


class Auto(Vehiculo):
    def __init__(self, marca, modelo, turbo):
        #el metodo super sirve para pasar los atriburos al padre del cual se esta haciendo la herencia
        super().__init__(marca, modelo, 4)
        self.turbo = turbo

    def derrape(self):
        return "Estoy derrapando"


class Camion(Vehiculo):
    def __init__(self, marca, modelo, doble_corona, acelera = False):
        super().__init__(marca, modelo,8,acelera)
        self.doble_corona = doble_corona

    def cargar(self, cargar):
        #Indicar si el camion tiene doble corona: El camion de marca xxxx y modelo xxx tiene doble corona y carga xxx toneladas
        #si no tiene: El camion de marcar xxx y modelo xxx no tiene doble corno y solo carga xxx toneladas
        
        if self.doble_corona :
            return "El camion de marca {} y modelo {} tiene doble corona y carga {} tonaladas".format(self.marca, self.modelo,cargar)
        else:
            return "El camion de marca{}  y modelo {} no tiene doble corona y solo carga {}".format(self.marca, self.modelo,cargar)
            
           
     
objetAuto = Auto ("Hyundai","Accent", False)
objCamion = Camion("Volvo","F100",True, True)
 
print(objetAuto.estado())
print(objCamion.estado())

        