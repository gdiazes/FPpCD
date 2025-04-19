## Ejercicio 3: Argumentos por defecto (Nivel 3/10)

**Objetivo**: Crear una función con parámetros por defecto para generar mensajes personalizados.

```python
"""
# Curso: Fundamentos de Python para Ciencia de Datos
# Sesión 03: Fundamentos de programación
# Fecha: 19-04-2025
# Autor: Godofredo Diaz
# E-mail: gdiaz@tecsup.edu.pe
"""

# Corrige los 3 errores en la siguiente función
def crear_mensaje(nombre, mensaje="Bienvenido", idioma="español")
    if idioma = "español":
        return f"{mensaje}, {nombre}!"
    elif idioma == "inglés":
        return f"Welcome, {nombre}!"
    return f"Idioma {idioma} no soportado"

# Pruebas
print(crear_mensaje("Carlos"))
print(crear_mensaje("John", idioma="inglés"))
print(crear_mensaje("María", "Buenos días"))
```

**Pistas**:
1. Revisa la sintaxis de la definición de la función.
2. Hay un error en el operador de comparación.
3. ¿El orden de los parámetros y argumentos es correcto?

---
