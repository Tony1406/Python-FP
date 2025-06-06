# 5. Pedir por consola el nombre, el apellido y el salario y el sexo(“H” o “M”) de una persona
# a. Escribir toda la información de lo tecleado de la siguiente forma:
# b. Nombre completo en mayúsculas + el literal de sexo: Hombre para H, Mujer para M + el literal del salario : Bajo si el salario es menor de 30.000; Medio entre 30.000 y 50.000; Alto si es mayor de 50.000.
# c. El nombre completo, el literal del sexo y el salario hacerlo en sendas funciones previas al algoritmo.

nombre = str(input("Dame un nombre : "))
apellido = str(input("Dame un apellido : "))
salario = int(input("Dame tu salario : "))
sexo = str(input("Dame tu sexo (H hombre, M mujer): "))

def informacionPersonal(nombre,apellido,salario,sexo):
    if salario < 30000:
        salario = "Bajo"
    elif salario > 30000 and salario < 50000:
        salario = "Medio"
    elif salario > 50000:
        salario = "Alto"
        
    if sexo == "M" or sexo == "m":
        sexo = "Mujer"
    elif sexo == "H" or sexo == "H":
        sexo = "Hombre"
    
    print(f"Mi nombre es : {nombre.upper()} {apellido.upper()} , mi sexo es : {sexo}, mi salario es {salario}")
    
informacionPersonal(nombre,apellido,salario,sexo)