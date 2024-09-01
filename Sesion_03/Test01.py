lista0=[]
lista0.append(1)
lista0.append(2)
lista0.append(3)
print("Mi lista0 es {}".format(lista0))

lista1=['Argentina','Chile','Peru','Colombia']
print("Mi lista1 inicial es {}".format(lista1))
lista1.pop()
print("Ahora mi lista es la siguiente: {}".format(lista1))
lista1.pop(2)
print("Ahora mi lista es la siguiente: {}".format(lista1))

lista2=[40,68,77,190,355]
print("Mi lista2 inicial es {}".format(lista2))
lista2.insert(3,"abc")
print("Ahora mi lista es la siguiente: {}".format(lista2))

lista3=["Python","Java","PHP","Javascript","Typescript"]
print("Mi lista3 inicial es {}".format(lista3))
lista3.remove("PHP")
print("Ahora mi lista es la siguiente: {}".format(lista3))
lista3.remove("Java")
print("Ahora mi lista es la siguiente: {}".format(lista3))

lista4=["x","y","z","a","b","c"]
print("Mi lista4 inicial es {}".format(lista4))
lista4.clear()
print("Ahora mi lista es la siguiente: {}".format(lista4))

lista3=["python","java","php","javascript","typescript"]
print("Mi lista3 inicial es {}".format(lista3))
lista3.append("python")
lista3.append("NodeJS")
lista3.append("Python")
lista3.append("python")
print("Ahora mi lista es la siguiente: {}".format(lista3))
print("La cantidad de veces que se repite 'python' en la lista3 es {}".format(lista3.count("python")))

lista5=["Henry","Trujillo",57,"28/05/1967"]
print("Mi lista5 inicial es {}".format(lista5))
lista5.reverse()
print("Ahora mi lista es la siguiente: {}".format(lista5))

lista6=[1,2,3,4,5]
lista7=lista6.copy()
lista7.reverse()
lista7.append(10)
print("La lista6 original es la siguiente: {}".format(lista6))
print("La lista7 modificada es la siguiente: {}".format(lista7))

lista8=[]
lista8.append("Peru")
lista8.append("Brasil")
lista8.append("Argentina")
lista8.append("Colombia")
lista8.append("Chile")
print("Los valores de la lista8 son los siguientes: {}".format(lista8))
del lista8[2]
del lista8[3]
print("Ahora mi lista es la siguiente: {}".format(lista8))

lista9=["a","b","c","d","e","f","g"]
lista10=[1,2,3,4,5,6]
sumalista=lista9+lista10
print("El total de elementos de mi nueva lista es {}".format(sumalista))

listaa=[]
listab=[]
listaa.append('Henry')
listaa.append('57')
listaa.append('nutricionista')
print("La lista A es {}".format(listaa))
listab.append('Steve')
listab.append('46')
listab.append('ingeniero')
print("La lista B es {}".format(listab))
suma_edad=int(listaa[1])+int(listab[1])
print("La suma de las edades es {}".format(suma_edad))
suma_listas=listaa+listab
print("La nueva lista es {}".format(suma_listas))
suma_listas.remove('57')
suma_listas.remove('46')
print("Tras remover las edades, la lista es {}".format(suma_listas))