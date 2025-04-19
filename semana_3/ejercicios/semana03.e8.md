## Ejercicio 8: Decoradores simples (Nivel 8/10)

**Objetivo**: Implementar un decorador que registre las llamadas a una función.

```python
"""
# Curso: Fundamentos de Python para Ciencia de Datos
# Sesión 03: Fundamentos de programación
# Fecha: 19-04-2025
# Autor: Godofredo Diaz
# E-mail: gdiaz@tecsup.edu.pe
"""

# Corrige los 3 errores en el siguiente código
def registrar_llamada(funcion):
    def wrapper(*args, **kwargs)
        print(f"Llamando a {function.__name__} con args: {args} y kwargs: {kwargs}")
        resultado = funcion(*args, *kwargs)
        print(f"La función {funcion.__name__} retornó: {resultado}")
        return resultado
    return wrapper

# Aplicar el decorador
@registrar_llamadas
def suma(a, b):
    return a + b

# Prueba
resultado = suma(5, 3)
print(f"Resultado final: {resultado}")
```

**Pistas**:
1. Revisa la sintaxis de la definición de la función interna (wrapper).
2. Hay un error en el nombre de variable dentro del wrapper.
3. La forma de pasar los argumentos con nombre no es correcta. ¿Cómo se pasan los kwargs?

---
