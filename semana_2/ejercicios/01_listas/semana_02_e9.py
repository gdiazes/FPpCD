Ejercicio 9: Listas como Parámetros (Nivel 2)
Objetivo: Manipular listas como parámetros de funciones.
Código con errores:
pythonCopiardef agregar_elemento(lista, elemento):
    lista.add(elemento)
    return lista

def multiplicar_lista(lista, factor)
    resultado = []
    for elemento in lista
        resultado.append(elemento * factor)
    return resultado

mi_lista = [1, 2, 3]
print(agregar_elemento(mi_lista, 4))
print(multiplicar_lista(mi_lista, 2))
Pistas:

Las listas no tienen un método .add().
Las funciones en Python necesitan dos puntos después de la declaración.
Los bucles for en Python necesitan dos puntos después de la declaración.