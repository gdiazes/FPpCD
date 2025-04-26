## Ejercicio 5: Seleccionar Columnas Específicas

**Dificultad:** 5/10

**Instrucciones:** Carga el DataFrame del medallero y selecciona únicamente las columnas 'Pais' y 'Total'. Imprime las primeras 5 filas de este nuevo DataFrame.

**Código con Errores:**

```python
# Seleccionar columnas 'Pais' y 'Total'
import pandas as pd

archivo_path = "medallero_Panamericanos_Lima2019.csv"
df = pd.read_csv(archivo_path, encoding='cp1252') # Asumiendo que esta codificación es correcta

# Error 1: Forma incorrecta de seleccionar múltiples columnas
medallas_total = df['Pais', 'Total']

print(medallas_total.head) # Error 2: Llamada incorrecta al método head, Error 3: No se imprime nada si head no se llama ()
```

**Pistas:**

1.  Para seleccionar múltiples columnas, debes pasar una lista de nombres de columna.
2.  Los métodos en Python (como `head`) necesitan paréntesis `()` para ser ejecutados.
3.  Asegúrate de que la función `print()` reciba lo que retorna la ejecución de `head()`.

---

