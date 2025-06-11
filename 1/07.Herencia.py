class Persona: 
    numero = 23
    def __init__(self, id, nombre, edad):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self):
        return "Persona : [nombre + " + self.nombre + "]"
    
    def repr(self):
        return "Persona : [nombre + " + self.nombre + "]"
    
class Empleado(Persona):
    def __init__(self, id, nombre, edad, salario):
        super().__init__(id, nombre, edad)
        self.salario = salario
        
    def __str__(self):
        return "Empleado : nombre : " + self.nombre + " salario : " + str(self.salario)
    
    def __repr__(self):
        return "Empleado : nombre : " + self.nombre + " salario : " + str(self.salario)
    
p1 = Persona(12, "Tomas", 34)
e1 = Empleado(14, "Tomas", 23, 12000)

print(p1.nombre)
print(e1.salario)
print(Persona.numero)

lista = {p1, e1, Empleado(15, "Carlos", 65, 34000)}
dicc1 = {}

for ele in lista:
    print(ele.nombre)
    dicc1[ele.id] = ele
    if isinstance(ele, Empleado):
        print(ele.salario)
    
print(dicc1)