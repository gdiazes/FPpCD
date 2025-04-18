**Manual Paso a Paso: Creación y Publicación de la Librería Python `mi-calculadora` en PyPI (Ubuntu/Linux)**

**Introducción**

Este manual te guiará detalladamente en la creación de una librería Python llamada `mi-calculadora`, que contendrá operaciones matemáticas básicas. Cubriremos desde la configuración inicial y estructura del proyecto hasta su publicación en el Python Package Index (PyPI), permitiendo que cualquier persona pueda instalarla usando `pip`. **Los comandos están optimizados para un entorno Ubuntu/Debian Linux.**

**Prerrequisitos e Instalación de Herramientas (Ubuntu)**

1.  **Python 3 Instalado:** Ubuntu generalmente viene con Python 3 preinstalado.
    *   **Verificación:** Abre tu terminal y ejecuta:
        ```bash
        python3 --version
        ```
        Deberías ver una versión 3.x (se recomienda 3.7 o superior).
    *   **Instalación (si es necesario):**
        ```bash
        sudo apt update
        sudo apt install python3
        ```

2.  **pip (Gestor de Paquetes para Python 3):**
    *   **Verificación:** La forma más robusta es verificar a través del módulo `pip` de `python3`:
        ```bash
        python3 -m pip --version
        ```
    *   **Instalación (si es necesario):** A menudo se instala junto con `python3`, pero si no, usa:
        ```bash
        sudo apt update
        sudo apt install python3-pip
        ```
    *   **Actualización (Recomendado):** Asegúrate de tener la última versión de pip:
        ```bash
        python3 -m pip install --upgrade pip
        ```

3.  **venv (Entornos Virtuales para Python 3):** Esencial para aislar dependencias.
    *   **Verificación:** Intenta ejecutar `python3 -m venv --help`. Si funciona, está listo.
    *   **Instalación (si es necesario):** En Ubuntu/Debian, a veces necesita instalarse por separado:
        ```bash
        sudo apt update
        sudo apt install python3-venv
        ```

4.  **Herramientas de Build y Publicación (`build` y `twine`):** Las instalaremos más adelante usando `pip`.

