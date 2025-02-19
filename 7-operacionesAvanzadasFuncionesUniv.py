import numpy as np

print("array 1")

array1 = np.array([1, 2, 3])

print(array1)

print("array 2")

array2 = np.array([[0], [10], [20], [30]])

print(array2)

print("broadcast suma")

broadcast_suma = array2 + array1

print(broadcast_suma)

print("broadcast multiplicacion")

broadcast_multi = array2 * array1

print(broadcast_multi)

print("Suma a y b con add")

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

suma = np.add(a, b)

print(suma)

print("Resta a y b con substract")

resta = np.subtract(a, b)

print(resta)

print("Multiplicar a y b con multiply")

multiplicacion = np.multiply(a, b)

print(multiplicacion)

print("Division a y b con divide")

division = np.divide(b, a)

print(division)

print("Exponencial de a")

exponencial = np.exp(a)

print(exponencial)

print("Logaritmos de a")

logaritmos = np.log(a)

print(logaritmos)

print("Logaritmo de a en base a 10")

logaritmos = np.log10(a)

print(logaritmos)

print("Raiz cuadrada de a")

raiz_cuadrada = np.sqrt(a)

