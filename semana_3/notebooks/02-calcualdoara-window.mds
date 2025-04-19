# Manual Paso a Paso: Creación y Publicación de la Librería Python mi-calculadora en PyPI (Windows)

## Introducción

Este manual te guiará detalladamente en la creación de una librería Python llamada `mi-calculadora`, que contendrá operaciones matemáticas básicas. Cubriremos desde la configuración inicial y estructura del proyecto hasta su publicación en el Python Package Index (PyPI), permitiendo que cualquier persona pueda instalarla usando `pip`. Los comandos están optimizados para un entorno Windows.

## Prerrequisitos e Instalación de Herramientas (Windows)

### 1. Python 3 Instalado:

**Verificación**: Abre tu símbolo del sistema (cmd) o PowerShell y ejecuta:
```
python --version
```
Deberías ver una versión 3.x (se recomienda 3.7 o superior).

**Instalación (si es necesario)**:
- Descarga el instalador de Python desde [python.org](https://www.python.org/downloads/windows/)
- Durante la instalación, asegúrate de marcar la opción "Add Python to PATH"
- Completa la instalación siguiendo las instrucciones en pantalla

### 2. pip (Gestor de Paquetes para Python):

**Verificación**: En cmd o PowerShell, ejecuta:
```
python -m pip --version
```

**Actualización (Recomendado)**: Asegúrate de tener la última versión de pip:
```
python -m pip install --upgrade pip
```

### 3. venv (Entornos Virtuales para Python):

La herramienta `venv` viene incluida con Python en Windows. No es necesario instalarla por separado.

**Verificación**: Intenta ejecutar:
```
python -m venv --help
```
Si muestra la ayuda, está listo para usar.

### 4. Herramientas de Build y Publicación (`build` y `twine`): 

Las instalaremos más adelante usando `pip`.

### 5. Cuentas en Repositorios:

- **PyPI**: Necesitarás una cuenta registrada en [PyPI](https://pypi.org/account/register/) (Python Package Index) para la publicación final.
- **TestPyPI** (Muy Recomendado): Crea una cuenta separada en [TestPyPI](https://test.pypi.org/account/register/). Es un espejo de PyPI para realizar pruebas de publicación. ¡Usa contraseñas diferentes para PyPI y TestPyPI!

## Pasos

### Paso 1: Planificar tu Librería mi-calculadora

- **Nombre del Paquete (PyPI)**: `mi-calculadora` (Verifica disponibilidad en PyPI. Si está tomado, considera `mi-calculadora-basica-[tu_alias]`). Usaremos `mi-calculadora` aquí.
- **Nombre de Importación (Python)**: `mi_calculadora`
- **Funcionalidad**: Funciones para sumar, restar, multiplicar y dividir.
- **Audiencia**: Público general, principiantes.
- **Licencia**: Apache License 2.0.

### Paso 2: Estructura del Directorio

Crea un directorio principal para tu proyecto (p.ej., `C:\Proyectos\mi-calculadora-proyecto`) y organiza los archivos dentro:

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
    └── test_calculadora.py  # (Opcional pero recomendado)
```

En Windows, puedes crear esta estructura usando el Explorador de Archivos o comandos en cmd:

```
mkdir C:\Proyectos\mi-calculadora-proyecto
cd C:\Proyectos\mi-calculadora-proyecto
mkdir src
mkdir src\mi_calculadora
mkdir tests
type nul > LICENSE
type nul > README.md
type nul > pyproject.toml
type nul > src\mi_calculadora\__init__.py
type nul > src\mi_calculadora\operaciones.py
type nul > tests\test_calculadora.py
```

### Paso 3: Escribir el Código de la Librería

#### 1. `src/mi_calculadora/operaciones.py`:

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

#### 2. `src/mi_calculadora/__init__.py`:

```python
# src/mi_calculadora/__init__.py
"""
Mi-Calculadora: Una librería simple con operaciones matemáticas básicas.
"""
__version__ = "0.1.0"  # Versión inicial

from .operaciones import sumar, restar, multiplicar, dividir

__all__ = ['sumar', 'restar', 'multiplicar', 'dividir']
```

### Paso 4: Crear el Archivo `LICENSE`

1. Obtén el texto completo de la licencia Apache 2.0 desde [https://www.apache.org/licenses/LICENSE-2.0.txt](https://www.apache.org/licenses/LICENSE-2.0.txt).
2. Copia y pega ese texto en el archivo `LICENSE` en la raíz de tu proyecto (`mi-calculadora-proyecto/LICENSE`).

### Paso 5: Configurar `pyproject.toml`

Define la construcción y metadatos.

```toml
# pyproject.toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "mi-calculadora"
version = "0.1.0"  # Coincide con __version__
authors = [
    { name="Tu Nombre o Alias", email="tu_email@example.com" },  # ¡Actualiza!
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
    "License :: OSI Approved :: Apache Software License",  # ¡Correcto!
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Operating System :: OS Independent",
]
dependencies = []  # Sin dependencias externas

[project.urls]
"Homepage" = "https://github.com/tu_usuario/mi-calculadora-proyecto"  # ¡Actualiza!
"Repository" = "https://github.com/tu_usuario/mi-calculadora-proyecto"  # ¡Actualiza!
"Bug Tracker" = "https://github.com/tu_usuario/mi-calculadora-proyecto/issues"  # ¡Actualiza!
```

### Paso 6: Escribir un Buen `README.md`

La "cara" de tu proyecto.

```markdown
# Mi-Calculadora

[![PyPI version](https://badge.fury.io/py/mi-calculadora.svg)](https://badge.fury.io/py/mi-calculadora)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Librería Python simple con operaciones matemáticas básicas (suma, resta, multiplicación, división).

## Instalación

Instala desde PyPI usando pip:

```bash
pip install mi-calculadora
```

## Uso Básico

```python
import mi_calculadora

# Operaciones
suma = mi_calculadora.sumar(10, 5)  # 15
resta = mi_calculadora.restar(10, 5)  # 5
multi = mi_calculadora.multiplicar(10, 5)  # 50
div = mi_calculadora.dividir(10, 5)  # 2.0

print(f"Suma: {suma}, Resta: {resta}, Multi: {multi}, Div: {div}")

# Manejo de errores
try:
    mi_calculadora.dividir(10, 0)
except ValueError as e:
    print(f"Error: {e}")  # Error: No se puede dividir por cero.

# Versión
print(f"Versión: {mi_calculadora.__version__}")  # 0.1.0 (o la versión actual)
```

## Licencia

Distribuido bajo la Licencia Apache 2.0. Ver `LICENSE` para más información.

## Contribuciones

Proyecto de ejemplo. Issues bienvenidos en GitHub (ver URL en `pyproject.toml`).
```

### Paso 7: Configurar y Usar un Entorno Virtual

Aísla las dependencias de tu proyecto.

```bash
# Navega a la raíz de tu proyecto en cmd o PowerShell
cd C:\Proyectos\mi-calculadora-proyecto

# Crea un entorno virtual llamado 'venv'
python -m venv venv

# Activa el entorno virtual (para cmd en Windows)
venv\Scripts\activate

# Si estás usando PowerShell y hay problemas de permisos, ejecuta:
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# Y luego: venv\Scripts\Activate.ps1

# Tu prompt debería cambiar, mostrando (venv) al principio
# Ejemplo: (venv) C:\Proyectos\mi-calculadora-proyecto>
```

### Paso 8: Instalar Herramientas de Build y Construir el Paquete

Dentro de tu entorno virtual activado (`(venv)` visible en el prompt):

1. Instala `build` usando `pip`:

```bash
pip install --upgrade build
```

2. Ejecuta el proceso de construcción:

```bash
python -m build
```

Esto creará (o actualizará) el directorio `dist/` con los archivos:
- `mi_calculadora-0.1.0.tar.gz` (sdist)
- `mi_calculadora-0.1.0-py3-none-any.whl` (wheel)

### Paso 9: Instalar Twine y Publicar en TestPyPI (Prueba)

¡Fundamental probar antes de publicar en el real!

1. Instala `twine`:

```bash
pip install --upgrade twine
```

2. Sube los archivos de `dist/` a TestPyPI:

```bash
twine upload --repository testpypi dist/*
```

Se te pedirá tu nombre de usuario y contraseña de TestPyPI.

**Seguridad**: Es mejor usar un API Token de TestPyPI. Genera uno en la configuración de tu cuenta de TestPyPI. Usa `__token__` como nombre de usuario y pega el token como contraseña.

### Paso 10: Probar la Instalación desde TestPyPI

Simula cómo un usuario instalaría tu paquete desde el repositorio de prueba. Hazlo en un entorno virtual limpio y separado.

```bash
# (Opcional) Desactiva el entorno actual
deactivate

# (Opcional) Crea y activa un nuevo entorno para la prueba
mkdir C:\Proyectos\test-mi-calculadora
cd C:\Proyectos\test-mi-calculadora
python -m venv test_env
test_env\Scripts\activate

# Instala tu paquete desde TestPyPI usando pip
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ mi-calculadora

# Abre el intérprete de Python
python
```

Dentro del intérprete de Python:

```python
>>> import mi_calculadora
>>> mi_calculadora.sumar(99, 1)
100
>>> mi_calculadora.__version__
'0.1.0'
>>> exit()
```

Si todo funciona correctamente, ¡procede a la publicación oficial!

### Paso 11: Publicar en PyPI (Oficial)

Ahora, publica tu librería en el repositorio principal de PyPI.

1. Verifica: Revisa que los archivos en `dist/` (el `tar.gz` y el `.whl`) correspondan a la versión `0.1.0` (o la que deseas publicar). Si hiciste cambios, borra `dist/` y vuelve a ejecutar `python -m build`.

2. Sube a PyPI oficial:

```bash
twine upload dist/*
```

Se te pedirá tu nombre de usuario y contraseña de PyPI (el real).

**Seguridad**: Nuevamente, se recomienda usar un API Token generado desde tu cuenta de PyPI. Usuario: `__token__`, Contraseña: el token.

### ¡Advertencia Crucial!
- No puedes volver a subir la misma versión (ej. `0.1.0`) a PyPI.
- Eliminar paquetes/versiones de PyPI es difícil.
- Para actualizaciones o correcciones, incrementa la versión en `pyproject.toml` y `src/mi_calculadora/__init__.py` (e.g., a `0.1.1`), reconstruye (`python -m build`) y repite el `twine upload dist/*`.

### Paso 12: Verificar la Publicación Final

1. Espera unos minutos y visita `https://pypi.org/project/mi-calculadora/`. Verifica que la página muestra la información correcta (README, licencia, etc.).

2. Realiza una instalación final en un entorno virtual limpio:

```bash
# (En un nuevo entorno virtual limpio y activado)
pip install mi-calculadora

# Prueba en Python
python
>>> import mi_calculadora
>>> print(mi_calculadora.dividir(10, 2))
5.0
>>> exit()
```

## Solución de Problemas Comunes en Windows

### 1. Problemas de Activación del Entorno Virtual

**Problema**: "No se puede ejecutar este script en el sistema actual..."

**Solución**: Ejecuta en PowerShell como administrador:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 2. Problemas con Python en PATH

**Problema**: "python no se reconoce como un comando interno o externo..."

**Solución**: 
- Asegúrate de que marcaste "Add Python to PATH" durante la instalación
- O añade manualmente Python a tu PATH:
  1. Busca "Variables de entorno" en el menú de Windows
  2. Edita la variable PATH
  3. Añade las rutas a Python y Python\Scripts

### 3. Problemas con la Construcción del Paquete

**Problema**: Errores durante `python -m build`

**Solución**:
- Verifica la estructura correcta del proyecto
- Comprueba que `pyproject.toml` está correcto y bien formateado
- Actualiza setuptools: `pip install --upgrade setuptools wheel`

### 4. Problemas con la Subida a PyPI

**Problema**: Errores de autenticación con `twine`

**Solución**:
- Verifica tus credenciales
- Utiliza tokens API en lugar de contraseñas
- Utiliza el archivo `.pypirc` en tu directorio home:

```
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-API-TOKEN

[testpypi]
username = __token__
password = testpypi-API-TOKEN
```

## Conclusión

¡Enhorabuena! Has seguido los pasos para crear, empaquetar y publicar tu librería `mi-calculadora` en PyPI desde un entorno Windows, usando las mejores prácticas con entornos virtuales. Tu librería está ahora disponible para la comunidad Python.

Recuerda la importancia de mantener tu librería, añadir pruebas (`tests/`), y gestionar versiones adecuadamente para futuras actualizaciones.

## Preguntas Críticas para Reflexionar

1. **Sostenibilidad y Mantenimiento**: ¿Cómo planeas gestionar los reportes de errores (issues) y las solicitudes de nuevas funcionalidades (feature requests) a largo plazo? ¿Tienes el tiempo y los recursos para mantener la librería actualizada con nuevas versiones de Python y posibles cambios en sus dependencias?

2. **Valor y Audiencia**: ¿Qué problema específico resuelve tu librería que no esté ya cubierto por otras librerías existentes? ¿Cómo te asegurarás de que la librería siga siendo relevante y útil para tu audiencia objetivo a medida que el ecosistema Python evoluciona?

3. **Calidad y Robustez**: Más allá de la funcionalidad básica, ¿qué medidas adicionales (como pruebas unitarias exhaustivas con `pytest` o `unittest`, integración continua (CI/CD) con GitHub Actions/GitLab CI, documentación detallada generada con Sphinx, ejemplos de uso avanzados) implementarás para asegurar la calidad, fiabilidad y facilidad de uso de tu librería, fomentando así su adopción?
