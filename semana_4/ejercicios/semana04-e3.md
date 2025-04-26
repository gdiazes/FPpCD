
## Ejercicio 3: Crear DataFrame desde Diccionario

**Dificultad:** 3/10

**Instrucciones:** Importa pandas y crea un DataFrame a partir del diccionario `estudiantes_data`. Imprime el DataFrame resultante.

**Código con Errores:**

```python
# Crear DataFrame desde diccionario
import pandas as pd # Error 1: Alias incorrecto (o falta import si se usa pd más abajo sin importarlo)

estudiantes_data = {
    'Nombre': ['Ana', 'Juan', 'Pedro'],
    'Nota': [8.5, 9.0, 7.0],
    'Ciudad': ['Lima', 'Arequipa', 'Lima']
}

df = pandas.Dataframe(estudiante_data) # Error 2: Nombre de librería/variable incorrecto, Error 3: Nombre clase incorrecto (mayúscula)
print(df)
```

**Pistas:**

1.  ¿Cuál es el alias estándar (y el usado comúnmente) para importar la librería pandas?
2.  Verifica que el nombre de la variable del diccionario coincida exactamente con el usado en la creación del DataFrame.
3.  Revisa la capitalización correcta para crear un `DataFrame`.

---
