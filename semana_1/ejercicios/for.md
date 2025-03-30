¡Perfecto, Elliot! Aquí tienes una publicación en Markdown con los comentarios explicativos separados visualmente del código. Esta estructura es ideal para usar en GitHub, blogs técnicos o Notebooks educativos 🧠📘:

markdown
Copiar
Editar
# 🐍 Estructuras de Control en Python: `for`, `if`, `while`

Esta guía muestra cómo usar `for`, `if` y `while` en Python, con ejemplos que escalan de lo básico a lo complejo.  
Los comentarios explicativos están claramente separados del código para facilitar la lectura y comprensión.

---

## 🔁 Bucle `for`

---

### 🔹 Básico – Recorrer una lista

**📝 Descripción:** Recorre e imprime cada color en la lista.

```python
# Lista de colores
colores = ["rojo", "verde", "azul"]

# Recorremos la lista con un for
for color in colores:
    print("Color:", color)
🔸 Intermedio – Sumar números del 1 al 10
📝 Descripción: Usa un bucle for con range() para acumular una suma.

python
Copiar
Editar
# Inicializamos la suma
suma = 0

# Sumamos los números del 1 al 10
for numero in range(1, 11):
    suma += numero

print("La suma es:", suma)
🔺 Avanzado – Iterar una lista de diccionarios
📝 Descripción: Muestra el rol de cada usuario a partir de una lista de diccionarios.

python
Copiar
Editar
# Lista de usuarios con nombre y rol
usuarios = [
    {"nombre": "Elliot", "rol": "Programador"},
    {"nombre": "Mijael", "rol": "Músico"},
    {"nombre": "Luz", "rol": "Analista"}
]

# Recorremos la lista
for usuario in usuarios:
    print(f"{usuario['nombre']} es {usuario['rol']}")
🔍 Condicional if
🔹 Básico – Verificar si un número es positivo
📝 Descripción: Condición simple para validar si un número es mayor que cero.

python
Copiar
Editar
# Número de prueba
numero = 7

# Condicional para evaluar si es positivo
if numero > 0:
    print("El número es positivo")
🔸 Intermedio – Evaluar una nota
📝 Descripción: Evalúa una nota y muestra un mensaje según el rango.

python
Copiar
Editar
# Nota de estudiante
nota = 15

# Condiciones múltiples con elif
if nota >= 18:
    print("Excelente")
elif nota >= 14:
    print("Aprobado")
else:
    print("Desaprobado")
🔺 Avanzado – Filtrar usuarios activos
📝 Descripción: Imprime solo los usuarios que están activos.

python
Copiar
Editar
# Lista de usuarios con estado
usuarios = [
    {"nombre": "Elliot", "activo": True},
    {"nombre": "Luz", "activo": False},
    {"nombre": "Mijael", "activo": True}
]

# Verificamos si están activos
for usuario in usuarios:
    if usuario["activo"]:
        print(f"{usuario['nombre']} está activo")
🔄 Bucle while
🔹 Básico – Contar del 1 al 5
📝 Descripción: Ciclo que imprime números mientras una condición se cumple.

python
Copiar
Editar
# Inicializamos contador
contador = 1

# Repetimos mientras el contador sea menor o igual a 5
while contador <= 5:
    print("Contador:", contador)
    contador += 1
🔸 Intermedio – Validar contraseña
📝 Descripción: Solicita la contraseña hasta que sea la correcta.

python
Copiar
Editar
# Contraseña correcta
contraseña_correcta = "python123"
ingreso = ""

# Pedimos al usuario que ingrese hasta acertar
while ingreso != contraseña_correcta:
    ingreso = input("Ingresa la contraseña: ")

print("¡Acceso concedido!")
🔺 Avanzado – Juego de adivinanza con intentos limitados
📝 Descripción: Permite 3 intentos para adivinar un número secreto.

python
Copiar
Editar
# Número secreto
numero_secreto = 7
intentos = 0
max_intentos = 3

# Ciclo mientras queden intentos
while intentos < max_intentos:
    intento = int(input("Adivina el número (1-10): "))
    intentos += 1

    if intento == numero_secreto:
        print("🎉 ¡Correcto!")
        break
    else:
        print("❌ Incorrecto")

# Si se terminan los intentos y no acertó
if intentos == max_intentos and intento != numero_secreto:
    print("😢 Se acabaron los intentos.")
📌 Recomendaciones
Usa for cuando conozcas cuántas veces repetirás.

Usa while cuando no sepas cuántas repeticiones habrá.

Combina for o while con if para tomar decisiones dentro de bucles.
