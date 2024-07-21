# CLASE:

class Robot:
    def __init__(self, nombre, modelo):
        self.nombre = nombre
        self.modelo = modelo
        self.modo = "descanso"
    # Establezco mi clase Robot y sus atributos >:3

    # Momento de los métodos, en este caso funciones o.o
    def cambiar_modo(self, nuevo_modo):
        modos_actuales = ["descanso", "trabajo", "reparacion", "exploracion"]
        if nuevo_modo in modos_actuales:
            self.modo = nuevo_modo
            print(str(self.nombre) + " ha cambiado al modo " + str(self.modo) + ".")
        else:
            print("Modo no válido.")

    def tarea(self):
        if self.modo == "trabajo":
            print(str(self.nombre) + " está realizando tareas de trabajo.")
        elif self.modo == "reparacion":
            print(str(self.nombre) + " está realizando tareas de reparación.")
        elif self.modo == "exploracion":
            print(str(self.nombre) + " está explorando nuevas áreas.")
        else:
            print(str(self.nombre) + " está modo " + str(self.modo) + ", no realiza tareas.")

        # Un extra para mi modelo, porque quería lucirlo xd ^^
    def Modelo(self):
        print("El modelo de " + str(self.nombre) + " es " + str(self.modelo) + ".")

# Uso de la clase
mi_robot = Robot("Fuuka2", "IDLE")
print(str(mi_robot.nombre) + ":")
mi_robot.Modelo()
mi_robot.cambiar_modo("trabajo")
mi_robot.tarea()
mi_robot.cambiar_modo("descanso")
mi_robot.tarea()