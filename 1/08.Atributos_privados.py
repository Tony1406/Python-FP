class Producto: 
    def __init__(self, id, descripcion, precio):
        self.__id = id
        self.__descripcion = descripcion
        self.__precio = precio
    def getPrecio(self):
        return self.__precio
    def setPrecio(self,precio):
        self.__precio = precio
        
p1 = Producto(1,"Camisa", 45)
p1.setPrecio(123)
print(p1.__precio())
print(p1._Producto__precio)