# -*- coding: utf-8 -*-
"""
Juego de Palabras Revueltas con Temporizador y Opciones Múltiples
Proyecto Final de Python Básico

Este programa implementa un juego donde el usuario debe identificar palabras
con letras revueltas, eligiendo entre opciones múltiples, dentro de un límite de tiempo.

NOTA: Este código contiene errores intencionales como ejercicio de depuración.
Encuentra y corrige los errores para hacer funcionar el programa.
"""
import random
import time
import threading
import os

def obtener_lista_palabras():
    # ERROR 1: Lista vacía (no hay palabras para jugar)
    palabras = ()  # Debería ser una lista, no una tupla vacía
    
    # ERROR 2: Faltan palabras importantes para el juego
    
    # ERROR 3: Las palabras tienen errores de ortografía
    palabras = ['pyton', 'programasion', 'computadora', 'algritmo',
                'desarollador', 'sofware', 'codificacion', 'tecnologia',
                'internet', 'navegador', 'interfas', 'variable', 'funsion']
    
    return

def seleccionar_palabra_aleatoria(palabras):
    # ERROR 1: Índice fuera de rango
    return palabras[len(palabras)]  # Debería usar random.choice o un índice válido
    
    # ERROR 2: No se importa la biblioteca necesaria
    return choice(palabras)  # Falta importar random o usar random.choice
    
    # ERROR 3: Se retorna la lista completa en lugar de una palabra
    return palabras

def revolver_palabra(palabra):
    # ERROR 1: No se convierte la palabra a lista
    random.shuffle(palabra)  # Debe convertir el string a lista antes de mezclar
    
    # ERROR 2: Error al unir las letras mezcladas
    letras_palabra = list(palabra)
    random.shuffle(letras_palabra)
    palabra_revuelta = letras_palabra  # Debería unir las letras con join
    
    # ERROR 3: Función incompleta (falta retornar)
    letras_palabra = list(palabra)
    random.shuffle(letras_palabra)
    palabra_revuelta = ''.join(letras_palabra)
    # Falta return palabra_revuelta

def obtener_intento_jugador():
    # ERROR 1: Mensaje confuso para el usuario
    intento = input("Escribe algo: ")  # Debería pedir al usuario que ordene la palabra
    
    # ERROR 2: No se limpia la entrada del usuario
    intento = input("Ordena la palabra: ")  # Falta strip() y lower()
    
    # ERROR 3: Faltan validaciones básicas
    intento = input("Ordena la palabra: ").strip().lower()
    # No se valida si el intento está vacío o si es la palabra "salir"
    
    return intento

def limpiar_pantalla():
    # ERROR 1: Comando no válido para limpiar la pantalla
    os.system('clear')  # No funciona en Windows
    
    # ERROR 2: No se detecta el sistema operativo
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')  # Debería usar os.name para detectar Windows ('nt')
    
    # ERROR 3: Error de sintaxis en la construcción ternaria
    os.system('cls' if os.name = 'nt' else 'clear')  # Debe usar == para comparación

def mostrar_temporizador(minutos, evento_fin):
    # ERROR 1: Conversión incorrecta de minutos a segundos
    segundos_totales = minutos  # Debería multiplicar por 60
    
    # ERROR 2: No se verifica si el evento está definido
    while segundos_totales > 0:  # Falta verificar "and not evento_fin.is_set()"
        time.sleep(1)
        segundos_totales -= 1
        mins = segundos_totales // 60
        segs = segundos_totales % 60
        print(f"\rTiempo restante: {mins:02d}:{segs:02d}", end="")
    
    # ERROR 3: No se utiliza tiempo real (imprecisión en el temporizador)
    segundos_totales = minutos * 60
    for i in range(segundos_totales, 0, -1):  # Debería usar time.time() para medir tiempo real
        mins = i // 60
        segs = i % 60
        print(f"\rTiempo restante: {mins:02d}:{segs:02d}", end="")
        time.sleep(1)
    
    print("\n¡TIEMPO TERMINADO!")
    evento_fin.set()

def generar_opciones(palabra_correcta, todas_palabras):
    # ERROR 1: No se incluye la palabra correcta en las opciones
    opciones = []  # Debería incluir palabra_correcta en la lista
    
    # ERROR 2: Pueden generarse opciones duplicadas
    opciones = [palabra_correcta]
    for i in range(4):
        palabra = random.choice(todas_palabras)  # Puede elegir la misma palabra varias veces
        opciones.append(palabra)
    
    # ERROR 3: No se manejan casos con pocas palabras disponibles
    opciones = [palabra_correcta]
    palabras_restantes = [p for p in todas_palabras if p != palabra_correcta]
    opciones.extend(random.sample(palabras_restantes, 4))  # Error si hay menos de 4 palabras
    
    random.shuffle(opciones)
    return opciones

