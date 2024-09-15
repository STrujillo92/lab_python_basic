#Control o gestion de excepciones

'''
Crear una aplicación usando excepciones donde no se pueda
realizar la suma entre diferentes tipos de datos
'''

def operaciones(a,b):
    try:
        #resultado=a+b
        resultado=a/b
    except TypeError:
        print('No se puede sumar un string con un dato int.')
    except ZeroDivisionError:
        print('No se puede dividir entre cero.')
    else:
        print('Resultado: {}.'.format(resultado))

operaciones(40,'Lima')
operaciones(40,0)