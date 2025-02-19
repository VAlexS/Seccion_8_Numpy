'''
Crea un DataFrame de Pandas llamado mi_dataframe con dos columnas: "Frutas" y "Cantidad".

La columna "Frutas" debe contener los valores "Manzana", "Banana" y "Cereza".

La columna "Cantidad" debe contener los números 5, 8 y 3 respectivamente.

Luego, convierte este DataFrame en un array de NumPy y guárdalo en una variable llamada array_frutas.
'''

import numpy as np
import pandas as pd

mi_dataframe = pd.DataFrame({
    'Frutas': ["Manzana", "Banana", "Cerveza"],
    'Cantidad': [5, 8, 3]
})



array_frutas = mi_dataframe.to_numpy()

print(array_frutas)

