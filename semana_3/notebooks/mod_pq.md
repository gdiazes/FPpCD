## Crear módulos y paquete mediante funciones


La conceptualización de módulos y paquetes en Python se deriva directamente de la necesidad de organizar y reutilizar el código de manera efectiva, una evolución natural de los principios de la programación estructurada. La **Referencia del Lenguaje Python (Python Software Foundation, s.f., sección 6)** describe formalmente el sistema de importación y la estructura de módulos y paquetes, que son la base para compartir y organizar el código en Python.

**1. Creación de un Módulo (`operaciones_basicas.py`)**

Un **módulo** en Python es, en su forma más simple, un archivo individual que contiene código Python (definiciones de funciones, clases, variables). Sirve como una unidad lógica para agrupar funcionalidades relacionadas y actúa como su propio espacio de nombres, evitando colisiones entre identificadores definidos en diferentes archivos.

**Paso a Paso y Sintaxis:**

1.  **Crear el Archivo `.py`**: Se crea un archivo de texto simple con la extensión `.py`. El nombre del archivo (sin la extensión) se convertirá en el nombre del módulo cuando se importe.
    *   *Ejemplo*: Creamos un archivo llamado `operaciones_basicas.py`.

2.  **Definir Funciones (u otro código) dentro del Archivo**: Dentro de este archivo, escribimos las definiciones de nuestras funciones, siguiendo la sintaxis que ya discutimos. Es crucial incluir docstrings para documentar cada función y, opcionalmente, un docstring a nivel de módulo al inicio del archivo.

    ```python
    # operaciones_basicas.py

    """
    Módulo que proporciona funciones para realizar
    operaciones matemáticas básicas.
    """

    def sumar(a, b):
        """Devuelve la suma de a y b."""
        # La sintaxis de la función es la misma que antes
        return a + b

    def restar(a, b):
        """Devuelve la resta de a menos b."""
        return a - b

    def multiplicar(a, b):
        """Devuelve la multiplicación de a y b."""
        return a * b

    def dividir(a, b):
        """
        Devuelve la división de a entre b.
        Lanza ValueError si b es cero.
        """
        if b == 0:
            raise ValueError("División por cero no permitida.")
        return a / b

    # Podríamos añadir otras constantes o funciones si fuera necesario
    PI = 3.14159
    ```

3.  **Guardar el Archivo**: Simplemente guardamos el archivo. Ahora `operaciones_basicas.py` es un módulo Python listo para ser importado y utilizado en otros scripts o módulos, siempre que se encuentre en el `sys.path` de Python (que incluye el directorio actual y las ubicaciones de instalación de Python).

**2. Creación de un Paquete (`calculadora`)**

Un **paquete** es una forma de estructurar el espacio de nombres de los módulos de Python utilizando una jerarquía de directorios. Un directorio se convierte en un paquete si contiene un archivo especial llamado `__init__.py`. Este archivo puede estar vacío, pero su presencia indica a Python que el directorio debe ser tratado como un paquete, permitiendo importar módulos de él o submódulos dentro de él usando la notación de puntos (`.`).

**Paso a Paso y Sintaxis:**

1.  **Crear el Directorio del Paquete**: Se crea un directorio con el nombre que deseamos para nuestro paquete.
    *   *Ejemplo*: Creamos un directorio llamado `calculadora`.

2.  **Crear el Archivo `__init__.py`**: Dentro del directorio del paquete (`calculadora/`), creamos un archivo *obligatorio* llamado `__init__.py`. Este archivo se ejecuta cuando el paquete (o un módulo dentro de él) es importado por primera vez. A menudo se deja vacío, pero puede contener código de inicialización del paquete o definir qué símbolos exporta el paquete (usando `__all__`).
    *   *Sintaxis*: Simplemente crear un archivo vacío con ese nombre exacto.

    ```python
    # calculadora/__init__.py
    # Este archivo puede estar vacío o contener código de inicialización.
    # Por ejemplo, podríamos hacer que algunas funciones estén disponibles
    # directamente al importar 'calculadora', pero lo mantendremos simple.
    print("Inicializando el paquete calculadora...")
    ```
    *(Nota: El `print` es solo para demostrar que se ejecuta; a menudo es mejor mantenerlo vacío o usarlo para importar selectivamente).*

