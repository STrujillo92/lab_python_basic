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

#Instanciamos nuestra clase
carro1=Carro('azul',70)
print('La velocidad de mi primer carro es: {}.'.format(carro1.velocidad))
carro1.acelerar()
carro1.acelerar()
carro1.acelerar()
carro1.acelerar()
print('La nueva velocidad de mi primer carro es: {}.'.format(carro1.velocidad))
carro1.frenar()
carro1.frenar()
print('La velocidad actual de mi primer carro es: {}.'.format(carro1.velocidad))