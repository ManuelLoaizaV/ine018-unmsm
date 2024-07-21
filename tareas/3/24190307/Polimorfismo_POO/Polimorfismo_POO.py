# POLIMORFISMO

class I_AM:
    def __init__(self, nombre, artista, fecha, numero_de_canciones, orden_de_mini_album):
        self.nombre = nombre
        self.artista = artista
        self.fecha = fecha
        self.numero_de_canciones = numero_de_canciones
        self.orden_de_mini_album = orden_de_mini_album
 # Sé que pude utilizar herencia, pero quería un archivo específico de cada pilar del POO
 # No le quería quitar protagonismo al Polimorfismo
    
    def descripcion (self): # Hago énfasis en que tengo un método que se llama 'descripcion'!!!!

        self.Lista_de_canciones = ["  1. LATATA", "  2. $$$ (Dollar)", "  3. Maze", "  4. Don't text me", 
                                   "  5. What's you name?", "  6. Hear me"]
        
        print(" Nombre del álbum: " + str(self.nombre) +
              "\n Artista: " + str(self.artista) +
              "\n Fecha de Lanzamiento: " + str(self.fecha) +
              "\n Fue el " + str(self.orden_de_mini_album) + " mini álbum del grupo" +
              "\n Consta de " + str(self.numero_de_canciones) + " canciones que son las siguientes: ")
        
        for i in range(len(self.Lista_de_canciones)):
            print(self.Lista_de_canciones[i])  

class I_BURN:
    def __init__(self, nombre, artista, fecha, numero_de_canciones, orden_de_mini_album):
        self.nombre = nombre
        self.artista = artista
        self.fecha = fecha
        self.numero_de_canciones = numero_de_canciones
        self.orden_de_mini_album = orden_de_mini_album
  
    def descripcion (self): # Hago énfasis en que tengo OTRO método que se llama 'descripcion'!!!!

        self.Lista_de_canciones = ["  1. HANN (Alone in the Winter)", "  2. HWAA (火花)", "  3. MOON", 
                                   "  4. Where is love?", "  5. Lost", "  6. DAHLIA"]  
                                    # La sexta uff xdxd
        
        print(" Nombre del álbum: " + str(self.nombre) +
              "\n Artista: " + str(self.artista) +
              "\n Fecha de Lanzamiento: " + str(self.fecha) +
              "\n Fue el " + str(self.orden_de_mini_album) + " mini álbum del grupo" +
              "\n Consta de " + str(self.numero_de_canciones) + " canciones que son las siguientes: ")
        
        for i in range(len(self.Lista_de_canciones)):
            print(self.Lista_de_canciones[i])

# Aquí hago una función para que me de la 'descripcion' de la clase que le especifico
def descripciones(Minialbum):
    Minialbum.descripcion()

album1 = I_AM("I AM", "(G)I-DLE", "2 de mayo del 2018", "6", "primer")  
album2 = I_BURN("I BURN", "(G)I-DLE", "11 de enero de 2021", "6", "cuarto")  

descripciones(album1)
print("--------------------------------------------------------------------------------")
descripciones(album2)

# En conclusión podemos observar que el método 'descripción' toma MUCHAS FORMAS,
# Es por eso que llamo mi funcion 'descripciones'