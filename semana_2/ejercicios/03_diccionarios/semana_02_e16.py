Ejercicio 1: Creación y Acceso a Diccionarios (Nivel 5)
Objetivo: Crear y acceder correctamente a elementos de un diccionario.
Código con errores:
pythonCopiarpersona = {"nombre": "Laura", "edad": 28, "ciudad": "Barcelona"}
print("Nombre: " + persona["nombre"])
print("Profesión: " + persona["profesión"])
print("Ciudad: " + persona[2])
Pistas:

No puedes acceder a una clave que no existe sin manejar la excepción.
Los diccionarios se acceden por clave, no por índice numérico.
Considera usar .get() para valores que podrían no existir.