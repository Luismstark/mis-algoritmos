"""GENERADOR DE FECHA ALEATORIA"""


import random
from datetime import datetime, timedelta

# Establecer el rango de fechas
fecha_inicio = datetime(2022, 12, 1)
fecha_fin = datetime(2023, 3, 1)

# Generar una lista de 210 fechas aleatorias
fechas_aleatorias = []
for i in range(602):
    delta = fecha_fin - fecha_inicio
    dias_desde_inicio = random.randint(0, delta.days)
    fecha_aleatoria = fecha_inicio + timedelta(days=dias_desde_inicio)
    fechas_aleatorias.append(fecha_aleatoria)

# Ordenar la lista de fechas de manera ascendente
fechas_aleatorias.sort()

# Imprimir la lista de fechas ordenadas
for fecha in fechas_aleatorias:
    print(fecha.strftime("%d/%m/%Y"))
    