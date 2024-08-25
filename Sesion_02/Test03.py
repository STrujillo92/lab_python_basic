var_1="7000"
var_2=35000
var_3=40.85

suma_1=int(var_1)+var_2+var_3
print(suma_1)

nombre="Samantha"
apellido="Trujillo"
nombre_completo=nombre + " " + apellido
print(nombre_completo)

suma_2=int(var_1)+var_2
print("El valor de mi suma_2 es: {}".format(suma_2))

suma_3=var_2+var_3
print("El valor de mi suma_3 es: {}".format(suma_3))

suma_4=var_1+str(var_2)+str(var_3)
print("El valor de mi suma_4 es: {}".format(suma_4))

resta_1=20-120
resta_2=3000-500
resta_3=200.98-5000-480

print("El tipo de dato de la resta_1 es: {}".format(type(resta_1)))
print("El tipo de dato de la resta_2 es: {}".format(type(resta_2)))
print("El tipo de dato de la resta_3 es: {}".format(type(resta_3)))

multiplica_1=9*1000
multiplica_2=90*9.9
multiplica_3=9.5*100.5

print("El valor de multiplica_1 es: {}".format(multiplica_1))
print("El valor de multiplica_2 es: {}".format(multiplica_2))
print("El valor de multiplica_3 es: {}".format(multiplica_3))

multiplica_4="\nHola mundo"
print(multiplica_4*3)

division_1=250/10
division_2=200.8/50
division_3=75.4/20.6
print("El valor de division_1 es: {}".format(division_1))
print("El tipo de dato de la division_1 es: {}".format(type(division_1)))
print("El valor de division_2 es: {}".format(division_2))
print("El tipo de dato de la division_2 es: {}".format(type(division_2)))
print("El valor de division_3 es: {}".format(division_3))
print("El tipo de dato de la division_3 es: {}".format(type(division_3)))

var_1=10%4
var_2=100%6
var_3=356%3
print("El valor de var_1 es: {}".format(var_1))
print("El valor de var_2 es: {}".format(var_2))
print("El valor de var_3 es: {}".format(var_3))

var_1=5
var_2=6
var_3=5**6
print("El valor de var_3 es: {}".format(var_3))
var_4=pow(var_1,var_2)
print("El valor de var_4 es: {}".format(var_4))

var_1=70
var_2=6
var_3=var_1//var_2
print("El valor de var_3 es: {}".format(var_3))

"""
Requisitos:
1. Crear 2 variables enteras, 2 variables flotantes, 1 variable string, 1 variable string con contenido numérico,
1 variable boolean
2. Obtener y mostrar la suma de una variable entera con la variable string numérica (realizar conversión necesaria)
3. Suma de las 2 variables enteras más la variable string numérica y la variable flotante
4. Obtener y mostrar el módulo de las 2 variables enteras %
5. Obtener y mostrar el resultado entero de las 2 variables enteras //
"""

var_1=100
var_2=8
var_3=10.5
var_4=3.1415
var_5="Python"
var_6="1000"
var_7=False

suma_1=var_1+int(var_6)
print("El valor de suma_1 es: {}".format(suma_1))
suma_2=var_1+var_2+int(var_6)+var_4
print("El valor de suma_2 es: {}".format(suma_2))
modulo_1=var_1%var_2
print("El valor de modulo_1 es: {}".format(modulo_1))
div_1=var_1//var_2
print("El valor de div_1 es: {}".format(div_1))
