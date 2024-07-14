# Polimorfismo:

## Mini album (G)I-DLE 🎵

En este ejemplo, utilizaré a mi grupo favorito (G)I-DLE  y crearé dos clases distintas (`I_AM` y `I_BURN`) cada una representando un álbum de música:

- `I_AM`:
``` python
class I_AM:
```

- `I_BURN`:
``` python
class I_BURN:
```

Cada una tendrá atributos como: `nombre`, `artista`, `fecha`, `numero_de_canciones` y `orden_de_mini_album`, pero en un caso especial, cada una tendrá su propio método `descripcion` y allí aplicaré el pilar del "Polimorfismo", porque `descripcion` tomará _MUCHAS FORMAS_ ^^.

_Cabe resaltar que también pude usar "Herencia" para no escribir tanto (en el caso del constructor), pero no quería emplear dos pilares de POO en un solo ejemplo destinado al Polimorfismo._

## Clase `I_AM`

- **Atributos:**
    - `nombre`: El nombre del álbum.
    - `artista`: El nombre del artista o grupo (en este caso).
    - `fecha`: La fecha de lanzamiento del álbum.
    - `numero_de_canciones`: El número de canciones en el álbum.
    - `orden_de_mini_album`: El orden del mini álbum en la discografía del grupo.

        ``` python 
        def __init__(self, nombre, artista, fecha, numero_de_canciones, orden_de_mini_album):
            self.nombre = nombre
            self.artista = artista
            self.fecha = fecha
            self.numero_de_canciones = numero_de_canciones
            self.orden_de_mini_album = orden_de_mini_album
        ```

- **Métodos:**
    - `__init__(self, nombre, artista, fecha, numero_de_canciones, orden_de_mini_album)`: Este es el constructor que inicializa el nombre del album, el artista, la fecha de lanzamiento, el número de canciones y el orden del mini álbum.

        ``` python
        def __init__(self, nombre, artista, fecha, numero_de_canciones, orden_de_mini_album):
        ```
    - `descripcion(self)`: Imprime la descripción del álbum, incluyendo la lista de canciones.
        ``` python
        def descripcion (self):
            self.Lista_de_canciones = ["  1. LATATA", "  2. $$$ (Dollar)", "  3. Maze", "  4. Don't text me", 
                                       "  5. What's you name?", "  6. Hear me"]
        
            print(" Nombre del álbum: " + str(self.nombre) +
                 "\n Artista: " + str(self.artista) +
                 "\n Fecha de Lanzamiento: " + str(self.fecha) +
                 "\n Fue el " + str(self.orden_de_mini_album) + " mini álbum del grupo" +
                 "\n Consta de " + str(self.numero_de_canciones) + " canciones que son las siguientes: ")
        
            for i in range(len(self.Lista_de_canciones)):
                print(self.Lista_de_canciones[i])
        ```

## Clase `I_BURN`

- **Atributos:**
    - `nombre`: El nombre del álbum.
    - `artista`: El nombre del artista o grupo (en este caso).
    - `fecha`: La fecha de lanzamiento del álbum.
    - `numero_de_canciones`: El número de canciones en el álbum.
    - `orden_de_mini_album`: El orden del mini álbum en la discografía del grupo.

        ``` python 
        def __init__(self, nombre, artista, fecha, numero_de_canciones, orden_de_mini_album):
            self.nombre = nombre
            self.artista = artista
            self.fecha = fecha
            self.numero_de_canciones = numero_de_canciones
            self.orden_de_mini_album = orden_de_mini_album
        ```

- **Métodos:**
    - `__init__(self, nombre, artista, fecha, numero_de_canciones, orden_de_mini_album)`: Este es el constructor que inicializa el nombre del album, el artista, la fecha de lanzamiento, el número de canciones y el orden del mini álbum.

        ``` python
        def __init__(self, nombre, artista, fecha, numero_de_canciones, orden_de_mini_album):
        ```
    - `descripcion(self)`: Imprime la descripción del álbum, incluyendo la lista de canciones.
        ``` python
        def descripcion (self):
            self.Lista_de_canciones = ["  1. HANN (Alone in the Winter)", "  2. HWAA (火花)", "  3. MOON", 
                                       "  4. Where is love?", "  5. Lost", "  6. DAHLIA"]  
        
            print(" Nombre del álbum: " + str(self.nombre) +
                 "\n Artista: " + str(self.artista) +
                 "\n Fecha de Lanzamiento: " + str(self.fecha) +
                 "\n Fue el " + str(self.orden_de_mini_album) + " mini álbum del grupo" +
                 "\n Consta de " + str(self.numero_de_canciones) + " canciones que son las siguientes: ")
        
            for i in range(len(self.Lista_de_canciones)):
                print(self.Lista_de_canciones[i])

## Función para imprimir el método `descripcion`:

 - `descripciones(Minialbum)`: Es esta función que demuestra el polimorfismo al aceptar objetos de diferentes clases y llamar a su método `descripcion`.

     ``` python
        def descripciones(Minialbum):
        Minialbum.descripcion()
    ```

## Ejecución:

1. **Creación de los mini álbumes:**
    ```python
    album1 = I_AM("I AM", "(G)I-DLE", "2 de mayo del 2018", "6", "primer")  
    album2 = I_BURN("I BURN", "(G)I-DLE", "11 de enero de 2021", "6", "cuarto")
    ```

2. **Imprimo sus descripciones:**
    - De I AM:
        ```python
        descripciones(album1)
        ```
        ****
    - De I BURN:
        ```python
        descripciones(album2)
        ```
   
        **** Cada album separado por una línea de guiones:

        ``` python
            print("-------------------------------------------------------------------------------------")
        ```
## Resultados del código ejecutado correctamente:
```
 Nombre del álbum: I AM
 Artista: (G)I-DLE
 Fecha de Lanzamiento: 2 de mayo del 2018
 Fue el primer mini álbum del grupo
 Consta de 6 canciones que son las siguientes: 
 1. LATATA
 2. $$$ (Dollar)
 3. Maze
 4. Don't text me
 5. What's you name?
 6. Hear me
--------------------------------------------------------------------------------
 Nombre del álbum: I BURN
 Artista: (G)I-DLE
 Fecha de Lanzamiento: 11 de enero de 2021
 Fue el cuarto mini álbum del grupo
 Consta de 6 canciones que son las siguientes: 
 1. HANN (Alone in the Winter)
 2. HWAA (火花)
 3. MOON
 4. Where is love?
 5. Lost
 6. DAHLIA
```