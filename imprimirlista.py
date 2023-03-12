
""" Escriba una programa que tome como entrada 
una lista de numeros enteros y calcule la suma de los numeros pares de la lista. Luego imprima  la suma en la consola."""


def suma_pares(lista):
    suma = 0
    for num in lista:
        if num % 2 == 0:
            suma += num
    return suma

lista_de_numeros = [1,2,3,4,5,6,7,8,9,10]

resultado = suma_pares(lista_de_numeros)

print(resultado) 
print('-------------------------------------------')

"""esta funcion imprime numeros en la consola"""
def numero(i,f,c):
    
    for num in range(i,f,c):
        print(num)

numero(0,200,2)

print('-------------------------------------------')

"""y esta funcion devuelve el valor de una lista"""

def numero2(i,f,c):
    lista = []
    for num in range(i,f,c):
        lista.append(num)
    return lista

la_lista = numero2(0,200,2)
print(la_lista)