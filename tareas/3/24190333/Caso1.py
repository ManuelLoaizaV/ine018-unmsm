class Persona:

    def __init__(self, name="", age=0, uid=""):
        self.__nombre = name
        self.__edad = age
        self.__dni = uid

    def __str__(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}, DNI: {self.__dni}"
    
    def set_Nombre(self, name):
        self.__nombre = name

    def get_Nombre(self):
        return self.__nombre
    
    def set_Edad(self, age):
        self.__edad = age
    
    def get_Edad(self):
        return self.__edad
    
    def set_DNI(self, uid):
        self.__dni = uid
    
    def get_DNI(self):
        return self.__dni
        
persona1 = Persona("Juan", 20, "12345678")

persona2 = Persona("Ana", 25, "87654321")

persona3 = Persona("Pedro", 30, "87654321")

print(persona1)
print(persona2)
print(persona3)

print()