'''
    - Crear una función aplicando exepciones donde el bloque del except
    va a considerar a los errors de división entre cero y el tipo de error
    - Los valores tienen que ser ingresados por consola
'''

def operaciones():
    a = input('Ingrese un valor para a:')
    b = input('Ingrese un valor para b:')
    try:
        a = float(a)
        b = float(b)
        suma = a + b
        division = a / b
        print('Datos ingresados son válidos.')
    except ValueError:
        print('Uno o más de los datos ingresados no es int o float. Corregir.')
    except ZeroDivisionError:
        print('Su segundo número no puede ser 0. División entre cero no es posible.')
    else:
        print('La suma de {} y {} es: {}.'.format(a,b,suma))
        print('La division de {} entre {} es {}.'.format(a,b,division))

operaciones()
operaciones()
operaciones()