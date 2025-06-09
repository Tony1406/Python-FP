s = "  hola mundo desde python  "

# upper: Convierte todo el texto a mayúsculas
print(s.upper())  # "  HOLA MUNDO DESDE PYTHON  "

# lower: Convierte todo el texto a minúsculas
print(s.lower())  # "  hola mundo desde python  "

# capitalize: Convierte la primera letra en mayúscula y el resto en minúscula
print(s.capitalize())  # "  hola mundo desde python  " (los espacios no afectan)

# title: Convierte la primera letra de cada palabra en mayúscula
print(s.title())  # "  Hola Mundo Desde Python  "

# strip: Elimina espacios (u otros caracteres) al inicio y al final
print(s.strip())  # "hola mundo desde python"

# replace: Reemplaza una subcadena por otra
print(s.replace("python", "el infierno"))  # "  hola mundo desde el infierno  "

# find: Devuelve el índice de la primera aparición de una subcadena, o -1 si no existe
print(s.find("mundo"))  # 7

# split: Divide el string en una lista según un separador (espacio por defecto)
print(s.split())  # ['hola', 'mundo', 'desde', 'python']

# join: Une una lista de strings con el string como separador
lista = ['uno', 'dos', 'tres']
print("-".join(lista))  # "uno-dos-tres"

# startswith: Devuelve True si el string comienza con la subcadena dada
print(s.strip().startswith("hola"))  # True

# endswith: Devuelve True si el string termina con la subcadena dada
print(s.strip().endswith("python"))  # True

# len: Devuelve la longitud del string (número de caracteres)
print(len(s))  # 28

# count: Cuenta cuántas veces aparece una subcadena
print(s.count("o"))  # 3
