## Ejercicio 1: Lectura Básica de Archivo

**Dificultad:** 1/10

**Instrucciones:** Abre el archivo `ejemplo1.txt` en modo lectura e imprime todo su contenido. El código actual tiene errores.

**Código con Errores:**

```python
# Intenta abrir y leer el archivo ejemplo1.txt
archivo = open(ejemplo1.txt, "w") # Error 1: Modo incorrecto, Error 2: Nombre archivo como variable
contenido = archivo.readall()     # Error 3: Método inexistente
print(contenido)
# Falta cerrar el archivo si no se usa 'with'

## Pistas:
### ¿Cuál es el modo correcto para leer un archivo?
### Los nombres de archivo deben ser cadenas de texto (strings).
### Revisa el nombre del método para leer el contenido completo de un archivo.
