'''
Crea un DataFrame de Pandas llamado mi_dataframe con dos columnas: "Frutas" y "Cantidad". Identico al ejercicio anterior.

La columna "Frutas" debe contener los valores "Manzana", "Banana" y "Cereza".

La columna "Cantidad" debe contener los números 5, 8 y 3 respectivamente.

Luego, filtra las filas donde la cantidad sea mayor a 4, almacena el resultado en una variable llamada: mi_dataframe_filtrado

Convierte el resultado en un array de NumPy. Guarda el array resultante en una variable llamada array_filtrado

En esta lección podrás recordar como filtrar datos en Pandas:

Flitrado de series en Pandas (https://www.udemy.com/course/python-para-data-science/learn/lecture/41885350/?instructorPreviewMode=instructor_v4#questions)
'''

import numpy as np
import pandas as pd


def filtrarSeries(serie, condicion: bool):
    return serie[condicion]


def filtrarDataframes(dataframe, condicion: bool):
    return dataframe[condicion]


mi_dataframe = pd.DataFrame({
    'Frutas': ["Manzana", "Banana", "Cerveza"],
    'Cantidad': [5, 8, 3]
})

print(mi_dataframe)

print("Dataframe filtrado")

mi_dataframe_filtrado = filtrarDataframes(mi_dataframe, condicion=mi_dataframe['Cantidad'] > 4)

print(mi_dataframe_filtrado)

print("array filtrado")

array_filtrado = mi_dataframe_filtrado.to_numpy()

print(array_filtrado)
