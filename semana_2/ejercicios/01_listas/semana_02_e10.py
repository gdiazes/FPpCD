Ejercicio 10: Listas Anidadas (Nivel 1)
Objetivo: Trabajar con listas anidadas (matrices).
Código con errores:
pythonCopiarmatriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
elemento = matriz[1][3]
matriz[0, 0] = 10
fila_plana = matriz[0] + matriz[1] + matriz[3]
print(f"Elemento seleccionado: {elemento}")
print(f"Matriz modificada: {matriz}")
print(f"Lista plana: {fila_plana}")
Pistas:

Los índices en Python comienzan en 0 y deben estar dentro del rango de la lista.
El acceso a matrices requiere índices separados [i][j], no [i, j].
Asegúrate de que los índices que estás utilizando existan.