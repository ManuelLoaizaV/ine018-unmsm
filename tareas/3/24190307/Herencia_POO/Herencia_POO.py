#HERENCIA:

class Beacon: # Beacon es mi clase principal (Su academia uu)
    def __init__(self, nombre, edad, hogar, especie, semblanza, arma):
        self.nombre = nombre
        self.edad = edad
        self.hogar = hogar
        self.especie = especie
        self.semblanza = semblanza
        self.arma = arma

# Ahora creo mis clases con el team RWBY, con los mismos atributos de 'Beacon'
class Ruby(Beacon):
    def __init__(self, nombre, edad, hogar, especie, semblanza, arma, apodo):
        super().__init__(nombre, edad, hogar, especie, semblanza, arma)
        self.apodo = apodo
        # Ya no es necesario poner self, porque super() ya lo tiene incorporado, o eso leí
        # Y lo utilizamos porque añadimos otro atributo, que no estaba previamente en Beacon

    def Apodo(self):
       print(str(self.apodo))
        # Creando métodos distintos para diferenciarlas un poco uu
    
class Weiss(Beacon):
    def __init__(self, nombre, edad, hogar, especie, semblanza, arma, familia):
        super().__init__(nombre, edad, hogar, especie, semblanza, arma)
        self.familia = familia

    def Familia(self):
        print(str(self.familia))

class Blake(Beacon):
    def __init__(self, nombre, edad, hogar, especie, semblanza, arma, secreto):
        super().__init__(nombre, edad, hogar, especie, semblanza, arma)
        self.secreto = secreto

    def Secreto(self):
        print(str(self.secreto))

class Yang(Beacon):
    def __init__(self, nombre, edad, hogar, especie, semblanza, arma, brazo):
        super().__init__(nombre, edad, hogar, especie, semblanza, arma)
        self.brazo = brazo

    def Brazo(self):
        print(self.brazo)

# Modo Wiki Fandom xdxd
def imprimir_datos(personaje):
    print(" ⌂ " + str(personaje.__class__.__name__) +
          "\n Nombre completo: " + str(personaje.nombre) +
          "\n Edad: " + str(personaje.edad) +
          "\n Lugar de origen: " + str(personaje.hogar) +
          "\n Especie: " + str(personaje.especie) +
          "\n Semblanza: " + str(personaje.semblanza) +
          "\n Arma: " + str(personaje.arma) +
          "\n ⌂ Curiosidad:")

# El team RWBY!!!
ruby = Ruby("Ruby Rose", "15", "Patch (Vale)", "Humana", "Petal Burst", "Crescent Rose", 
            "  - Uno de sus rasgos más resaltantes es que tiene los ojos plateados como su madre.")

weiss = Weiss("Weiss Schnee", "17", "Atlas", "Humana", "Glyphs", "Myrtenaster", 
              "  - Proviene de una familia dueña de la famosa Schnee Dust Company, distribuidora de Dust.")

blake = Blake("Blake Belladonna", "17", "Isla de Menagerie", "Faunus", "Shadow", "Gambol Shroud", 
              "  - Cuando era más joven pertenecía a una organización llamada White Fang, pero luego huyó.")

yang = Yang("Yang Xiao Long", "17", "Patch (Vale)", "Humana", "Burn", "Ember Celica", 
            "  - Perdió su brazo derecho por proteger a Blake, ahora tiene uno de metal hecho en Atlas.")

imprimir_datos(ruby)
ruby.Apodo()
print("-------------------------------------------------------------------------------------")
imprimir_datos(weiss)
weiss.Familia()
print("-------------------------------------------------------------------------------------")
imprimir_datos(blake)
blake.Secreto()
print("-------------------------------------------------------------------------------------")
imprimir_datos(yang)
yang.Brazo()

# Que no se note que me gusta RWBY xdxd