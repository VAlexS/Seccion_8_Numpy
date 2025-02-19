import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

print("array original")

print(array)

print(array.shape)

array_mod = array.reshape(3, 3)

print("array resimensionado (3, 3)")

print(array_mod)

print("array redimensionado (-1, 3)")

array_mod2 = array.reshape(-1, 3)

print(array_mod2)

print("array transpuesto")

array_volteado = array_mod2.transpose()
print(array_volteado)

print("array chato")

array_chato = array_mod.flatten()

print(array_chato)

print("array ravel")

array_ravel = array_mod.ravel()
print(array_ravel)

