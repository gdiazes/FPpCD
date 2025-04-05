Ejercicio 19: Métodos de Diccionarios (Nivel 2)
Objetivo: Usar correctamente los métodos de diccionarios.
Código con errores:
pythonCopiarconfig = {"tema": "oscuro", "fuente": "Arial", "tamaño": 12}
config.actualizar({"tema": "claro"})
todas_claves = config.keys
claves_valores = config.elementos()

for clave, valor in claves_valores
    print(f"{clave}: {valor}")
    
if "margen" not in config.claves():
    config["margen"] = 10
Pistas:

El método para actualizar un diccionario no es .actualizar().
Para llamar métodos, necesitas usar paréntesis.
Los bucles for en Python necesitan dos puntos.