nom=input('Ingrese su nombre: ')
apel=input('Ingrese su apellido: ')
nombrec=nom+' '+apel
print('El tamaño del nombre completo, incluida la separación es: {}'.format(len(nombrec)))
print('El nombre completo en mayúsculas es: {}'.format(nombrec.upper()))
if len(nom)<len(apel):
    print('La longitud del nombre es menor a la del apellido.')
elif len(nom)==len(apel):
    print('La longitud del nombre es igual a la del apellido.')
else:
    print('La longitud del nombre es mayor a la del apellido.')