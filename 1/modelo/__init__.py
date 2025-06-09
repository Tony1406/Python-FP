class Persona:
    
    def __init__(self, nombre, apellido, sexo, salario):
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.salario = salario
        
        
    def literal_sexo(self):
        if self.sexo == "H":
            return "Hombre"
        else:
            return "Mujer"
        
    def nombre_completo(self):
        return self.nombre + "" + self.apellido
        
    def __str__(self):
        return "nombre : " + self.nombre
    
    def __eq__(self, value: object):
        if self == object:
            return True
        if self.nombre == object.nombre:
            return True
        return False
        