rango = range (0,11)
print(type(rango))
#For por rangos, no incluye el ultimo, osea el 11 en este cao
for i in rango:
    print(i)

#For por cadena de caracteres
nombre = "tomas"
for letra in nombre:
    print(letra)
    
#For de oraciones
frase = "En un lugar de la mancha"
cucu = frase.split(" ")
#Insertar en una cadena de caracteres, o array de caracteres en este caso
cucu.insert(1, "cucululu")
for word in cucu:
    print(word)
# f'{}' es para usar el valor de una variable dentro de un string, lo mismo que ${} en JS, solo que la f (o format) va antes de crear el string
for i, valor in enumerate(cucu):
    print(f'{i} => {valor}')
