"""
Requisitos:

1. Crear variables para los valores de nombre, profesión y ciudad
2. Crear 2 variables de remuneración de enero y febrero
3. Crear 1 variable donde se sumará el ingreso de enero y febrero
4. Mostrar en pantalla el mensaje de:
"Hola soy nombre, mi profesión es profesión y mi remuneración acumulada es 'remuneración total'"

"""

nombre="Samantha"
profesion="ingeniera"
ciudad="Lima"
rem_ene=1500
rem_feb=2000
rem_tot=rem_ene+rem_feb
print("Hola soy {}, mi profesión es {} y mi remuneración acumulada es {}".format(nombre,profesion,rem_tot))

nombre="Samantha"
ciudad="Lima"
saldo=4000
empresa=False
correo=""
empleado=[nombre,saldo,empresa,ciudad]
print("Tipo de dato para la variable 'saldo' es: {}".format(type(saldo)))
print("Tipo de dato para la variable 'empresa' es: {}".format(type(empresa)))
print("Tipo de dato para la variable 'nombre' es: {}".format(type(nombre)))
print("Tipo de dato para la variable 'ciudad' es: {}".format(type(ciudad)))
print("Tipo de dato para la variable 'empleado' es: {}".format(type(empleado)))
print("Tipo de dato para la variable 'correo' es: {}".format(type(correo)))

varstr="2024"
nombre="Samantha"
modulo=1
print(int(varstr))
varint=int(varstr)
print(type(varint))
varmod=str(modulo)
print(type(varmod))
print(varmod)

