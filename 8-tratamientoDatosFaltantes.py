import numpy as np

array = np.array([1, 2, np.nan, 4, 5])
print(array)

print("Is NaN")

print(np.isnan(array))

print("Mean")

print(np.mean(array))

print("NanMean")

print(np.nanmean(array))

print("Array con 0")

array_con_0 = np.where(np.isnan(array), 0, array)

print(array_con_0)

print("Rellenar valor faltante con el Promedio")
promedio = np.nanmean(array)
array_con_promedio = np.where(np.isnan(array), promedio, array)

print(array_con_promedio)

print("Eliminar el promedio")
array_filtrado = array[~np.isnan(array)]
print(array_filtrado)