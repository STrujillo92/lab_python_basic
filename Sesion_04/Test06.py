from django.template.defaultfilters import upper, lower

mi_cadena='Machine Learning con Python'
print('Mi cadena en mayúsculas es: {}'.format(mi_cadena.upper()))
print('Mi cadena en minúsculas es: {}'.format(mi_cadena.lower()))
print('Mi cadena en forma de título es: {}'.format(mi_cadena.title()))

cade1='Conexión a base de datos Python'
cade2=cade1.replace(cade1[0:8],'Nueva conexión')
print(cade2)

cade3='Conexión a base de datos con Python   '
cade4=cade3.rstrip()
print(len(cade3))
print(len(cade4))

cade5='     Hola Python'
cade6=cade5.lstrip()
print(cade6)

cade7='Samantha Michelle Trujillo Cortez'
cade8=cade7.split() #hace una lista con cada palabra
print(cade8)

for palabra in cade8:
    print(palabra)