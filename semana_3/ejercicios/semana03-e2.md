## Ejercicio 2: Calculadora simple (Nivel 2/10)

**Objetivo**: Implementar una función que realice operaciones matemáticas básicas según un operador proporcionado.

```python
"""
# Curso: Fundamentos de Python para Ciencia de Datos
# Sesión 03: Fundamentos de programación
# Fecha: 19-04-2025
# Autor: Godofredo Diaz
# E-mail: gdiaz@tecsup.edu.pe
"""

# Corrige los 3 errores en la siguiente función
def calculadora(a, b, operacion):
    if operacion = "suma":
        return a + b
    elif operacion == "resta"
        return a - b
    elif operacion == "multiplicacion":
        return a * b
    elif operacion == "division":
        return a / 0
    else:
        return "Operación no válida"

# Pruebas
print(calculadora(10, 5, "suma"))
print(calculadora(10, 5, "division"))
```

**Pistas**:
1. Revisa los operadores de comparación en las estructuras condicionales.
2. ¿Falta algún caracter después de la condición "resta"?
3. ¿Qué sucede si dividimos por cero en Python?

---
