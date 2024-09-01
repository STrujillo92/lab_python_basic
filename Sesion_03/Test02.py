dicci1={'nombre':'Lucy','edad':54,'promedio':15}
print("El dicci1 tiene el siguiente contenido {}".format(dicci1))
dicci1['distrito']='Lince'
dicci1['habilitado']=True
print("Ahora dicci1 tiene el siguiente contenido {}".format(dicci1))

del dicci1['edad']
del dicci1['distrito']
print("Ahora dicci1 tiene el siguiente contenido {}".format(dicci1))

dicci2={'nombre':'Mysql','tipo':'BD relacional'}
keys=sorted(dicci2)
values=sorted(dicci2.values())
print("El dicci2 tiene el siguiente contenido {}".format(dicci2))
print("Las claves de dicci2 son {}".format(keys))
print("Los valores de dicci2 son {}".format(values))

lista1=list(dicci2)
lista2=list(dicci2.values())
lista3=list(dicci2.items())
print("El diccionario convertido en lista es {}".format(lista1))
print("El diccionario convertido en lista es {}".format(lista2))
print("El diccionario convertido en lista es {}".format(lista3))