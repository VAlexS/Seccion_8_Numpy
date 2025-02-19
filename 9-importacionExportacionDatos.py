import numpy as np


print("IMPORTACION DE DATOS")
array = np.genfromtxt("medallas.csv", delimiter=",", filling_values=0, skip_header=1, dtype=int)
print(array)

print("EXPORTACION DE DATOS")

array_ejemplo = np.array([[1, 2, 3],
                          [4, 5, 6]])

np.savetxt("arrayAlmacenado.csv", array_ejemplo, delimiter=',', fmt='%d')