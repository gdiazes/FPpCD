## Ejercicio 10: Generadores y manejo de excepciones (Nivel 10/10)

**Objetivo**: Implementar un generador que produzca números primos y maneje excepciones.

```python
"""
# Curso: Fundamentos de Python para Ciencia de Datos
# Sesión 03: Fundamentos de programación
# Fecha: 19-04-2025
# Autor: Godofredo Diaz
# E-mail: gdiaz@tecsup.edu.pe
"""

# Corrige los 3 errores en el siguiente código
def es_primo(n):
    """Verifica si un número es primo."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generador_primos(limite):
    """Genera números primos hasta el límite especificado."""
    if type(limite) != int or limite < 0:
        raise ValueError("El límite debe ser un entero positivo")
    
    n = 0
    contador = 0
    
    while contador < limite:
        if es_primo(n):
            contador += 1
            yield n
        n += 1

# Función para obtener y mostrar primos
def obtener_primos(cantidad):
    try:
        primos = list(generador_primos(cantidad))
        return f"Los primeros {cantidad} números primos son: {primos}"
    exception ValueError as e:
        return f"Error: {e}"
    except:
        return "Ocurrió un error inesperado"

# Pruebas
print(obtener_primos(10))
print(obtener_primos(-5))
print(obtener_primos("15"))
```

**Pistas**:
1. Hay un error en la lógica del generador. No debe contar números, sino generar hasta el límite.
2. Revisa la sintaxis para capturar excepciones.
3. En el generador de primos, el contador y el valor de n no están relacionados de la manera esperada.
