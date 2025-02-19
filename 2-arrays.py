import time

import numpy as np
import pandas as pd


def separar():
    print("___________________________________\n")


array = np.array([1, 2, 3, 4, 5])

print(array)

print(type(array))

separar()

lista_grande = list(range(1000000))

array_grande = np.array(lista_grande)

separar()

print(type(lista_grande))

print(type(array_grande))

separar()

inicio_lista = time.time()

for i in lista_grande:
    cuadrado = i ** 2

fin_lista = time.time()

print("Tiempo lista: ", fin_lista-inicio_lista)

separar()

inicio_array = time.time()

array_grande ** 2

fin_array = time.time()

print("Tiempo array: ",fin_array-inicio_array)


