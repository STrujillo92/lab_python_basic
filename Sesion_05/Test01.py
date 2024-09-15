'''Manejo de errores'''

#Tipo de error: división entre 0
#var1=500/0

#Tipo de error: suma de tipos de datos diferentes
#suma=100+'hola'

"""
TypeError
ZeroDivisionError
IndexError
KeyError
FileNotFoundError
ImportError
OverflowError
"""

'''
Estructura y uso
try:
    bloque código 1
except 'excepción 1':
    bloque código 2
else:
    bloque código 3
'''

def division(a,b):
    try:
        resultado=a/b
        print('Datos válidos')
    except ZeroDivisionError:
        print('No es posible dividir entre 0.')
        resultado=None
        print('Resultado: {}.'.format(resultado))
    else:
        print('Resultado: {}.'.format(resultado))

division(1000,5)
division(400,0)
division(2,500)