## Ejercicio 9: Importaciones y manejo de módulos (Nivel 9/10)

**Objetivo**: Corregir errores relacionados con importaciones y uso de módulos.

```python
"""
# Curso: Fundamentos de Python para Ciencia de Datos
# Sesión 03: Fundamentos de programación
# Fecha: 19-04-2025
# Autor: Godofredo Diaz
# E-mail: gdiaz@tecsup.edu.pe
"""

# Corrige los 3 errores en el siguiente código
from math import sin, cos
import random as rnd
from datetime import datetime, time

def analizar_datos(datos):
    # Usar funciones matemáticas
    angulo = PI / 4  # 45 grados
    comp_x = cos(angulo)
    comp_y = sin(angulo)
    
    # Generar valores aleatorios
    aleatorio = random.randint(1, 100)
    
    # Obtener fecha actual
    ahora = datetime.now()
    
    return {
        "componentes": (comp_x, comp_y),
        "aleatorio": aleatorio,
        "timestamp": ahora.strftime("%Y-%m-%d %H:%M:%S")
    }

# Prueba
resultado = analizar_datos([1, 2, 3, 4, 5])
print(resultado)
```

**Pistas**:
1. La constante Pi no está importada. ¿Cómo acceder a ella desde el módulo math?
2. Hay un error en el nombre del módulo al usar la función randint.
3. Revisa si todas las importaciones son necesarias.

---
