# 6. Crear una lista de dict, con la información ; nombre, apellidos, sexo, salario. Recorrer la lista e informar:
# a. Cuantas personas hay en la lista.
# b. Cuentas son Hombre y cuantas mujeres.
# c. Cuanto suman sus salarios.


personas = [
    {"nombre": "Carlos", "apellidos": "Ramírez Pérez", "sexo": "M", "salario": 2500},
    {"nombre": "María", "apellidos": "López Gómez", "sexo": "F", "salario": 3100},
    {"nombre": "Luis", "apellidos": "Martínez Díaz", "sexo": "M", "salario": 2800},
    {"nombre": "Ana", "apellidos": "Fernández Ruiz", "sexo": "F", "salario": 3300},
    {"nombre": "Jorge", "apellidos": "García Herrera", "sexo": "M", "salario": 2900},
    {"nombre": "Lucía", "apellidos": "Moreno Torres", "sexo": "F", "salario": 2700},
    {"nombre": "Pedro", "apellidos": "Sánchez Vega", "sexo": "M", "salario": 2600},
    {"nombre": "Elena", "apellidos": "Castro Romero", "sexo": "F", "salario": 3200},
    {"nombre": "Raúl", "apellidos": "Jiménez León", "sexo": "M", "salario": 3000},
    {"nombre": "Isabel", "apellidos": "Navarro Soto", "sexo": "F", "salario": 3400}
]


contadorPersonas = 0
contadorMujeres = 0
contadorHombres = 0
sumaSalario = 0
for info in personas:
    contadorPersonas += 1
    if info["sexo"] == "F":
        contadorMujeres += 1
    elif info["sexo"] == "M":
        contadorHombres += 1
    sumaSalario += info["salario"]

print(f"Existen {contadorPersonas} personas")
print(f"Existen {contadorMujeres} mujeres")
print(f"Existen {contadorHombres} Hombres")
print(f"El salario de todos suma {sumaSalario}")