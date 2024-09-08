#Uso de if ternarios
estado=1
'''Aplicamos la forma ternaria'''
'''
if estado==1:
    print('1. Su estado final es terminado.')
else:
    print('2. Su estado final es no terminado.')
'''
final='1. Su estado final es terminado.' if estado==1 else '2. Su estado final es no terminado.'
print(final)

sueldo=int(input('Ingrese su sueldo: '))
if sueldo>3500:
    print('Su sueldo no tiene bonificación.')
else:
    sueldof=sueldo*1.2
    print('Su sueldo tiene bonificación este año y la base más la bonificación es de {} soles.'.format(sueldof))
