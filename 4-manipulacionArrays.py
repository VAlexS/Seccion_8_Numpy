import numpy as np


def separar():
    print("_____________________________\n")


x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]

array_concatenado = np.concatenate([x, y, z])

print("array contatenado")

print(array_concatenado)

separar()

a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]

array_concatenado_vertical = np.concatenate([a, b], axis=1)

print("array concatenado vertical")

print(array_concatenado_vertical)

separar()

array_concatenado_horizontal = np.concatenate([a, b], axis=0)

print("array concatenado horizontal")

print(array_concatenado_horizontal)

separar()

print("array reformado")

array_reformado = array_concatenado_horizontal.reshape(2, 4)
print(array_reformado)

separar()

array_multi = array_reformado * array_reformado

print(array_multi)

separar()

raices = np.sqrt(array_multi)
