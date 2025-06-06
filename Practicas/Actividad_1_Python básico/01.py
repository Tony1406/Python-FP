# 1. Leemos por consola dos números enteros y calculamos y mostramos por la consola:
# a. La suma
# b. La resta
# c. El producto
# d. La división
# e. La división entera
# f. El resto de su división

numero1 = 3
numero2 = 5

def sumar(op1, op2):
    return op1 + op2

def resta(op1, op2):
    return op1 - op2

def producto(op1, op2):
    return op1 * op2

def división(op1, op2):
    return op1 / op2

def divisiónEntera(op1, op2):
    return op1 // op2

def resto(op1, op2):
    return op1 % op2

print(f" La suma es : {sumar(numero1, numero2)}")
print(f" La resta es : {resta(numero1, numero2)}")
print(f" El producto es : {producto(numero1, numero2)}")
print(f" La division es : {división(numero1, numero2)}")
print(f" La división entera es : {divisiónEntera(numero1, numero2)}")
print(f" El resto es : {resto(numero1, numero2)}")