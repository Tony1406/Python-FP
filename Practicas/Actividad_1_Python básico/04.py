# 4. Para que un triángulo sea válido se tiene que cumplir que la suma de dos cualquiera de sus lados siempre tiene que ser mayor que el tercero(en todas sus combinaciones).
# a. Crear una función que reciba los tres lados y devuelva True si el triángulo es válido, y False si el triángulo no es válido
# b. Tras llamar a esta función si no es válido informar y si es válido, determinar si es equilatero(los tres lados iguales, isósceles(2 lados iguales y uno desigual, o escaleno, los tres lados distintos.

from triangulos04 import validarTriangulo

lado1 = int(input("Dame un lado : "))
lado2 = int(input("Dame otro lado : "))
lado3 = int(input("Dame un ultimo lado : "))
    
validarTriangulo(lado1,lado2,lado3)