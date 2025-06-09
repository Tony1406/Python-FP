def validarTriangulo(a, b, c):
    sumaLado1_2 = a + b
    sumaLado2_3 = b + c
    sumaLado3_1 = c + a
    
    if sumaLado1_2 > c or sumaLado2_3 > a or sumaLado3_1 > b:
        print("Es un triangulo valido")
        if a == b and b == c:
            print("equilatero")
            return True
        elif a != b and b != c:
            print("escaleno")
            return True
        elif a == b and b != c or a != b and b == c:
            print("isósceles")
            return True
    else:
        print("no es un triangulo valido")
        return False