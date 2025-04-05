### Ejercicio 4: Acceso a Elementos de una Tupla (Nivel 5)
#**Objetivo:** Acceder correctamente a los elementos de una tupla.

#**Código con errores:**
#```python
coordenadas = (10, 20, 30)
print(coordenadas)
print("La coordenada x es: " + str(coordenadas[0]))
print("La coordenada z es: " + str(coordenadas[2]))
print("Las primeras dos coordenadas son: " + str(coordenadas[0:2]))
#

#**Pistas:**
#- Los índices en Python comienzan en 0.
#- Para convertir números a strings en concatenación, necesitas usar una función específica.
#- El slicing en Python incluye el primer índice pero excluye el último.
