'''
Crea un array de NumPy llamado mi_array con dos columnas y tres filas.

    1) La primera columna debe contener los números 10, 20 y 30.

    2) La segunda columna debe contener los números 40, 50 y 60.


Convierte este array en un DataFrame de Pandas llamado df_numeros y asigna los nombres "Decenas" y "Centenas" a las columnas.
'''

import numpy as np
import pandas as pd

mi_array = np.array([[10, 40],
                     [20, 50],
                     [30, 60]])

df_numeros = pd.DataFrame(mi_array, columns=['Decenas', 'Centenas'])

print(df_numeros)