"""GENERADO DE NUMEROS """
import random

# Crea una lista vacía para almacenar los números aleatorios.
numero_inicio = 2134567890
numero_final = 3999999999
cantidad_inicio = 1
cantidad_final = 602
numero = 0

# Crea un bucle que se ejecutará 100 veces:
for i in range(cantidad_final):
    numero = random.randint(numero_inicio, numero_final)
    cantidad_final =+ 1
    print(numero)
     

# Imprime la lista de números aleatorios.
  