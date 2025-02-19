'''
Crea un array bidimensional A de forma 2x2 que contenga los números del 1 al 4.

Crea otro array bidimensional B de la misma forma que contenga los números del 5 al 8.

Realiza las siguientes operaciones e imprime los resultados:

    1) La suma de A y B. Almacena el resultado en una variable llamada suma_AB

    2) El producto elemento a elemento de A y B. Almacena el resultado en una variable llamada productoAB
'''
import numpy as np

def separar():
    print("__________________________________\n")

A = np.array([[1, 2], [3, 4]])

B = np.array([[5, 6], [7, 8]])

print("A")

print(A)

separar()

print("B")

print(B)

separar()

suma_AB = A + B

print("Suma A y B")

print(suma_AB)

separar()

productoAB = A * B

print("Producto A y B")

print(productoAB)