## Ejercicio 7: Escritura Selectiva a Archivo de Texto

**Dificultad:** 7/10

**Instrucciones:** Lee el archivo `ejemplo1.txt`. Luego, escribe en un nuevo archivo llamado `ejemplo1_filtrado.txt` únicamente las líneas que contienen la palabra "Python" (ignorando mayúsculas/minúsculas).

**Código con Errores:**

```python
# Escribir líneas que contienen "Python" (case-insensitive) a un nuevo archivo
palabra_buscar = "Python"
archivo_salida = "ejemplo1_filtrado.txt"

with open("ejemplo1.txt", "r") as f_in # Error 1: Falta ':' al final del 'with'
    with open(archivo_salida, "a") as f_out: # Error 2: Modo 'a' podría no ser ideal si se ejecuta varias veces
        for linea in f_in.readline(): # Error 3: Iterar sobre readline() lee solo la primera línea caracter por caracter
            if palabra_buscar.lower() in linea:
                f_out.write(linea)

print(f"Archivo {archivo_salida} creado/actualizado.")
```

**Pistas:**

1.  La sintaxis de la declaración `with` requiere dos puntos (`:`) al final.
2.  Si quieres que el archivo de salida se cree limpio cada vez que ejecutas el script, ¿qué modo de apertura es mejor que `'a'` (append)?
3.  Para procesar un archivo línea por línea, ¿cómo se itera directamente sobre el objeto archivo?

---

