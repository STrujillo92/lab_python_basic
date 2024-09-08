#Programación orientada a objetos
class Carro:
    #atributos
    ruedas=4
    #Constructor: valores que van a tener por defecto mi clase, que se le instancia a una variable
    def __init__(self,color,aceleracion):
        self.color=color
        self.aceleracion=aceleracion
        self.velocidad=0
    #Métodos: Son las funciones de la clase
    def acelerar(self):
        self.velocidad=self.velocidad+self.aceleracion
    def frenar(self):
        velocidad=self.velocidad-self.aceleracion
        if velocidad<0:
            self.velocidad=0
        self.velocidad=velocidad

#Aplicando herencia, se crea la clase hija
class CarroVolador(Carro):
    ruedas=6
    def __init__(self,color,aceleracion,estado_volando=False):
        super().__init__(color,aceleracion)
        self.color=color
        self.aceleracion=aceleracion
        self.estado_volando=estado_volando
    def vuela(self):
        self.estado_volando=True
    def aterriza(self):
        self.estado_volando=False

carro1=Carro('Rojo',55)
carro_vol1=CarroVolador('Blanco',65)
print('El color del carro volador es: {}'.format(carro_vol1.color))
print('El estado de la velocidad de mi carro volador es: {}'.format(carro_vol1.aceleracion))
carro_vol1.vuela()
carro_vol1.acelerar()
carro_vol1.acelerar()
print('La nueva velocidad del carro volador es: {}.'.format(carro_vol1.velocidad))



