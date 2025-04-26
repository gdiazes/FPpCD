## Ejercicio 9: Agrupación y Agregación

**Dificultad:** 9/10

**Instrucciones:** Carga el DataFrame del medallero. Agrupa los países por la cantidad de medallas de 'Plata' que obtuvieron. Luego, para cada grupo, calcula la cantidad *total* de medallas de 'Oro' y 'Bronce'. Muestra el resultado.

**Código con Errores:**

```python
# Agrupar por Plata y sumar Oro y Bronce por grupo
import pandas as pd
import numpy # Error 1: numpy no se usa explícitamente si usamos funciones de agregación de Pandas/NumPy conocidas por .agg

archivo_path = "medallero_Panamericanos_Lima2019.csv"
df = pd.read_csv(archivo_path, encoding='cp1252')

# Error 2: Falta especificar la función de agregación después de groupby
grupos_plata = df.groupby('Plata')

# Error 3: .agg espera un diccionario o función, y las columnas a agregar deben ser correctas
resultado_agg = grupos_plata.agg({'Oro': sum, 'Bronce': 'total'})

print(resultado_agg)
```

**Pistas:**

1.  El método `.agg()` se aplica *después* del `.groupby()` para realizar cálculos sobre los grupos.
2.  `numpy` no necesita ser importado si usas funciones de agregación estándar como strings ('sum', 'mean') o funciones NumPy directamente (`np.sum`) dentro de `.agg()`.
3.  El método `.agg()` puede recibir un diccionario donde las claves son las columnas a agregar y los valores son las funciones de agregación (como string `'sum'` o la función `sum`). Verifica los nombres de las funciones de agregación.

---

