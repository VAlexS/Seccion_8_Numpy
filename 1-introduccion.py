import numpy as np
import pandas as pd

def separar():
    print("___________________________________\n")

df = pd.read_csv("Ciudades_Visitadas_Latinoamerica_2023.csv")

print(df)

separar()

promedio_poblacion = df['Población'].mean()

print(promedio_poblacion)

separar()

promedio_poblacion_redondeado = np.round(promedio_poblacion)

print(promedio_poblacion_redondeado)

separar()

visitantes_minimos = np.min(df['Visitantes'])

print(visitantes_minimos)

separar()

visitantes_maximos = np.max(df['Visitantes'])

print(visitantes_maximos)

separar()

