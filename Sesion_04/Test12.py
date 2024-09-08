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
carro1=Carro('Blanco',60)
print('El color del primer carro es: {}.'.format(carro1.color))
carro2=Carro('Rojo',80)
#Asignar un nuevo atributo a una instancia en particular
carro2.marchas=30000
print('El número de marchas del segundo carro es: {}.'.format(carro2.marchas))