def mostrar_opciones(opciones):
    # ERROR 1: Formato incorrecto para mostrar opciones
    print("\nOpciones:")
    print(opciones)  # Debería mostrar cada opción numerada
    
    # ERROR 2: Índice incorrecto para enumerar opciones
    print("\nOpciones:")
    for i, opcion in enumerate(opciones):  # Debería comenzar desde 1, no desde 0
        print(f"{i}. {opcion}")
    
    # ERROR 3: Error de sintaxis en f-string
    print("\nOpciones:")
    for i, opcion in enumerate(opciones, 1):
        print(f"{i. opcion}")  # Falta cerrar la llave antes del punto

def obtener_seleccion(opciones):
    # ERROR 1: No se maneja la entrada vacía (pista)
    seleccion = input("\nSelecciona una opción (1-5) o escribe la palabra completa: ").strip()
    
    # ERROR 2: Error en la validación del rango de opciones
    if seleccion.isdigit():
        if 0 <= int(seleccion) <= 5:  # El rango debería ser 1-5, no 0-5
            return opciones[int(seleccion)]  # Falta restar 1 al índice
    
    # ERROR 3: No se manejan excepciones
    seleccion = input("\nSelecciona una opción (1-5) o escribe la palabra completa: ").strip()
    if seleccion.isdigit() and 1 <= int(seleccion) <= 5:
        return opciones[int(seleccion) - 1]  # Puede causar IndexError
    return seleccion.lower()

def jugar_palabras_revueltas():
    limpiar_pantalla()
    print("=" * 50)
    print("  JUEGO DE PALABRAS REVUELTAS CON OPCIONES MÚLTIPLES")
    print("=" * 50)
    
    # ERROR 1: No se maneja el caso de nombre vacío
    nombre_jugador = input("\nIngresa tu nombre: ")
    
    # ERROR 2: Falta validación para la duración del juego
    minutos = int(input("\nElige la duración del juego (1-5 minutos): "))
    
    # ERROR 3: No se detiene correctamente el temporizador al final
    evento_fin_tiempo = threading.Event()
    hilo_temporizador = threading.Thread(target=mostrar_temporizador, args=(minutos, evento_fin_tiempo))
    hilo_temporizador.daemon = True
    hilo_temporizador.start()
    
    try:
        palabras = obtener_lista_palabras()
        puntuacion = 0
        intentos_maximos = 3
        
        while not evento_fin_tiempo.is_set():
            palabra = seleccionar_palabra_aleatoria(palabras)
            palabra_revuelta = revolver_palabra(palabra)
            
            opciones = generar_opciones(palabra, palabras)
            
            print(f"\n\nPalabra Revuelta: {palabra_revuelta}")
            mostrar_opciones(opciones)
            
            intentos = 0
            while intentos < intentos_maximos and not evento_fin_tiempo.is_set():
                intento_jugador = obtener_seleccion(opciones)
                
                if intento_jugador == "":
                    print(f"Pista: La palabra empieza con '{palabra[0]}' y termina con '{palabra[-1]}'")
                    continue
                
                if intento_jugador == "salir":
                    evento_fin_tiempo.set()
                    break
                
                if intento_jugador == palabra:
                    print("¡Felicidades! Adivinaste la palabra correcta.")
                    puntuacion += 1
                    break
                else:
                    intentos += 1
                    restantes = intentos_maximos - intentos
                    if restantes > 0:
                        print(f"Intento incorrecto. Te quedan {restantes} intentos.")
                    else:
                        print(f"Sin intentos restantes. La palabra correcta era: {palabra}")
    except KeyboardInterrupt:
        print("\n\nJuego interrumpido por el usuario.")
    finally:
        evento_fin_tiempo.set()
    
    # Falta: hilo_temporizador.join() para esperar a que el hilo termine
    
    limpiar_pantalla()
    print("\n" + "=" * 50)
    print(f"         FIN DEL JUEGO - RESULTADOS")
    print("=" * 50)
    print(f"\nJugador: {nombre_jugador}")
    print(f"Tiempo jugado: {minutos} minuto(s)")
    print(f"Puntuación final: {puntuacion} palabra(s) correcta(s)")
    
    if puntuacion > 0:
        print(f"\n¡Buen trabajo, {nombre_jugador}! Has conseguido una media de {puntuacion/minutos:.1f} palabras por minuto.")
    else:
        print(f"\n¡Ánimo, {nombre_jugador}! La próxima vez lo harás mejor.")
    
    print("\n¡Gracias por jugar!")

if __name__ == "__main__":
    jugar_palabras_revueltas()
