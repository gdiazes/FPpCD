# Ejercicios de Manipulación de Datos en Python (Semana 4)

Estos ejercicios están basados en los conceptos vistos en la sesión 4 (manejo de archivos y librería Pandas). Cada ejercicio tiene un nivel de dificultad (1-10), incluye un fragmento de código con 3 errores intencionales y 3 pistas para ayudarte a encontrar la solución.

**Prerrequisitos:**

*   Tener la librería Pandas instalada (`pip install pandas`).
*   Tener acceso a los archivos `ejemplo1.txt` y `medallero_Panamericanos_Lima2019.csv` (con codificación `cp1252` o `latin1`). Para los ejercicios, se asume que estos archivos han sido **subidos directamente al entorno de Colab** (o al directorio de trabajo actual), por lo que las rutas no incluirán `/content/drive/MyDrive/`. Si usas Google Drive, ajusta las rutas en el código de los ejercicios.

---

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
