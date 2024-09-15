#Uso de librería de fecha y tiempo

from datetime import datetime

str_date='2/6/2024'

'''
d:días
m:mes
y:año
'''

conversion=datetime.strptime(str_date,'%m/%d/%Y')
print(conversion)

'''Traer el mes de la fecha en letras'''

conversion_mes=datetime.strftime(conversion,'%d %b del %Y')
print(conversion_mes)
#donde b reemplaza a m para mostrar mes de forma literal