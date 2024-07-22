class DispositivoInteligente:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.estado = "apagado"
    # Establezco mi DispositivoInteligente y sus atributos

    # Momento de los métodos, en este caso funciones
    def cambiar_estado(self, nuevo_estado):
        estados_validos = ["apagado", "encendido", "reposo"]
        if nuevo_estado in estados_validos:
            self.estado = nuevo_estado
            print(f"{self.nombre} ha cambiado al estado {self.estado}.")
        else:
            print("Estado no válido.")

    def funcion(self):
        if self.estado == "encendido":
            print(f"{self.nombre} está en funcionamiento.")
        elif self.estado == "reposo":
            print(f"{self.nombre} está en modo de espera.")
        else:
            print(f"{self.nombre} está apagado, no realiza funciones.")

    def Tipo(self):
        print(f"El tipo de {self.nombre} es {self.tipo}.")

# Usamos la clase
mi_dispositivo = DispositivoInteligente("SIRI", "Asistente Virtual")
print(f"{mi_dispositivo.nombre}:")
mi_dispositivo.Tipo()
mi_dispositivo.cambiar_estado("encendido")
mi_dispositivo.funcion()
mi_dispositivo.cambiar_estado("reposo")
mi_dispositivo.funcion()
mi_dispositivo.cambiar_estado("apagado")
mi_dispositivo.funcion()