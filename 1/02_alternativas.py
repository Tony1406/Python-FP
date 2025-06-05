edad = int(input("Dime tu edad "))
if edad >= 18:
    print("eres mayor de edad")
else:
    print("eres menor de edad")
    
opcion = input("Mete una opcion (insert , update o delete) : ")

if opcion == "insert":
    print ("Añadiendo")
elif opcion == "update":
    print("Modificando")
elif opcion == "delete":
    print ("borrando")
else: 
    print("opcion erronea")    

print("CON MATCH")

match opcion:
    case 'insert':
        print("insertando")
    case 'update':
        print("modif")
    case 'delete':
        print("deleteando")
    case _:
        print("opcion erronea")
        