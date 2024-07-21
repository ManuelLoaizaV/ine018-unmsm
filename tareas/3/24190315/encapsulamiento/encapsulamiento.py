#ENCAPSULAMIENTO
class Persona:
    def __init__(self):
        self.__nombre = "Alejandro Perales Yuyes"

    def __saludar(self):
        print("Alumno de la escuela profesional de Ingeniería Biomédica")

    def mostrar_nombre(self):
        return self.__nombre
    
    def saludar(self):
        self.__saludar()

alumno = Persona()
alumno.saludar()
print(alumno.mostrar_nombre())