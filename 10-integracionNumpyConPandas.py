import numpy as np
import pandas as pd

df = pd.DataFrame({
    'Impares': [1, 3, 5],
    'Pares': [2, 4, 6]
})

print("df")

print(df)

print("Array_np1")

array_np1 = df.values

print(array_np1)

print("array_np2")

array_np2 = df.to_numpy()

print(array_np2)

print("Raiz cuadrada")

print(np.sqrt(df))

print("Maximo")

print(np.max(array_np2))

print("Minimo")

print(np.min(array_np2))

print("df desde np")

df_desde_np = pd.DataFrame(array_np1)

print(df_desde_np)

print("df desde np con columnas")

df_desde_np = pd.DataFrame(array_np1, columns=['Col1', 'Col2'])

print(df_desde_np)