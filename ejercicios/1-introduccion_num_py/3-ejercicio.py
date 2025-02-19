'''
Se te ha proporcionado un dataset que contiene información sobre varias ciudades, incluyendo su población y el número de visitantes anuales.
Este dataset está representado en el siguiente DataFrame de Pandas

Encuentra el valor máximo de visitantes usando el método adecuado de numpy, y almacena este valor en una variable llamada: max_visitantes
'''

import numpy as np
import pandas as pd

def separar():
    print("___________________________________\n")


datos = {
    "Ciudad": ["Ciudad de México", "Buenos Aires", "Río de Janeiro", "Lima", "Bogotá", "Santiago de Chile", "São Paulo", "La Habana", "Cancún", "Cartagena"],
    "País": ["México", "Argentina", "Brasil", "Perú", "Colombia", "Chile", "Brasil", "Cuba", "México", "Colombia"],
    "Población": [9265833, 3059574, 6748314, 9756020, 7181663, 6199241, 12333146, 2164182, 888124, 1036671],
    "Visitantes": [21000000, 15000000, 13000000, 9000000, 8000000, 7500000, 20000000, 4000000, 5000000, 3000000]
}

df = pd.DataFrame(datos)

print(df)

separar()

print("Numero maximo de visitantes")

max_visitantes = np.max(df["Visitantes"])

print(max_visitantes)