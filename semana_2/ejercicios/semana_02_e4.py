### Ejercicio 1: Acceso a Elementos de una Tupla (Nivel 5)
**Objetivo:** Acceder correctamente a los elementos de una tupla.

**Código con errores:**
```python
coordenadas = (10, 20, 30)
print("La coordenada x es: " + coordenadas[0])
print("La coordenada z es: " + coordenadas[3])
print("Las primeras dos coordenadas son: " + coordenadas[0:1])
```

**Pistas:**
- Los índices en Python comienzan en 0.
- Para convertir números a strings en concatenación, necesitas usar una función específica.
- El slicing en Python incluye el primer índice pero excluye el último.
