Guía de Sincronización de Git para el Curso de Fundamentos de Python para Ciencia de Datos (4 semanas)
Estructura de carpetas recomendada
CopiarFPpCD/
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
Estrategia de sincronización semana a semana
Configuración inicial (antes de la primera clase)
bashCopiar# Clonar el repositorio del curso
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
Sincronización al inicio de cada semana
bashCopiar# Asegurarte de tener los últimos materiales del profesor
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
Sincronización diaria durante la semana
bashCopiar# Al inicio de cada sesión de estudio
git checkout mi-progreso
git pull origin main --no-rebase  # Obtener actualizaciones del profesor

# Guardar tu avance después de cada sesión importante
git add semana_X/soluciones/ejercicio_Y.py
git add semana_X/notebooks/mi_analisis.ipynb
git commit -m "Completa ejercicios de la sección Z"

# Subir tus avances a tu repositorio personal (opcional)
git push origin mi-progreso  # Si has configurado un fork
Etiquetas para seguir tu progreso
bashCopiar# Al completar una semana
git tag -a semana1-completada -m "Finaliza todos los ejercicios de la Semana 1"

# Al finalizar ejercicios importantes
git tag ejercicio-pandas-completo

# Ver tu progreso
git tag -l
Sincronización para situaciones específicas del curso
Trabajo en equipo para proyectos grupales (Semana 4)
bashCopiar# Crear rama para trabajo en equipo
git checkout -b equipo3-proyecto

# Añadir repositorio de compañero
git remote add companero https://github.com/companero/FPpCD.git

# Compartir avances con compañeros
git push origin equipo3-proyecto

# Integrar trabajo de compañeros
git pull companero equipo3-proyecto
Preparación para evaluaciones
bashCopiar# Etiquetar estado antes de evaluación
git tag -a pre-evaluacion-semana2 -m "Material preparado para evaluación"

# Crear rama para práctica de evaluación
git checkout -b practica-evaluacion semana2-completada
Sincronización entre computadora personal y laboratorio
bashCopiar# Antes de terminar en un equipo
git add semana_actual/soluciones/
git commit -m "Avance hasta ejercicio X"
git push origin mi-progreso

# Al comenzar en otro equipo
git pull origin mi-progreso
Solución de problemas comunes durante el curso
Conflictos en notebooks al sincronizar
bashCopiar# Instalar herramienta para manejar notebooks
pip install nbdime

# Ver diferencias específicas
nbdiff semana_2/notebooks/analisis_pandas.ipynb

# Si prefieres mantener tu versión pero incorporar actualizaciones
git checkout --ours semana_2/notebooks/analisis_pandas.ipynb
git add semana_2/notebooks/analisis_pandas.ipynb
Recuperar estado al inicio de un ejercicio
bashCopiar# Ver commits relacionados con un ejercicio específico
git log --grep="ejercicio" semana_3/

# Volver al estado inicial de un ejercicio
git checkout abc123^ -- semana_3/ejercicios/visualizacion.py
Mantener separadas las soluciones oficiales de las tuyas
bashCopiar# Si el profesor actualiza soluciones
git checkout main -- semana_1/soluciones_oficiales/
git commit -m "Obtiene soluciones oficiales para comparar"

Esta estructura y estrategia de sincronización están diseñadas específicamente para un curso de 4 semanas de Fundamentos de Python para Ciencia de Datos, facilitando:

Organización progresiva: Estructura por semanas que refleja el avance del curso
Separación clara: Materiales del profesor vs. tus soluciones personales
Facilidad de sincronización: Estrategias específicas para cada etapa del curso
Seguimiento del progreso: Sistema de etiquetas para marcar hitos completados
