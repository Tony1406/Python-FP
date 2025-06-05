# ------------------------------
# 📌 TIPOS DE DATOS BÁSICOS
# ------------------------------

# Enteros (int)
numero = 42

# Flotantes (float)
decimal = 3.14

# Booleanos (bool)
es_mayor = True  # o False

# Cadenas (str)
mensaje = "Hola, Python"

# None (como null o undefined)
nada = None

# ------------------------------
# 📌 COLECCIONES
# ------------------------------

# Lista (list) - como un Array en JS
lista = [1, 2, 3, "cuatro", True]

# Tupla (tuple) - como una lista inmutable
tupla = (10, 20, 30)

# Conjunto (set) - sin elementos duplicados
conjunto = {1, 2, 3, 3, 2}  # => {1, 2, 3}

# Diccionario (dict) - como un objeto literal o Map
persona = {
    "nombre": "Anthony",
    "edad": 22,
    "vive_en": "Madrid"
}

# ------------------------------
# 📌 OPERADORES
# ------------------------------

# Aritméticos
suma = 5 + 2
resta = 5 - 2
producto = 5 * 2
division = 5 / 2           # Devuelve float: 2.5
division_entera = 5 // 2   # Devuelve int: 2
modulo = 5 % 2             # Resto: 1
potencia = 2 ** 3          # 8

# Comparación
igual = 5 == 5
diferente = 5 != 3
mayor = 5 > 2
menor = 5 < 10
mayor_igual = 5 >= 5
menor_igual = 5 <= 6

# Lógicos
and_logico = True and False
or_logico = True or False
not_logico = not True

# Asignación
x = 10
x += 5  # x = x + 5

# Identidad
a = [1, 2]
b = a
c = [1, 2]
es_igual = a == c      # True (compara contenido)
es_mismo = a is c      # False (compara referencia)

# Pertenencia
existe = 2 in [1, 2, 3]       # True
no_existe = "z" not in "hola"  # True

# ------------------------------
# 📌 DELIMITADORES Y SINTAXIS
# ------------------------------

# No hay llaves {}. Se usa indentación obligatoria (4 espacios o tab bien configurado).
# Los bloques terminan por indentación, no por símbolos.
# Punto y coma es innecesario (pero lo puedes usar si quieres... no lo hagas).

# Ejemplo: Condicional
edad = 22
if edad >= 18:
    print("Eres mayor de edad")
elif edad == 17:
    print("Casi casi...")
else:
    print("Eres menor de edad")

# Ejemplo: Bucle for
for numero in [1, 2, 3]:
    print("Número:", numero)

# Ejemplo: Bucle while
contador = 0
while contador < 3:
    print("Contando:", contador)
    contador += 1

# ------------------------------
# 📌 FUNCIONES
# ------------------------------

def saludar(nombre):
    return f"Hola, {nombre}"

print(saludar("Anthony"))

# Función anónima (lambda)
al_cuadrado = lambda x: x * x
print(al_cuadrado(4))  # 16

# ------------------------------
# 📌 CLASES Y OBJETOS
# ------------------------------

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

anthony = Persona("Anthony", 22)
anthony.saludar()

# 🟩 Casting entre tipos primitivos

a = int("123")          # str → int
b = int(3.7)            # float → int (trunca a 3)
c = float("3.14")       # str → float
d = float(5)            # int → float
e = str(456)            # int → str
f = str(True)           # bool → str
g = bool(0)             # int → bool (False)
h = bool(1)             # int → bool (True)
i = bool("")            # str vacío → False
j = bool("hola")        # str no vacío → True

# 🟦 Casting entre colecciones

lista_desde_str = list("hola")             # ['h', 'o', 'l', 'a']
lista_desde_tupla = list((1, 2, 3))        # [1, 2, 3]
lista_desde_set = list({1, 2, 3})          # [1, 2, 3] (desordenado)

tupla_desde_lista = tuple([1, 2, 3])       # (1, 2, 3)
set_desde_lista = set([1, 2, 2, 3])        # {1, 2, 3}
dict_desde_lista = dict([["a", 1], ["b", 2]])  # {'a': 1, 'b': 2}
