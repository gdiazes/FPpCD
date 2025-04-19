## Ejercicio 7: Funciones lambda y map (Nivel 7/10)

**Objetivo**: Usar funciones lambda y map para transformar una lista de temperaturas de Celsius a Fahrenheit.

```python
"""
# Curso: Fundamentos de Python para Ciencia de Datos
# Sesión 03: Fundamentos de programación
# Fecha: 19-04-2025
# Autor: Godofredo Diaz
# E-mail: gdiaz@tecsup.edu.pe
"""

# Corrige los 3 errores en el siguiente código
def convertir_temperaturas(temperaturas_celsius):
    # Fórmula: (C × 9/5) + 32 = F
    convertir = lambda f: (f * 9/5) + 32
    
    # Usar map para aplicar la conversión a cada temperatura
    temperaturas_fahrenheit = map(convertir, temperaturas_celsius)
    
    return temperaturas_fahrenheit

# Lista de temperaturas en Celsius
temp_celsius = [0, 10, 20, 30, 40]

# Convertir y mostrar
resultado = convertir_temperaturas(temp_celsius)
print(f"Temperaturas en Fahrenheit: {resultado}")
```

**Pistas**:
1. La variable en la función lambda no coincide con el uso dentro de la función.
2. El resultado de map es un objeto iterable, no una lista. ¿Cómo podemos verlo como lista?
3. Revisa la fórmula de conversión de Celsius a Fahrenheit.

---
