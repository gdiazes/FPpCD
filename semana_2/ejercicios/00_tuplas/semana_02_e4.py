Ejercicio 4: Conversión de Tipos (Nivel 2)
Objetivo: Convertir correctamente entre tuplas y otros tipos de datos.
Código con errores:
pythonCopiarlista_numeros = [10, 20, 30, 40]
mi_tupla = tupla(lista_numeros)
mi_tupla.sort()
nueva_lista = lista(mi_tupla) + [50]
print(nueva_lista)
Pistas:

La función para convertir a tupla no se llama tupla().
Las tuplas no tienen método .sort().
La función para convertir a lista no se llama lista().