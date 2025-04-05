Ejercicio 15: Sets de Objetos Complejos (Nivel 1)
Objetivo: Trabajar con sets que contienen objetos complejos.
Código con errores:
pythonCopiarclass Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

punto1 = Punto(1, 2)
punto2 = Punto(1, 2)
punto3 = Punto(3, 4)

puntos = {punto1, punto2, punto3}
print(f"Número de puntos únicos: {len(puntos)}")

for punto in puntos
    print(f"Punto: ({punto.x}, {punto.y})")
Pistas:

Por defecto, dos instancias de una clase son consideradas diferentes.
Para que los objetos sean únicos en un set, necesitas implementar métodos especiales.
Los bucles for en Python necesitan dos puntos.

