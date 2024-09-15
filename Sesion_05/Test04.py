'''
- Agregar un exepción donde se va a considerar una lista con 4 valores, todos sus datos serán string
- Al querer modificar una de las posiciones no existentes crear un nuevo índice y darle valor de "0"
- Mostrar la lista final
'''

l1=[]
for i in range(4):
    l1.append(input('Ingrese el valor a agregar en la lista: '))

def modificar():
    ind=int(input('Ingrese la posición a modificar en la lista: '))
    valor=input('Ingrese el valor a modificar en la lista: ')
    try:
        l1[ind]=valor
    except IndexError:
        print('Posición ingresada es inválida.')
        l1.append(valor)
        print('La lista resultante es: {}.'.format(l1))
    else:
        print('La lista resultante es: {}.'.format(l1))

modificar()
modificar()