3.  **Colocar Módulos Dentro del Directorio del Paquete**: Movemos o creamos nuestros archivos de módulo (`.py`) dentro del directorio del paquete.
    *   *Ejemplo*: Movemos nuestro archivo `operaciones_basicas.py` dentro del directorio `calculadora/`.

**Estructura de Carpetas Resultante (Árbol)**

Imaginemos que tenemos un proyecto principal donde usaremos nuestra calculadora:

```
mi_proyecto/
├── calculadora/              <-- Directorio del Paquete
│   ├── __init__.py           <-- Archivo que define 'calculadora' como paquete
│   └── operaciones_basicas.py  <-- Nuestro módulo con las funciones
├── main_script.py            <-- Un script que usará el paquete
└── README.txt                <-- Documentación del proyecto/paquete
```

**3. Archivo `README.txt`**

Este archivo proporciona información esencial para que otros (o tú mismo en el futuro) entiendan y utilicen el paquete.

```txt
===================================
Paquete Calculadora - Documentación
===================================

Descripción
-----------
Este proyecto contiene un paquete Python simple llamado 'calculadora', diseñado para
proporcionar funcionalidades matemáticas básicas. Es un ejemplo de cómo estructurar
código reutilizable usando módulos y paquetes.

Estructura
----------
mi_proyecto/
├── calculadora/              # El paquete principal
│   ├── __init__.py           # Marca el directorio como paquete
│   └── operaciones_basicas.py  # Módulo con funciones de suma, resta, etc.
├── main_script.py            # Ejemplo de cómo usar el paquete
└── README.txt                # Esta documentación

Módulos y Funciones Disponibles
-------------------------------
- calculadora.operaciones_basicas
    - sumar(a, b): Devuelve a + b.
    - restar(a, b): Devuelve a - b.
    - multiplicar(a, b): Devuelve a * b.
    - dividir(a, b): Devuelve a / b (lanza ValueError si b=0).

Uso Básico
----------
Para usar las funciones desde otro script (como `main_script.py`) ubicado en el mismo
nivel que el directorio 'calculadora', puedes importarlas de las siguientes maneras:

1. Importando el módulo completo:
   import calculadora.operaciones_basicas

   resultado_suma = calculadora.operaciones_basicas.sumar(10, 5)
   resultado_div = calculadora.operaciones_basicas.dividir(10, 2)
   print(f"Suma: {resultado_suma}, División: {resultado_div}")

2. Importando el módulo con un alias:
   import calculadora.operaciones_basicas as op

   resultado_mult = op.multiplicar(4, 3)
   print(f"Multiplicación: {resultado_mult}")

3. Importando funciones específicas:
   from calculadora.operaciones_basicas import sumar, restar

   resultado_resta = restar(100, 55)
   print(f"Resta: {resultado_resta}")

Consideraciones
---------------
- Asegúrate de que el directorio 'mi_proyecto' (o el directorio que contiene 'calculadora')
  esté en el PYTHONPATH o que ejecutes tu script principal desde 'mi_proyecto'.
- El archivo __init__.py es esencial para que Python reconozca 'calculadora' como un paquete.

```

Este enfoque, utilizando módulos y paquetes, permite escalar la organización del código más allá de las funciones individuales, creando artefactos de software reutilizables y mantenibles, una práctica indispensable en cualquier proyecto de investigación computacional serio.

---

**Referencias**

Python Software Foundation. (s.f.). *6. Modules*. The Python Tutorial (Version 3.12.4). Recuperado el 24 de mayo de 2024, de https://docs.python.org/3/tutorial/modules.html *(Cubre tanto módulos como la introducción a paquetes y el sistema de importación)*.

Python Software Foundation. (s.f.). *The import system*. The Python Language Reference (Version 3.12.4). Recuperado el 24 de mayo de 2024, de https://docs.python.org/3/reference/import.html *(Referencia más formal sobre cómo funciona el sistema de importación)*.
