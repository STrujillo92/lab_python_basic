#Control de flujo con FOR
ingenierias=['software','sistemas','industrial','quimica','mecánica','mecatrónica']
print('El tamaño de la lista de ingenierias es {}.'.format(len(ingenierias)))
i=0
for ingenieria in ingenierias:
    print(ingenieria)
    i=i+1
    print('Valor de i: {}.'.format(i))