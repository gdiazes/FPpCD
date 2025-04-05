Ejercicio 3: Verificación de Elementos (Nivel 3)
Objetivo: Verificar la presencia de elementos en un set.
Código con errores:
pythonCopiarcolores = {"rojo", "verde", "azul"}
if "amarillo" in colores
    print("El amarillo está presente")
else
    print("El amarillo no está presente")
    
colores.add("amarillo")
colores.remove("violeta")
print(colores.has("amarillo"))
Pistas:

Los bloques condicionales en Python necesitan dos puntos.
No puedes eliminar un elemento que no existe en el set sin manejar la excepción.
Los sets no tienen un método .has().