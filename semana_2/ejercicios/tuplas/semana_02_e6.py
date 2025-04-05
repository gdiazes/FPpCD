### Ejercicio 6: Operaciones con Tuplas (Nivel 3)
**Objetivo:** Realizar operaciones básicas con tuplas.

**Código con errores:**
```python
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla_combinada = tupla1.append(tupla2)
tupla1[0] = 10
print(len(tupla_combinada))
```

**Pistas:**
- Las tuplas no tienen método `.append()`, se concatenan de otra manera.
- Las tuplas son inmutables, no se pueden modificar después de creadas.
- `len()` devuelve la cantidad de elementos en una secuencia.
