class Jugador:
    def __init__(self, nombre, edad, equipo):
        self.nombre = nombre
        self.edad = edad
        self.equipo = equipo
    
    def accion(self):
        return f"{self.nombre} juega para el equipo {self.equipo}."

# Clase que se deriva
class JugadorFutbol(Jugador):
    def __init__(self, nombre, edad, equipo, posicion, goles):
        super().__init__(nombre, edad, equipo)
        self.posicion = posicion
        self.goles = goles

    def accion(self):
        return f"{self.nombre}, de {self.edad} años, juega como {self.posicion} para el equipo {self.equipo} y ha hecho {self.goles} goles."

# Otra clase derivada
class JugadorBasquetbol(Jugador):
    def __init__(self, nombre, edad, equipo, puntos, rebotes):
        super().__init__(nombre, edad, equipo)
        self.puntos = puntos
        self.rebotes = rebotes

    def accion(self):
        return f"{self.nombre}, de {self.edad} años, juega para el equipo {self.equipo} y ha hecho {self.puntos} puntos y {self.rebotes} rebotes en baloncesto."

# Función para mostrar la acción del jugador
def mostrar_accion(jugador):
    print(jugador.accion())

# Creamos objetos de los jugadores
futbolista = JugadorFutbol("Lionel Messi", 36, "Inter Miami", "Delantero", 750)
basquetbolista = JugadorBasquetbol("LeBron James", 39, "Los Angeles Lakers", 25000, 7000)

#Vemos las acciones
mostrar_accion(futbolista)
mostrar_accion(basquetbolista)