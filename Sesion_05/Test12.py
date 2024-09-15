'''Decoradores en Python'''

def funcionADecoradora(funcionB):

    def funcionC():
        print('1. Antes de ejecutar la función a decorar')
        funcionB()
        print('2. Después de ejecutar la función a decorar')
    return funcionC()


@funcionADecoradora
def saludo():
    print('Hola Python')