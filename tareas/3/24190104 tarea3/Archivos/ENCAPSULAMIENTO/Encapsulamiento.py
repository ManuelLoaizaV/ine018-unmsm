class Jugador:
    def __init__(self, nombre, edad, equipo):
        self.__nombre = nombre  
        self.__edad = edad  
        self.__equipo = equipo  
    #Aquí usamos el metodo del encapsulamiento para que no varie el nombre , la edad y el equipo

    # Métodos 'get' para acceder a los atributos
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_equipo(self):
        return self.__equipo

    # Métodos 'set' para modificar los atributos
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def set_edad(self, nueva_edad):
        if nueva_edad > 0:  
            self.__edad = nueva_edad
        else:
            print("Edad inválida")

    def set_equipo(self, nuevo_equipo):
        self.__equipo = nuevo_equipo

# Uso del encapsulamiento
persona = Jugador("Rodrygo", 23, "Real Madrid")
print(persona.get_nombre())  
print(persona.get_edad())  
print(persona.get_equipo())  

persona.set_nombre("Lamile")
persona.set_edad(17)
persona.set_equipo("Barcelona")
print(persona.get_nombre())  
print(persona.get_edad())  
print(persona.get_equipo())  

persona.set_edad(-5)  
print(persona.get_edad())  