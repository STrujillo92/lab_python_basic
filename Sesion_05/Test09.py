from datetime import datetime

'''Uso del método timestamp'''

time_now=datetime.strptime('2024/05/02 20:30:00','%Y/%m/%d %H:%M:%S').timestamp()
print(time_now)

#timestamp convierte la fecha en segundos.
