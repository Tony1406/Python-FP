# 2. Leer consecutivamente dos números cada vez, hasta que los dos sean -1. Comparar los dos números leídos e informar cada vez si son iguales, mayor o menor (el primero  respecto al segundo). Al final del proceso informar cuantas veces los números eran
# iguales, cuantas veces el primero era mayor del segundo y cuantas veces el primero
# era menor del segundo número leído.

numero1 = int(input("Dime un numero "))
numero2 = int(input("Dime otro numero "))

contadorIguales = 0
contadorMayor = 0
contadorMenor = 0

while numero1 != -1 or numero2 != -1:
    if numero1 > numero2:
        print(f"{numero1} es mayor que {numero2}")
        contadorMayor += 1
    elif numero1 < numero2:
        print(f"{numero1} es menor que {numero2}")
        contadorMenor += 1
    elif numero1 == numero2:
        print("Son iguales")
        contadorIguales += 1
    numero1 = int(input("Dime nuevamente un numero "))
    numero2 = int(input("Dime nuevamente otro numero "))

print(f"La cantidad de veces que son iguales es :{contadorIguales} ")
print(f"La cantidad de veces que uno es mayor es :{contadorMayor} ")
print(f"La cantidad de veces que uno es menor es :{contadorMenor} ")