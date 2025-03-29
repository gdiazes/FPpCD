# Guía de Sincronización con Git para FPpCD

Esta guía está diseñada para estudiantes del curso de **Fundamentos de Python para Ciencia de Datos (FPpCD)** de 4 semanas. Te ayudará a mantener tu trabajo organizado y sincronizado a lo largo del curso.

## Estructura de carpetas recomendada

```
FPpCD/
├── semana_1/                 # Introducción a Python
│   ├── notebooks/            # Jupyter notebooks de la semana
│   ├── ejercicios/           # Ejercicios propuestos
│   ├── soluciones/           # Tus soluciones (gitignore por defecto)
│   ├── recursos/             # Material complementario
│   └── README.md             # Resumen de contenidos de la semana
│
├── semana_2/                 # Análisis de datos con NumPy y Pandas
│   ├── notebooks/
│   ├── ejercicios/
│   ├── soluciones/
│   ├── datasets/             # Datasets pequeños para práctica
│   └── README.md
│
├── semana_3/                 # Visualización de datos
│   ├── notebooks/
│   ├── ejercicios/
│   ├── soluciones/
│   ├── datasets/
│   ├── imagenes/             # Imágenes generadas
│   └── README.md
│
├── semana_4/                 # Introducción a Machine Learning
│   ├── notebooks/
│   ├── ejercicios/
│   ├── soluciones/
│   ├── datasets/
│   ├── modelos/              # Modelos entrenados
│   └── README.md
│
├── proyecto_final/           # Proyecto integrador
│   ├── datos/
│   ├── notebooks/
│   ├── resultados/
│   └── README.md
│
├── recursos_comunes/         # Recursos compartidos entre semanas
│   ├── datasets/             # Datasets utilizados en múltiples semanas
│   ├── utils/                # Funciones de utilidad comunes
│   └── cheatsheets/          # Guías rápidas de referencia
│
├── .gitignore                # Archivos a ignorar en el repositorio
├── environment.yml           # Entorno conda para el curso
└── README.md                 # Documentación principal del curso
```

## Instrucciones de sincronización para estudiantes

### Configuración inicial (antes de la primera clase)

Antes de comenzar el curso, configura tu entorno de trabajo:

```bash
# Clonar el repositorio del curso
git clone https://github.com/gdiazes/FPpCD.git
cd FPpCD

# Crear rama personal para tu trabajo
git checkout -b mi-progreso

# Crear estructura para tus soluciones (si no existe)
mkdir -p semana_1/soluciones semana_2/soluciones semana_3/soluciones semana_4/soluciones
touch semana_1/soluciones/.gitkeep

# Commit inicial de tu rama personal
git add .
git commit -m "Inicializa estructura para mis soluciones"
```

### Sincronización al inicio de cada semana

Al comenzar una nueva semana del curso, asegúrate de tener los materiales actualizados:

```bash
# Asegurarte de tener los últimos materiales del profesor
git checkout main
git pull origin main

# Actualizar tu rama personal con los nuevos materiales
git checkout mi-progreso
git merge main -m "Incorpora materiales de la semana X"

# Si hay conflictos, resolverlos manteniendo tus soluciones
git status
# Resolver conflictos manualmente...
git add archivos_resueltos
git commit -m "Resuelve conflictos de sincronización"
```

### Sincronización diaria durante la semana

Para tu trabajo diario, mantén estos hábitos:

```bash
# Al inicio de cada sesión de estudio
git checkout mi-progreso
git pull origin main --no-rebase  # Obtener actualizaciones del profesor

# Guardar tu avance después de cada sesión importante
git add semana_X/soluciones/ejercicio_Y.py
git add semana_X/notebooks/mi_analisis.ipynb
git commit -m "Completa ejercicios de la sección Z"

# Subir tus avances a tu repositorio personal (opcional)
git push origin mi-progreso  # Si has configurado un fork
```

### Seguimiento de tu progreso

Utiliza etiquetas para marcar hitos importantes:

```bash
# Al completar una semana
git tag -a semana1-completada -m "Finaliza todos los ejercicios de la Semana 1"

# Al finalizar ejercicios importantes
git tag ejercicio-pandas-completo

# Ver tu progreso
git tag -l
```

## Situaciones específicas

### Trabajo en equipo para proyectos grupales

Para colaborar en el proyecto final (Semana 4):

```bash
# Crear rama para trabajo en equipo
git checkout -b equipo3-proyecto

# Añadir repositorio de compañero
git remote add companero https://github.com/companero/FPpCD.git

# Compartir avances con compañeros
git push origin equipo3-proyecto

# Integrar trabajo de compañeros
git pull companero equipo3-proyecto
```

### Preparación para evaluaciones

Organiza tu trabajo antes de las evaluaciones:

```bash
# Etiquetar estado antes de evaluación
git tag -a pre-evaluacion-semana2 -m "Material preparado para evaluación"

# Crear rama para práctica de evaluación
git checkout -b practica-evaluacion semana2-completada
```

### Sincronización entre computadora personal y laboratorio

Para trabajar en diferentes equipos:

```bash
# Antes de terminar en un equipo
git add semana_actual/soluciones/
git commit -m "Avance hasta ejercicio X"
git push origin mi-progreso

# Al comenzar en otro equipo
git pull origin mi-progreso
```

## Solución de problemas comunes

### Conflictos en notebooks al sincronizar

Los notebooks Jupyter suelen generar conflictos al sincronizar:

```bash
# Instalar herramienta para manejar notebooks
pip install nbdime

# Ver diferencias específicas
nbdiff semana_2/notebooks/analisis_pandas.ipynb

# Si prefieres mantener tu versión pero incorporar actualizaciones
git checkout --ours semana_2/notebooks/analisis_pandas.ipynb
git add semana_2/notebooks/analisis_pandas.ipynb
```

### Recuperar estado al inicio de un ejercicio

Si necesitas volver al punto de partida de un ejercicio:

```bash
# Ver commits relacionados con un ejercicio específico
git log --grep="ejercicio" semana_3/

# Volver al estado inicial de un ejercicio
git checkout abc123^ -- semana_3/ejercicios/visualizacion.py
```

### Mantener separadas las soluciones oficiales de las tuyas

Para comparar tus soluciones con las oficiales:

```bash
# Si el profesor actualiza soluciones
git checkout main -- semana_1/soluciones_oficiales/
git commit -m "Obtiene soluciones oficiales para comparar"
```

## Ejemplo de .gitignore para el curso

```
# Python
__pycache__/
*.py[cod]
*$py.class
.pytest_cache/

# Jupyter Notebooks
.ipynb_checkpoints

# Entornos virtuales
venv/
env/
.env/

# Datos (opcional, ajustar según necesidades del curso)
*.csv
*.xlsx
semana_*/datasets/raw/
!recursos_comunes/datasets/*.csv  # Permitir datasets comunes

# Imágenes generadas
semana_*/imagenes/*.png
!semana_*/imagenes/ejemplo_*.png  # Mantener ejemplos

# Modelos
*.pkl
*.joblib
*.h5

# IDE
.vscode/
.idea/

# Archivos de sistema
.DS_Store
Thumbs.db
```

---

Esta guía está diseñada para ayudarte a mantener tu trabajo organizado durante las 4 semanas del curso FPpCD. Recuerda que Git es una herramienta poderosa para el seguimiento de tu progreso y te será muy útil en tu carrera profesional en ciencia de datos.

## Recursos adicionales

- [Pro Git Book](https://git-scm.com/book/es/v2)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [Jupyter Notebook Best Practices](https://jupyter.org/jupyter-book/guide/03_running.html)

**Última actualización:** Marzo 2025
