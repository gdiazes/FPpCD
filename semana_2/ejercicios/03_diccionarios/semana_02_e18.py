Ejercicio 18: Anidamiento de Diccionarios (Nivel 3)
Objetivo: Trabajar correctamente con diccionarios anidados.
Código con errores:
pythonCopiarusuarios = {
    "alice": {"email": "alice@example.com", "rol": "admin"},
    "bob": {"email": "bob@example.com", "rol": "usuario"}
}

print(f"Email de Alice: {usuarios['alice']['correo']}")
usuarios["charlie"] = {"correo": "charlie@example.com"}
usuarios["bob"]["permisos"] = ["leer", "escribir"]
print(usuarios["charlie"]["rol"])
Pistas:

Asegúrate de que las claves que intentas acceder existan.
Mantén consistencia en los nombres de las claves.
Si accedes a una clave que podría no existir, considera un valor por defecto.