from funciones import suma as opera_1, multiplica as opera_2

var1 = int(input("Ingrese el valor de la variable 1: "))
var2 = int(input("Ingrese el valor de la variable 2: "))

sum = opera_1(var1, var2)
print('La suma de {} y {} es {}.'.format(var1, var2, sum))

mul = opera_2(var1, var2)
print('La multiplicación de {} y {} es {}.'.format(var1, var2, mul))
