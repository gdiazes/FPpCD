## Ejercicio 6: Filtrar Filas con `.loc` y Condición Simple

**Dificultad:** 6/10

**Instrucciones:** Carga el DataFrame del medallero. Establece 'Pais' como índice. Luego, filtra y muestra las filas (todos sus datos) de los países que obtuvieron exactamente 0 medallas de Oro.

**Código con Errores:**

```python
# Filtrar países con 0 medallas de Oro usando .loc
import pandas as pd

archivo_path = "medallero_Panamericanos_Lima2019.csv"
df = pd.read_csv(archivo_path, encoding='cp1252')

df.set_index("Pais") # Error 1: Falta inplace=True para modificar el df

# Error 2: Condición de igualdad incorrecta, Error 3: .loc necesita la condición directamente
condicion = df['Oro'] = 0
paises_cero_oro = df.loc[condicion]

print(paises_cero_oro)
```

**Pistas:**

1.  El método `.set_index()` devuelve un nuevo DataFrame por defecto. ¿Cómo modificas el original?
2.  Para comparar igualdad en una condición, se usa `==`, no `=`.
3.  `.loc[]` espera la serie booleana directamente como primer argumento para el filtrado de filas.

---

