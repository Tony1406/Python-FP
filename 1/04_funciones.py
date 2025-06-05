#funcion que suma cosas
def sumar(op1, op2):
    return op1 + op2

def literal_genero(genero):
    if str(genero).upper() == "H":
        return "Hombre"
    elif str(genero).upper() == "M":
        return "Mujer"
    else:
        return "Genero incorrecto"
    
print(sumar(2,34))
print(sumar("Hola", " y Adios"))
print(literal_genero('m'))