class Trabajador:
    def __init__(self, nombre="", sueldo=1200.00, tipo=""):
        self._nombre = nombre
        self._sueldo = sueldo
        self._tipo = tipo
    
    def __str__(self):
        return f"Nombre: {self._nombre}, Sueldo: {self._sueldo}, Tipo: {self._tipo}"
    

class Administrativo(Trabajador):

    def __init__(self, nombre="", sueldo=1200.00, tipo="", MBA=False, area=""):
        super().__init__(nombre, sueldo, tipo)
        self.__area = area
        self.__MBA = MBA

    def __str__(self):
        return f"{super().__str__()}, Area: {self.__area}, MBA: {self.__MBA}"
    
    def func1(self):
        print(f"Soy {self._nombre} y soy {self._tipo} en el area de {self.__area}")


class Tecnico(Trabajador):
    def __init__(self, nombre="", sueldo=1200.00, tipo="", certificado="AWS", cod_machine=""):
        super().__init__(nombre, sueldo, tipo)
        self._certificado = certificado
        self.__cod_machine = cod_machine

    def __str__(self):
        return f"{super().__str__()}, Especialidad: {self.__especialidad}"
    
    def func1(self):
        print(f"Soy {self._nombre}, soy {self._tipo} y tengo el certificado {self._certificado}, y mi codigo de maquina es {self.__cod_machine}")

Trabajador1 = Trabajador("Juan", 1500.00, "Administrativo")
Administrativo1 = Administrativo("Pedro", 2000.00, "Administrativo", True, "Recursos Humanos")
Tecnico1 = Tecnico("Ana", 1800.00, "Tecnico", "Azure", "1234")

Administrativo1.func1()
Tecnico1.func1()

print()