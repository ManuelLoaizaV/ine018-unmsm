class Jugador:
    def __init__(self, nombre, edad, equipo):
        self.nombre = nombre
        self.edad = edad
        self.equipo = equipo
    
    def presentar(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Equipo: {self.equipo}"

# Clase que se deriva
class JugadorFutbol(Jugador):
    def __init__(self, nombre, edad, equipo, posicion, goles):
      
        super().__init__(nombre, edad, equipo)
        self.posicion = posicion
        self.goles = goles

    def presentar(self):
        return f"{super().presentar()}, Posición: {self.posicion}, Goles: {self.goles}"

    def cambiar_posicion(self, nueva_posicion):
        self.posicion = nueva_posicion

# Creamos objetos de JugadorFutbol
lionel_messi = JugadorFutbol("Lionel Messi", 37, "Inter Miami", "Delantero", 23)
cristiano_ronaldo = JugadorFutbol("Cristiano Ronaldo", 39, "Al Nassr", "Delantero", 700)

# Presentamos los detalles de los jugadores
print(lionel_messi.presentar())
print(cristiano_ronaldo.presentar())
# Cambiamos la posición de Messi
lionel_messi.cambiar_posicion("Extremo Izquierdo")
# Cambiamos la posición de Cristiano 
cristiano_ronaldo.cambiar_posicion("Extremo Derecho")
#Vemos los cambios
print(lionel_messi.presentar())
print(cristiano_ronaldo.presentar())