5.  **Cuentas en Repositorios:**
    *   **PyPI:** Necesitarás una cuenta registrada en [PyPI (Python Package Index)](https://pypi.org/) para la publicación final.
    *   **TestPyPI (Muy Recomendado):** Crea una cuenta separada en [TestPyPI](https://test.pypi.org/). Es un espejo de PyPI para realizar pruebas de publicación. ¡**Usa contraseñas diferentes para PyPI y TestPyPI**!

**Pasos**

**Paso 1: Planificar tu Librería `mi-calculadora`**

*   **Nombre del Paquete (PyPI):** `mi-calculadora` (Verifica disponibilidad en PyPI. Si está tomado, considera `mi-calculadora-basica-[tu_alias]`). Usaremos `mi-calculadora` aquí.
*   **Nombre de Importación (Python):** `mi_calculadora`
*   **Funcionalidad:** Funciones para sumar, restar, multiplicar y dividir.
*   **Audiencia:** Público general, principiantes.
*   **Licencia:** Apache License 2.0.

**Paso 2: Estructura del Directorio**

Crea un directorio principal para tu proyecto (p.ej., `~/proyectos/mi-calculadora-proyecto`) y organiza los archivos dentro:

```
mi-calculadora-proyecto/
├── LICENSE
├── README.md
├── pyproject.toml
├── src/
│   └── mi_calculadora/
│       ├── __init__.py
│       └── operaciones.py
└── tests/
    └── test_calculadora.py # (Opcional pero recomendado)
```

**Paso 3: Escribir el Código de la Librería**

1.  **`src/mi_calculadora/operaciones.py`:**
    ```python
    # src/mi_calculadora/operaciones.py
    """Módulo con operaciones matemáticas básicas."""

    def sumar(a, b):
      """Retorna la suma de dos números."""
      return a + b

    def restar(a, b):
      """Retorna la resta de dos números (a - b)."""
      return a - b

    def multiplicar(a, b):
      """Retorna la multiplicación de dos números."""
      return a * b

    def dividir(a, b):
      """
      Retorna la división de dos números (a / b).
      Lanza un ValueError si se intenta dividir por cero.
      """
      if b == 0:
          raise ValueError("No se puede dividir por cero.")
      return a / b
    ```

2.  **`src/mi_calculadora/__init__.py`:**
    ```python
    # src/mi_calculadora/__init__.py
    """
    Mi-Calculadora: Una librería simple con operaciones matemáticas básicas.
    """

    __version__ = "0.1.0" # Versión inicial

    from .operaciones import sumar, restar, multiplicar, dividir

    __all__ = ['sumar', 'restar', 'multiplicar', 'dividir']
    ```

**Paso 4: Crear el Archivo `LICENSE`**

1.  Obtén el texto completo de la licencia Apache 2.0 desde [https://www.apache.org/licenses/LICENSE-2.0.txt](https://www.apache.org/licenses/LICENSE-2.0.txt).
2.  Copia y pega ese texto en el archivo `LICENSE` en la raíz de tu proyecto (`mi-calculadora-proyecto/LICENSE`).

**Paso 5: Configurar `pyproject.toml`**

Define la construcción y metadatos.

```toml
# pyproject.toml

[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "mi-calculadora"
version = "0.1.0" # Coincide con __version__
authors = [
  { name="Tu Nombre o Alias", email="tu_email@example.com" }, # ¡Actualiza!
]
description = "Una librería simple de Python con operaciones matemáticas básicas."
readme = "README.md"
requires-python = ">=3.7"
license = {text = "Apache-2.0"}
keywords = ["calculadora", "matemáticas", "básico", "operaciones"]
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Intended Audience :: Education",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Scientific/Engineering :: Mathematics",
    "License :: OSI Approved :: Apache Software License", # ¡Correcto!
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Operating System :: OS Independent",
]
dependencies = [] # Sin dependencias externas

[project.urls]
"Homepage" = "https://github.com/tu_usuario/mi-calculadora-proyecto" # ¡Actualiza!
"Repository" = "https://github.com/tu_usuario/mi-calculadora-proyecto" # ¡Actualiza!
"Bug Tracker" = "https://github.com/tu_usuario/mi-calculadora-proyecto/issues" # ¡Actualiza!
```

**Paso 6: Escribir un Buen `README.md`**

La "cara" de tu proyecto.

```markdown
# Mi-Calculadora

[![PyPI version](https://badge.fury.io/py/mi-calculadora.svg)](https://badge.fury.io/py/mi-calculadora)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Librería Python simple con operaciones matemáticas básicas (suma, resta, multiplicación, división).

## Instalación

Instala desde PyPI usando pip (asegúrate de usar el pip asociado a Python 3):

```bash
python3 -m pip install mi-calculadora
```

## Uso Básico

Importa y usa las funciones en tu código Python 3:

```python
import mi_calculadora

# Operaciones
suma = mi_calculadora.sumar(10, 5)       # 15
resta = mi_calculadora.restar(10, 5)      # 5
multi = mi_calculadora.multiplicar(10, 5) # 50
div = mi_calculadora.dividir(10, 5)       # 2.0

print(f"Suma: {suma}, Resta: {resta}, Multi: {multi}, Div: {div}")

# Manejo de errores
try:
    mi_calculadora.dividir(10, 0)
except ValueError as e:
    print(f"Error: {e}") # Error: No se puede dividir por cero.

# Versión
print(f"Versión: {mi_calculadora.__version__}") # 0.1.0 (o la versión actual)
```

## Licencia

Distribuido bajo la Licencia Apache 2.0. Ver `LICENSE` para más información.

## Contribuciones

Proyecto de ejemplo. Issues bienvenidos en GitHub (ver URL en `pyproject.toml`).
```

**Paso 7: Configurar y Usar un Entorno Virtual**

Aísla las dependencias de tu proyecto.

```bash
# Navega a la raíz de tu proyecto en la terminal
cd ~/proyectos/mi-calculadora-proyecto # Ajusta la ruta si es necesario

# Crea un entorno virtual llamado 'venv' usando el módulo venv de python3
python3 -m venv venv

# Activa el entorno virtual (para bash/zsh en Linux)
source venv/bin/activate

# Tu prompt debería cambiar, mostrando (venv) al principio
# Ejemplo: (venv) tu_usuario@tu_maquina:~/proyectos/mi-calculadora-proyecto$
```

**Paso 8: Instalar Herramientas de Build y Construir el Paquete**

Dentro de tu entorno virtual activado (`(venv)` visible en el prompt):

1.  **Instala `build` usando `python3 -m pip`:**
    ```bash
    python3 -m pip install --upgrade build
    ```
2.  **Ejecuta el proceso de construcción usando `python3 -m build`:**
    ```bash
    python3 -m build
    ```

Esto creará (o actualizará) el directorio `dist/` con los archivos:
*   `mi_calculadora-0.1.0.tar.gz` (sdist)
*   `mi_calculadora-0.1.0-py3-none-any.whl` (wheel)

**Paso 9: Instalar Twine y Publicar en TestPyPI (Prueba)**

¡Fundamental probar antes de publicar en el real!

1.  **Instala `twine`:**
    ```bash
    python3 -m pip install --upgrade twine
    ```
2.  **Sube los archivos de `dist/` a TestPyPI:**
    ```bash
    # 'twine' es ahora un comando disponible en tu entorno virtual
    twine upload --repository testpypi dist/*
    ```
    *   Se te pedirá tu nombre de usuario y contraseña de **TestPyPI**.
    *   **Seguridad:** Es mejor usar un **API Token** de TestPyPI. Genera uno en la configuración de tu cuenta de TestPyPI. Usa `__token__` como nombre de usuario y pega el token como contraseña.

**Paso 10: Probar la Instalación desde TestPyPI**

Simula cómo un usuario instalaría tu paquete desde el repositorio de prueba. Hazlo en un entorno virtual limpio y separado.

```bash
# (Opcional) Desactiva el entorno actual
# deactivate

# (Opcional) Crea y activa un nuevo entorno para la prueba
# mkdir ~/proyectos/test-mi-calculadora && cd ~/proyectos/test-mi-calculadora
# python3 -m venv test_env
# source test_env/bin/activate

# Instala tu paquete desde TestPyPI usando python3 -m pip
python3 -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple mi-calculadora

# Abre el intérprete de Python 3
python3
```

Dentro del intérprete de Python 3:

```python
>>> import mi_calculadora
>>> mi_calculadora.sumar(99, 1)
100
>>> mi_calculadora.__version__
'0.1.0'
>>> exit()
```

Si todo funciona correctamente, ¡procede a la publicación oficial!

**Paso 11: Publicar en PyPI (Oficial)**

Ahora, publica tu librería en el repositorio principal de PyPI.

1.  **Verifica:** Revisa que los archivos en `dist/` (el `tar.gz` y el `.whl`) correspondan a la versión `0.1.0` (o la que deseas publicar). Si hiciste cambios, borra `dist/` (`rm -rf dist/`) y vuelve a ejecutar `python3 -m build`.
2.  **Sube a PyPI oficial:**
    ```bash
    twine upload dist/*
    ```
    *   Se te pedirá tu nombre de usuario y contraseña de **PyPI** (el real).
    *   **Seguridad:** Nuevamente, se recomienda usar un **API Token** generado desde tu cuenta de PyPI. Usuario: `__token__`, Contraseña: el token.

**¡Advertencia Crucial!**
*   No puedes volver a subir la misma versión (ej. `0.1.0`) a PyPI.
*   Eliminar paquetes/versiones de PyPI es difícil.
*   Para actualizaciones o correcciones, **incrementa la versión** en `pyproject.toml` y `src/mi_calculadora/__init__.py` (e.g., a `0.1.1`), reconstruye (`python3 -m build`) y repite el `twine upload dist/*`.

**Paso 12: Verificar la Publicación Final**

1.  Espera unos minutos y visita `https://pypi.org/project/mi-calculadora/`. Verifica que la página muestra la información correcta (README, licencia, etc.).
2.  Realiza una instalación final en un entorno virtual limpio:
    ```bash
    # (En un nuevo entorno virtual limpio y activado)
    python3 -m pip install mi-calculadora

    # Prueba en Python 3
    python3
    >>> import mi_calculadora
    >>> print(mi_calculadora.dividir(10, 2))
    5.0
    >>> exit()
    ```

**Conclusión**

¡Enhorabuena! Has seguido los pasos para crear, empaquetar y publicar tu librería `mi-calculadora` en PyPI desde un entorno Ubuntu/Linux, usando las mejores prácticas con `python3` y `venv`. Tu librería está ahora disponible para la comunidad Python.

Recuerda la importancia de mantener tu librería, añadir pruebas (`tests/`), y gestionar versiones adecuadamente para futuras actualizaciones.

---

**Preguntas Críticas para Reflexionar (Mismas que antes, siguen siendo relevantes)**

1.  **Sostenibilidad y Mantenimiento:** ¿Cómo planeas gestionar los reportes de errores (issues) y las solicitudes de nuevas funcionalidades (feature requests) a largo plazo? ¿Tienes el tiempo y los recursos para mantener la librería actualizada con nuevas versiones de Python y posibles cambios en sus dependencias?
2.  **Valor y Audiencia:** ¿Qué problema específico resuelve tu librería que no esté ya cubierto por otras librerías existentes? ¿Cómo te asegurarás de que la librería siga siendo relevante y útil para tu audiencia objetivo a medida que el ecosistema Python evoluciona?
3.  **Calidad y Robustez:** Más allá de la funcionalidad básica, ¿qué medidas adicionales (como pruebas unitarias exhaustivas con `pytest` o `unittest`, integración continua (CI/CD) con GitHub Actions/GitLab CI, documentación detallada generada con Sphinx, ejemplos de uso avanzados) implementarás para asegurar la calidad, fiabilidad y facilidad de uso de tu librería, fomentando así su adopción?
