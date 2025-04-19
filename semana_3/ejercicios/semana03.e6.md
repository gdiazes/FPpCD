## Ejercicio 6: Combinación de *args y **kwargs (Nivel 6/10)

**Objetivo**: Implementar una función flexible que procese datos de estudiantes con notas variables.

```python
"""
# Curso: Fundamentos de Python para Ciencia de Datos
# Sesión 03: Fundamentos de programación
# Fecha: 19-04-2025
# Autor: Godofredo Diaz
# E-mail: gdiaz@tecsup.edu.pe
"""

# Corrige los 3 errores en la siguiente función
def procesar_estudiante(nombre, *notas, **info_adicional):
    resultado = f"Estudiante: {nombres}\n"
    
    # Calcular promedio de notas
    if notas:
        promedio = sum(notas) / len(notas)
        resultado += f"Promedio: {promedio:.2f}\n"
    
    # Añadir información adicional
    for clave, valor in info_adicional:
        resultado += f"{clave}: {valor}\n"
    
    return resultado

# Prueba
print(procesar_estudiante("María", 15, 18, 17, carrera="Sistemas", ciclo=3))
```

**Pistas**:
1. Hay un error en el nombre de variable dentro de la función.
2. ¿Cómo se recorren los elementos de un diccionario correctamente?
3. Revisa el orden de los argumentos al llamar a la función.

---
