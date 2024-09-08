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
carro1=Carro('negro',60)
print('El color del primer carro es: {}.'.format(carro1.color))
print('La acelaración del primer carro es: {}.'.format(carro1.aceleracion))
print('La cantidad de ruedas que tiene el primer carro es: {}.'.format(carro1.ruedas))

carro2=Carro('azul',80)
print('El color del segundo carro es: {}.'.format(carro2.color))
print('La acelaración del segundo carro es: {}.'.format(carro2.aceleracion))
print('La cantidad de ruedas que tiene el segundo carro es: {}.'.format(carro2.ruedas))
