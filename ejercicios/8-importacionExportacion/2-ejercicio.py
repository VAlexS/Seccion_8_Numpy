'''
Dado el archivo 'datos.csv'

Utiliza la función de NumPy correcta para importar los datos que contienen solo números. Asegúrate de que el delimitador utilizado en el archivo sea una coma (,)

Asegurate de que se ignoren los encabezados de columna.

Guarda los datos importados en una variable llamada datos.
'''

import numpy as np


datos = np.genfromtxt("datos.csv", delimiter=",", filling_values=0, skip_header=1, dtype=int, usecols=(0, 1, 2, 3))

print(datos)