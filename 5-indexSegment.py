import numpy as np

def separar():
    print("_________________________\n")

array1d = np.array([1, 2, 3, 4, 5])

array2d = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

print(array1d[0])

print(array1d[-1])

print(array2d[0])

print(array2d[1][2])

print(array1d[1:4])

print(array2d[1, :])

print(array2d[1, 1:3])

#quiero obtener la columna del medio

print(array2d[:, 1])

#quiero obtener los 2 primeros numeros de las primeras 2 filas

print(array2d[:2, :2])

#indexacion booleana

print(array1d > 3)

print(array2d % 2 == 0)