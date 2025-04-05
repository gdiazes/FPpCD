Ejercicio 14: Conjuntos Inmutables (Nivel 2)
Objetivo: Trabajar correctamente con frozensets.
Código con errores:
pythonCopiarinmutable = frozenset(["a", "b", "c"])
inmutable.add("d")
mutable = set(inmutable)
mutable.update({"d", "e", "f"})
resultado = inmutable & mutable
print(f"Conjunto inmutable: {inmutable}")
print(f"Conjunto mutable: {mutable}")
print(f"Intersección: {resultado}")
Pistas:

Los frozensets son inmutables, no se pueden modificar.
& es un operador válido para la intersección de sets.
Revisar la lógica de las operaciones.