## Ejercicio 10: Combinando Lectura, Filtro y Escritura

**Dificultad:** 10/10

**Instrucciones:** Lee el archivo `medallero_Panamericanos_Lima2019.csv`. Filtra el DataFrame para quedarte solo con los países que obtuvieron al menos una medalla de cada tipo (Oro > 0, Plata > 0 y Bronce > 0). Guarda este subconjunto de datos (solo las columnas 'Pais', 'Oro', 'Plata', 'Bronce') en un nuevo archivo CSV llamado `medallero_completo.csv`, sin incluir el índice de Pandas en el archivo.

**Código con Errores:**

```python
# Filtrar países con al menos 1 medalla de cada tipo y guardar CSV
import pandas as pd

archivo_path = "medallero_Panamericanos_Lima2019.csv"
df = pd.read_csv(archivo_path, encoding='cp1252')

# Error 1: Sintaxis incorrecta para combinar condiciones múltiples
condicion = df['Oro'] > 0 & df['Plata'] > 0 & df['Bronce'] > 0
df_completo = df[condicion]

# Error 2: Selección incorrecta de columnas y parámetro incorrecto para no guardar índice
df_completo['Pais','Oro','Plata','Bronce'].to_csv("medallero_completo.csv", index=True) # Error 3: Selección de columnas

```

**Pistas:**

1.  Al combinar múltiples condiciones booleanas en Pandas, cada condición individual debe ir entre paréntesis `()`.
2.  Para guardar sin el índice del DataFrame, el parámetro `index` de `to_csv` debe ser `False`.
3.  Para seleccionar un subconjunto de columnas *antes* de guardar, crea un nuevo DataFrame con esas columnas o selecciona las columnas en el DataFrame existente usando la sintaxis de doble corchete `[[]]`.

---
```

