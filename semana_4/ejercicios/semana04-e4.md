## Ejercicio 4: Leer CSV y Mostrar Head

**Dificultad:** 4/10

**Instrucciones:** Lee el archivo `medallero_Panamericanos_Lima2019.csv` (recuerda que podría necesitar una codificación específica) y muestra las primeras 3 filas.

**Código con Errores:**

```python
# Leer CSV y mostrar las primeras 3 filas
import pandas as pd

archivo_path = "medallero_Panamericanos_Lima2019.csv"
df = pd.read_csv(filepath_or_buffer=archivo_path, encoding='utf8') # Error 1: Encoding podría ser incorrecto, Error 2: Nombre de parámetro redundante (se puede omitir)

print(df.header(3)) # Error 3: Método incorrecto para ver primeras filas
```

**Pistas:**

1.  Si obtienes `UnicodeDecodeError`, ¿qué otras codificaciones comunes podrías probar para archivos CSV?
2.  `read_csv` puede inferir el archivo si es el primer argumento posicional.
3.  ¿Cuál es el método de Pandas para visualizar las primeras filas de un DataFrame?

---
