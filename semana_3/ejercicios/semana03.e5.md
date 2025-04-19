## Ejercicio 5: Argumentos con nombre (**kwargs) (Nivel 5/10)

**Objetivo**: Crear una función que genere una ficha de persona usando argumentos con nombre.

```python
"""
# Curso: Fundamentos de Python para Ciencia de Datos
# Sesión 03: Fundamentos de programación
# Fecha: 19-04-2025
# Autor: Godofredo Diaz
# E-mail: gdiaz@tecsup.edu.pe
"""

# Corrige los 3 errores en la siguiente función
def crear_ficha(**datos):
    ficha = ""
    for clave, valor in datos:
        ficha += f"{clave}: {valor}\n"
    if not "nombre" in datos:
        ficha = "ERROR: El nombre es obligatorio"
    return ficha

# Pruebas
print(crear_ficha(nombre="Ana", edad=25, ciudad="Lima"))
print(crear_ficha(edad=30, profesion="Ingeniero"))
```

**Pistas**:
1. ¿Cómo se recorren los elementos de un diccionario?
2. La validación de "nombre" necesita ejecutarse antes de construir la ficha.
3. Revisa la sintaxis para verificar si una clave existe en un diccionario.

---
