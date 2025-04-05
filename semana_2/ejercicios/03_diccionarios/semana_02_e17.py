Ejercicio 17: Modificación de Diccionarios (Nivel 4)
Objetivo: Modificar correctamente un diccionario.
Código con errores:
pythonCopiarestudiante = {"nombre": "Carlos", "calificaciones": [85, 90, 78]}
estudiante.agregar("edad", 22)
estudiante["calificaciones"].agregar(92)
promedio = sum(estudiante.calificaciones) / len(estudiante.calificaciones)
print(f"Promedio de {estudiante['nombre']}: {promedio}")
Pistas:

No existe un método .agregar() para diccionarios.
Las listas tienen un método específico para añadir elementos.
Para acceder a un valor del diccionario, usa la notación de corchetes.