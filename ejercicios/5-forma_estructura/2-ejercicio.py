'''
Crea un array bidimensional llamado: array_original de forma (2, 3) que contenga los primeros 6 números enteros positivos.
Utiliza el método correcto para cambiar sus filas por columnas. Almacenalo en una variable llamada array_modificado
'''

import numpy as np

array_original = np.array([[1, 2, 3],
                           [4, 5, 6]])

print(array_original)

print("array transpuesto")

array_modificado = array_original.transpose()

print(array_modificado)