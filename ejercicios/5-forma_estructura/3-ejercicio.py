'''
Crea un array de 2 dimensiones array_original de forma (2, 3) que contenga los primeros 6 números enteros positivos. Identico al del ejercicio anterior.
Luego, crea una copia aplanada de este array y almacénalo en una variable llamada array_aplanado
'''

import numpy as np

array_original = np.array([[1, 2, 3],
                           [4, 5, 6]])

print("array original")

print(array_original)

print("array aplanado")

array_aplanado = array_original.flatten()

print(array_aplanado)



