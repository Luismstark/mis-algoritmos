"""REALIZARE UN PAR DE EJEMPLOS CON EL BUCLE  WHILE"""


def suma(n):
    lista = []
    suma = 0
    inicio = 1
    while inicio <= n:
        suma += inicio
        inicio += 1
        lista.append(suma)
    print(lista)
suma(100)


"""contar ocurrencias de un valor en una lista"""


def ocurrencias(lista, valor):
    num_de_ocurrencias = 0 # es la cantidad de veces que aparece el valor
    i = 0 
    while i < len(lista):

        if lista[i] == valor:
            num_de_ocurrencias += 1
        i += 1
    print(num_de_ocurrencias)

valor = 2 # cuantas de este valor encuentra en la lista
lista = [1,23,5,6,2,3,2,3,2,3,2,3,7,8,9,1,1,2,3,4,5,6,677,8,9,]
ocurrencias(lista,valor) 


"""
creare un algoritmo, mientras tengo dinero compro y si no tengo trabajo, mi saldo inicial es de 30
"""

def mientras_tengo_dinero():
    saldo = 30
    total = 0
    while total <= saldo:
        print("compra, compra")
        if saldo == 0:
            print("trabaja para ganar dinero")
        saldo -= 1

mientras_tengo_dinero()