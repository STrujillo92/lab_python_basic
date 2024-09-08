#Condicional if
var1=4
if var1>=5:
    print('{} es mayor o igual a 5.'.format(var1))
else:
    print('{} es menor o igual a 5.'.format(var1))

var1=int(input('Ingresa tu edad: '))
if var1<18:
    print('Eres menor de edad.')
elif var1<65:
    print('Eres mayor de edad.')
else:
    print('Eres un adulto mayor.')

var1,var2,var3=80,150.6,'Python'
if var1==50 and var2>40.0 or var3=='Python':
    print('Se cumple al menos una de las condiciones.')
else:
    print('No se cumple ninguna de las condiciones.')