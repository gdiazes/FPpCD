Ejercicio 20: Diccionarios por Comprensión (Nivel 1)
Objetivo: Utilizar correctamente la comprensión de diccionarios.
Código con errores:
pythonCopiarnumeros = range(1, 6)
cuadrados = {x, x**2 for x in numeros}
filtrados = {k: v for k, v in cuadrados if v > 10}
invertido = {valor, clave for clave, valor in cuadrados.items}
print(f"Cuadrados: {cuadrados}")
print(f"Filtrados (valor > 10): {filtrados}")
print(f"Invertido: {invertido}")
Pistas:

La sintaxis de comprensión de diccionarios requiere dos puntos entre clave y valor.
Los métodos necesitan paréntesis para ser ejecutados.
La comprensión de diccionarios al invertirlo también requiere dos puntos.