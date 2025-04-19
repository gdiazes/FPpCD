## Curso Básico de Python

## 1. Planificación del Proyecto

### Objetivo del Proyecto
Crear un juego educativo de palabras revueltas en Python que permita a los jugadores adivinar palabras con letras desordenadas, seleccionando entre opciones múltiples, dentro de un tiempo limitado.

### Descripción General
El proyecto consiste en desarrollar un juego de terminal que presenta palabras con letras en orden aleatorio. El jugador debe identificar la palabra correcta entre cinco opciones posibles. El juego incluye un temporizador configurable, sistema de puntuación y la posibilidad de obtener pistas.

### Requisitos del Proyecto

#### Requisitos Funcionales
1. El juego debe mostrar palabras con letras en orden aleatorio.
2. El jugador debe poder ver 5 opciones posibles para cada palabra revuelta.
3. El jugador debe poder seleccionar una opción por número o escribiendo la palabra completa.
4. El juego debe permitir configurar un temporizador de 1 a 5 minutos.
5. El juego debe registrar el nombre del jugador.
6. El jugador debe tener 3 intentos por cada palabra presentada.
7. El juego debe llevar un registro de la puntuación obtenida.
8. El juego debe proporcionar pistas cuando el jugador lo solicite.
9. El jugador debe poder finalizar el juego anticipadamente si lo desea.

#### Requisitos Técnicos
1. El programa debe funcionar en cualquier plataforma que soporte Python 3.x.
2. El juego debe ser totalmente operable mediante la terminal o consola.
3. La interfaz debe ser clara y fácil de entender para principiantes.
4. El código debe manejar adecuadamente las posibles entradas incorrectas del usuario.

### Casos de Uso

**Caso 1: Jugar una partida completa**
- El jugador inicia el juego y proporciona su nombre.
- Selecciona la duración de la partida (entre 1 y 5 minutos).
- El juego muestra palabras revueltas con opciones múltiples.
- El jugador selecciona respuestas hasta que se agota el tiempo.
- Al finalizar, recibe su puntuación total.

**Caso 2: Solicitar pista durante el juego**
- Cuando se muestra una palabra difícil, el jugador puede presionar ENTER sin escribir nada.
- El juego revela la primera y última letra de la palabra correcta como ayuda.

**Caso 3: Finalizar el juego manualmente**
- En cualquier momento, el jugador puede escribir "salir".
- El juego termina y muestra la puntuación final obtenida hasta ese momento.

### Herramientas Necesarias
- Python 3.x
- Editor de código (como IDLE, PyCharm o Visual Studio Code)
- Terminal o consola del sistema

## 2. Diseño del Programa

### Estructura General
Para este proyecto de fin de curso, vamos a diseñar un programa que sea modular y fácil de entender. El diseño se basa en funciones independientes que trabajan juntas para crear el juego completo.

### Componentes Principales

1. **Gestión de Palabras**
   - Funciones para obtener la lista de palabras
   - Función para seleccionar palabras aleatorias
   - Función para revolver las letras de una palabra
   - Función para generar las opciones múltiples

2. **Interfaz de Usuario**
   - Funciones para mostrar mensajes al usuario
   - Funciones para obtener la entrada del usuario
   - Función para limpiar la pantalla

3. **Sistema de Temporizador**
   - Función para controlar el tiempo de juego
   - Función para mostrar el tiempo restante

4. **Sistema de Puntuación**
   - Funciones para registrar aciertos
   - Funciones para mostrar resultados finales

### Diagrama de Flujo del Programa

```
Inicio → Pedir nombre del jugador → Configurar duración →
Mientras (tiempo > 0):
    Seleccionar palabra aleatoria →
    Revolver letras →
    Generar opciones múltiples →
    Mostrar palabra y opciones →
    Esperar respuesta del usuario →
    Verificar respuesta →
    Actualizar puntuación
Fin del tiempo → Mostrar puntuación final
```

### Bibliotecas a Utilizar

El juego utilizará las siguientes bibliotecas de Python:

- **random**: Para seleccionar palabras aleatoriamente y mezclar letras
- **time**: Para manejar el tiempo y crear pausas
- **threading**: Para ejecutar el temporizador en paralelo a la interfaz
- **os**: Para limpiar la pantalla en diferentes sistemas operativos
- **json** (opcional): Para guardar puntuaciones

### Estructuras de Datos

Para este proyecto utilizaremos varias estructuras de datos básicas:

1. **Lista de palabras**: Una lista (array) simple que contiene todas las palabras disponibles en el juego.
   ```python
   palabras = ['python', 'programacion', 'computadora', 'algoritmo', ...]
   ```

2. **Diccionario para puntuación**: Para almacenar información del jugador y su puntuación.
   ```python
   puntuacion = {'nombre': 'Juan', 'puntos': 10, 'tiempo_jugado': 3}
   ```

