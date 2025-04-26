## Ejercicio 8: Calcular y Añadir Nueva Columna

**Dificultad:** 8/10

**Instrucciones:** Carga el DataFrame del medallero. Calcula el 'Puntaje Ponderado' de cada país como `(Oro * 3) + (Plata * 2) + (Bronce * 1)`. Añade esta columna al DataFrame y muestra las 5 filas con mayor puntaje ponderado.

**Código con Errores:**

```python
# Calcular puntaje ponderado y añadir como columna
import pandas as pd

archivo_path = "medallero_Panamericanos_Lima2019.csv"
df = pd.read_csv(archivo_path, encoding='cp1252')

# Error 1: Acceso incorrecto a columnas para el cálculo
puntaje = (df.Oro * 3) + (df['Plata'] * 2) + (df.Bronce * 1)

df['Puntaje Ponderado'] == puntaje # Error 2: Asignación incorrecta (== en lugar de =)

# Error 3: Método incorrecto para ordenar y obtener los 'top'
top_5 = df.sort('Puntaje Ponderado', ascending=True).head(5)

print(top_5)
```

**Pistas:**

1.  Puedes acceder a las columnas con `df['NombreColumna']` o `df.NombreColumna` (si el nombre es un identificador válido). Asegúrate de ser consistente.
2.  Para asignar el resultado de un cálculo a una nueva columna, se usa el operador de asignación `=`.
3.  ¿Cuál es el método correcto para ordenar un DataFrame por los valores de una columna y cómo especificas el orden descendente para obtener los más altos?

---

