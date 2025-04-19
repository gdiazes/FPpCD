# Pistas para Corregir Errores en el Juego de Palabras Revueltas

Este documento proporciona pistas para ayudarte a identificar y corregir los errores en el código del juego de palabras revueltas. No se proporcionan soluciones directas para fomentar el aprendizaje a través del proceso de depuración.

## Función: obtener_lista_palabras()

**Pista 1:** 
¿Cuál es la diferencia entre una tupla `()` y una lista `[]` en Python? ¿Cuál necesitas para almacenar y poder modificar una colección de palabras?

**Pista 2:** 
Revisa cuidadosamente la lista de palabras. ¿Hay suficientes palabras para hacer el juego interesante? Si tuvieras que añadir más palabras relacionadas con programación, ¿cuáles incluirías?

**Pista 3:** 
Revisa la ortografía de las palabras en la lista. Algunas tienen errores que podrían confundir al jugador cuando intente adivinarlas.

**Pista de retorno:** 
La función no está devolviendo nada. ¿Qué debería devolver esta función? ¿Falta una instrucción final?

## Función: seleccionar_palabra_aleatoria(palabras)

**Pista 1:** 
En Python, las listas están indexadas desde 0 hasta len(lista)-1. ¿Qué ocurre si intentas acceder a palabras[len(palabras)]?

**Pista 2:** 
La función `choice()` no está disponible directamente. ¿Desde qué módulo debes importarla o qué prefijo debes usar para acceder a ella?

**Pista 3:** 
La función debe devolver una sola palabra aleatoria, no la lista completa de palabras. ¿Cómo puedes seleccionar un elemento aleatorio de una lista?

## Función: revolver_palabra(palabra)

**Pista 1:** 
`random.shuffle()` modifica la lista in-place, pero no puede modificar un string directamente. ¿Cómo puedes convertir un string a una estructura que pueda ser modificada por shuffle?

**Pista 2:** 
Después de mezclar las letras, debes convertir la lista de letras de nuevo a string. ¿Qué método de string puedes usar para unir una lista de caracteres?

**Pista 3:** 
¿Qué está faltando al final de la función para que devuelva la palabra revuelta?

## Función: obtener_intento_jugador()

**Pista 1:** 
El mensaje al usuario debe ser claro sobre lo que se espera que haga. ¿Cómo puedes mejorar "Escribe algo:" para indicar claramente que debe ordenar las letras de la palabra?

**Pista 2:** 
Las entradas de usuario pueden contener espacios en blanco al principio o final, y pueden tener diferentes casos (mayúsculas/minúsculas). ¿Qué métodos puedes usar para limpiar y normalizar la entrada?

**Pista 3:** 
¿Sería útil validar si el usuario ingresa una entrada vacía o si escribe "salir"? ¿Dónde pondrías esa validación?

## Función: limpiar_pantalla()

**Pista 1:** 
El comando 'clear' solo funciona en sistemas Unix/Linux. ¿Qué comando deberías usar para que funcione también en Windows?

**Pista 2:** 
Para detectar el sistema operativo, debes verificar el valor de `os.name`. ¿Qué valor tiene `os.name` en Windows y qué valor tiene en sistemas Unix/Linux?

**Pista 3:** 
Hay un error de sintaxis en la expresión ternaria. ¿Cuál es el operador correcto para comparar igualdad en Python?

## Función: mostrar_temporizador(minutos, evento_fin)

**Pista 1:** 
¿Cuántos segundos hay en un minuto? ¿Cómo debes convertir minutos a segundos?

**Pista 2:** 
La variable `evento_fin` se usa para señalar cuando el tiempo ha terminado o cuando el usuario quiere salir del juego. ¿Cómo debes verificar si este evento ha sido activado?

**Pista 3:** 
El enfoque de simplemente disminuir un contador cada segundo no es preciso porque no tiene en cuenta el tiempo que toma ejecutar el código. ¿Cómo puedes medir el tiempo real transcurrido?

## Función: generar_opciones(palabra_correcta, todas_palabras)

**Pista 1:** 
La lista de opciones debe incluir la palabra correcta. ¿Dónde debes añadirla y cuál es la mejor manera de hacerlo?

**Pista 2:** 
Si seleccionas palabras aleatorias una por una, podrías seleccionar la misma palabra varias veces. ¿Hay alguna función en el módulo random que pueda ayudarte a seleccionar elementos únicos?

**Pista 3:** 
¿Qué ocurre si hay menos de 4 palabras disponibles después de excluir la palabra correcta? ¿Cómo puedes manejar este caso para evitar un error?

## Función: mostrar_opciones(opciones)

**Pista 1:** 
Imprimir toda la lista de opciones de una vez no es muy legible para el usuario. ¿Cómo puedes mostrar cada opción en una línea separada con un número delante?

**Pista 2:** 
Si usas `enumerate()` sin argumentos adicionales, empezará a contar desde 0. ¿Cómo puedes hacer que empiece a contar desde 1?

**Pista 3:** 
Hay un error de sintaxis en la f-string. ¿Cómo debe ser la sintaxis correcta para incluir variables dentro de una f-string?

## Función: obtener_seleccion(opciones)

**Pista 1:** 
Si el usuario presiona ENTER sin escribir nada, ¿cómo puedes detectar esta entrada vacía y usarla para mostrar una pista?

**Pista 2:** 
Si el usuario ingresa un número entre 1 y 5, debes convertirlo a la opción correspondiente en la lista. ¿Cómo se relacionan los números que ve el usuario (1-5) con los índices de la lista (que empiezan en 0)?

**Pista 3:** 
¿Qué ocurre si el usuario ingresa un valor que no es un número válido o que está fuera del rango 1-5? ¿Cómo puedes manejar estos errores?

## Función: jugar_palabras_revueltas()

**Pista 1:** 
¿Qué ocurre si el usuario no ingresa un nombre y simplemente presiona ENTER? ¿Cómo puedes proporcionar un valor predeterminado en este caso?

**Pista 2:** 
¿Qué ocurre si el usuario ingresa un valor no numérico o un número fuera del rango 1-5 para la duración? ¿Cómo puedes validar esta entrada y manejar posibles errores?

**Pista 3:** 
El hilo del temporizador se inicia, pero no hay código para esperar a que termine antes de mostrar los resultados finales. ¿Qué método puedes usar para esperar a que un hilo termine?

## Consejos Generales para Depuración

1. **Ejecuta el código por partes**: Prueba cada función por separado para identificar exactamente dónde están los errores.

2. **Usa print para debugging**: Añade declaraciones `print()` estratégicamente para ver los valores de las variables en diferentes puntos del código.

3. **Lee los mensajes de error**: Los mensajes de error de Python suelen indicar exactamente dónde está el problema y dar pistas sobre cómo solucionarlo.

4. **Piensa en casos límite**: ¿Qué pasa si la lista de palabras está vacía? ¿Si el usuario no ingresa nada? Estos casos suelen revelar errores.

5. **Verifica tipos de datos**: Muchos errores ocurren cuando se mezclan diferentes tipos de datos. Verifica que estás usando el tipo correcto para cada operación.

¡Buena suerte con la depuración! Recuerda que encontrar y corregir errores es una parte importante del proceso de aprendizaje en programación.
