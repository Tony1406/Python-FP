# 4. Para que un triángulo sea válido se tiene que cumplir que la suma de dos cualquiera de sus lados siempre tiene que ser mayor que el tercero(en todas sus combinaciones).
# a. Crear una función que reciba los tres lados y devuelva True si el triángulo es válido, y False si el triángulo no es válido
# b. Tras llamar a esta función si no es válido informar y si es válido, determinar si es equilatero(los tres lados iguales, isósceles(2 lados iguales y uno desigual, o escaleno, los tres lados distintos.

lado1 = int(input("Dame un lado : "))
lado2 = int(input("Dame otro lado : "))
lado3 = int(input("Dame un ultimo lado : "))

def validarTriangulo(a, b, c):
    sumaLado1_2 = a + b
    sumaLado2_3 = b + c
    sumaLado3_1 = c + a
    
    if sumaLado1_2 > lado3 or sumaLado2_3 > lado1 or sumaLado3_1 > lado2:
        print("Es un triangulo valido")
        if a == b and b == c:
            print("equilatero")
            return True
        elif a != b and b != c:
            print("escaleno")
            return True
        elif a == b and b != c:
            print("isósceles")
            return True
        elif a != b and b == c:
            print("isósceles")
            return True
    else:
        print("no es un triangulo valido")
        return False
    
validarTriangulo(lado1,lado2,lado3)