3. **Lista para historial de partidas**: Para llevar registro de cada palabra jugada.
   ```python
   historial = [
       {'palabra': 'python', 'adivinada': True, 'intentos': 1},
       {'palabra': 'algoritmo', 'adivinada': False, 'intentos': 3}
   ]
   ```

### Interfaz de Usuario

El juego tendrá una interfaz basada en texto que se mostrará en la terminal o consola:

1. **Pantalla de inicio**: Muestra el título del juego y pide información básica.
   ```
   ===========================================
     JUEGO DE PALABRAS REVUELTAS CON OPCIONES
   ===========================================
   
   Ingresa tu nombre: _
   Elige la duración del juego (1-5 minutos): _
   ```

2. **Pantalla de juego**: Muestra la palabra revuelta, las opciones y el temporizador.
   ```
   Tiempo restante: 02:45
   
   Palabra Revuelta: THONPY
   
   Opciones:
   1. python
   2. programa
   3. código
   4. función
   5. lista
   
   Selecciona una opción (1-5) o escribe la palabra completa: _
   ```

3. **Pantalla final**: Muestra los resultados al terminar el juego.
   ```
   ===========================================
           FIN DEL JUEGO - RESULTADOS
   ===========================================
   
   Jugador: Juan
   Tiempo jugado: 3 minuto(s)
   Puntuación final: 8 palabra(s) correcta(s)
   
   ¡Buen trabajo! Has conseguido una media de 2.7 palabras por minuto.
   ```

## 3. Implementación del Código

### Estructura de Archivos
Para este proyecto de fin de curso crearemos un único archivo Python llamado `juego_palabras_revueltas.py` que contendrá todo el código necesario.

### Explicación de las Funciones Principales

1. **Funciones para Gestión de Palabras**

   ```python
   def obtener_lista_palabras():
       """
       Esta función retorna la lista de palabras disponibles para el juego.
       Contiene palabras relacionadas con programación y tecnología.
       """
       # Código para obtener y retornar una lista de palabras
   
   def seleccionar_palabra_aleatoria(palabras):
       """
       Esta función selecciona aleatoriamente una palabra de la lista proporcionada.
       """
       # Código para seleccionar una palabra al azar
   
   def revolver_palabra(palabra):
       """
       Esta función mezcla las letras de una palabra para crear un anagrama.
       """
       # Código para mezclar las letras de la palabra
   
   def generar_opciones(palabra_correcta, todas_palabras):
       """
       Esta función genera 5 opciones para mostrar al usuario,
       incluyendo la palabra correcta y 4 opciones aleatorias.
       """
       # Código para crear las opciones múltiples
   ```

2. **Funciones para Interfaz de Usuario**

   ```python
   def limpiar_pantalla():
       """
       Esta función limpia la pantalla de la terminal.
       Funciona tanto en Windows como en sistemas Unix/Linux.
       """
       # Código para limpiar la pantalla
   
   def mostrar_opciones(opciones):
       """
       Esta función muestra las opciones numeradas para que el usuario pueda seleccionar.
       """
       # Código para mostrar las opciones
   
   def obtener_intento_jugador():
       """
       Esta función obtiene la respuesta del usuario cuando intenta ordenar directamente.
       """
       # Código para obtener el intento del jugador
   
   def obtener_seleccion(opciones):
       """
       Esta función procesa la entrada del usuario, ya sea un número de opción
       o una palabra completa, y maneja casos especiales como pistas y salir.
       """
       # Código para procesar la selección del usuario
   ```

3. **Función del Temporizador**

   ```python
   def mostrar_temporizador(minutos, evento_fin):
       """
       Esta función muestra y controla un temporizador regresivo.
       Actualiza la pantalla cada segundo y señala cuando el tiempo termina.
       """
       # Código para mostrar y controlar el temporizador
   ```

4. **Función Principal del Juego**

   ```python
   def jugar_palabras_revueltas():
       """
       Función principal que controla todo el flujo del juego.
       Gestiona la interacción con el usuario, el temporizador,
       la generación de palabras y el sistema de puntuación.
       """
       # Código principal del juego
   ```

### Conceptos de Python Aplicados

En este proyecto se aplican varios conceptos fundamentales de Python:

1. **Variables y Tipos de Datos**: Strings, números, listas, diccionarios
2. **Estructuras de Control**: 
   - Condicionales (if/elif/else)
   - Bucles (while, for)
3. **Funciones**: Definición y llamada a funciones, parámetros y retorno de valores
4. **Manejo de Excepciones**: Try/except para validar entradas del usuario
5. **Trabajando con Módulos**: Importación y uso de bibliotecas como random, time, threading
6. **Operaciones con Cadenas**: Manipulación de strings para revolver palabras
7. **Operaciones con Listas**: Uso de funciones como append, extend, shuffle
8. **Entrada/Salida**: Interacción con el usuario mediante input/print
9. **Multithreading Básico**: Uso de hilos para el temporizador
10. **Formato de Strings**: Uso de f-strings para formatear texto
