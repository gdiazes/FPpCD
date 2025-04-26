## Ejercicio 2: Escritura con `with`

**Dificultad:** 2/10

**Instrucciones:** Usando `with`, abre (o crea) un archivo llamado `salida_ej2.txt` y escribe dos líneas distintas en él: "Primera línea de prueba" y "Segunda línea de prueba".

**Código con Errores:**

```python
# Escribir dos líneas en un archivo usando with
with open("salida_ej2.txt", "r") as file_out: # Error 1: Modo incorrecto
    file_out.write("Primera línea de prueba")
    file_out.Write("Segunda línea de prueba\n") # Error 2: Nombre método en mayúscula, Error 3: Falta un salto de línea en la primera write

```

**Pistas:**

1.  Para escribir (y crear si no existe), necesitas un modo diferente a `'r'`.
2.  Los nombres de métodos en Python son sensibles a mayúsculas y minúsculas.
3.  Si no añades `\n`, las escrituras se concatenan en la misma línea.

---
