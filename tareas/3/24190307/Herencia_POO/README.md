# Herencia:

## Team RWBY ❤️🤍🖤💛

En este ejemplo, usaré una de mis series favoritas, RWBY, y crearé una  clase llamada `Beacon` (la academia Beacon, el lugar donde empezó todo -.-).

``` python
class Beacon  
```

Luego de eso, utilizaré la herencia para crear subclases de mi clase `Beacon`, para representar a cada una de las miembros del team RWBY.

## Class `Beacon`

Esta es la clase principal que define los atributos básicos, los que pronto también serán parte de las clases de las integrantes del Team RWBY.


- **Atributos:**
  - `nombre`: El nombre de la integrante.
  - `edad`: Su edad  al comienzo de la serie.
  - `hogar`: El lugar donde nacieron y crecieron.
  - `especie`: La especie a la que pertencen.
  - `semblanza`: La semblanza que las caracteriza (Semejante a sus poderes).
  - `arma`: El nombre de su arma.

    ```python
    class Beacon:
        def __init__(self, nombre, edad, hogar, especie, semblanza, arma):
            self.nombre = nombre
            self.edad = edad
            self.hogar = hogar
            self.especie = especie
            self.semblanza = semblanza
            self.arma = arma
    ```
- **Métodos:**
    - `__init__(self, nombre, edad, hogar, especie, semblanza, arma)`: Este es el constructor que inicializa el nombre de la integrante, su edad, su hogar, su especie, su semblanza y su arma.

        ```python
            def __init__(self, nombre, edad, hogar, especie, semblanza, arma):
        ```

## Subclases:
Aquí empezaremos a definir las subclases, o sea a las integrantes del team RWBY por separado, utilzando los mismos atributos de la clase `Beacon` y agregándoles un atributo (una curiosidad suya) y un método para imprimir estos.

- ## Class `Ruby`:
    ```python
    class Ruby(Beacon):
        def __init__(self, nombre, edad, hogar, especie, semblanza, arma, apodo):
            super().__init__(nombre, edad, hogar, especie, semblanza, arma)
            self.apodo = apodo

        def Apodo(self):
            print(str(self.apodo))
    ```
    - Aquí añadiremos un atributo más, por lo que utilizamos la función `super.()` que nos permite llamar a los atributos y los métodos de la superclase `Beacon`. Luego en el propio contructor `__init__` de la clase `Ruby` añadimos el atributo `apodo` y finalmente, con el método `Apodo`, imprimimos el nuevo atributo.

- ## Class `Weiss`:
    ```python
    class Weiss(Beacon):
        def __init__(self, nombre, edad, hogar, especie, semblanza, arma, familia):
            super().__init__(nombre, edad, hogar, especie, semblanza, arma)
            self.familia = familia

        def Familia(self):
            print(str(self.familia))
    ```
    - Aquí igual, utilizamos la función `super.()` y en el propio contructor `__init__` de `Weiss` añadimos el atributo `familia` para luego, con el método `Familia`, imprimir el nuevo atributo.

- ## Class `Blake`:
    ```python
    class Blake(Beacon):
        def __init__(self, nombre, edad, hogar, especie, semblanza, arma, secreto):
            super().__init__(nombre, edad, hogar, especie, semblanza, arma)
            self.secreto = secreto

        def Secreto(self):
            print(str(self.secreto))
    ```
    - De igual forma, utilizamos la función `super.()`, luego en el propio contructor `__init__` de `Blake` añadimos el atributo `secreto` y finalmente, con el método `Secreto`, imprimimos el nuevo atributo.

- ## Class `Yang`:
    ```python
    class Yang(Beacon):
        def __init__(self, nombre, edad, hogar, especie, semblanza, arma, brazo):
            super().__init__(nombre, edad, hogar, especie, semblanza, arma)
            self.brazo = brazo

        def Brazo(self):
            print(self.brazo)
    ```
    - Lo mismo ^^. Utilizamos la función `super.()`, luego en el propio contructor `__init__` de `Yang` añadimos el atributo `brazo`, y luego imprimimos el nuevo atributo con el método `Brazo`.

- _"**Algo que quería rescatar aquí**_ _es que en el caso del `super()` ya no es necesario colocar el `self` puesto que ya viene incorporado en la función."_

## Creación de una función para imprimir sus datos:

``` python
def imprimir_datos(personaje):
    print(" ⌂ " + str(personaje.__class__.__name__) +
          "\n Nombre completo: " + str(personaje.nombre) +
          "\n Edad: " + str(personaje.edad) +
          "\n Lugar de origen: " + str(personaje.hogar) +
          "\n Especie: " + str(personaje.especie) +
          "\n Semblanza: " + str(personaje.semblanza) +
          "\n Arma: " + str(personaje.arma) +
          "\n ⌂ Curiosidad:")
```
- Aquí debo resaltar el uso del `__class__.__name__`. Esto me ayudó a imprimir las clases de las diferentes integrantes (objetos).
## Ejecución:

1. **Creación de nuestras integrantes del Team RWBY:**
    ```python
    ruby = Ruby("Ruby Rose", "15", "Patch (Vale)", "Humana", "Petal Burst", "Crescent Rose", 
                "  - Uno de sus rasgos más resaltantes es que tiene los ojos plateados como su madre.")

    weiss = Weiss("Weiss Schnee", "17", "Atlas", "Humana", "Glyphs", "Myrtenaster", 
                "  - Proviene de una familia dueña de la famosa Schnee Dust Company, distribuidora de Dust.")

    blake = Blake("Blake Belladonna", "17", "Isla de Menagerie", "Faunus", "Shadow", "Gambol Shroud", 
                "  - Cuando era más joven pertenecía a una organización llamada White Fang, pero luego huyó.")

    yang = Yang("Yang Xiao Long", "17", "Patch (Vale)", "Humana", "Burn", "Ember Celica", 
                "  - Perdió su brazo derecho por proteger a Blake, ahora tiene uno de metal hecho en Atlas.")
    ```
    - Cada una con sus respectivos datos y curiosidades :D.

2. **Imprimo los datos de cada una con su respectiva curiosidad**:
- Para Ruby:
    ```python
    imprimir_datos(ruby)
    ruby.Apodo()
    ```
    ****
- Para Weiss:
    ```python
    imprimir_datos(weiss)
    weiss.Familia()
    ```
    ****
- Para Blake:
    ```python
    imprimir_datos(blake)
    blake.Secreto()
    ```
    ****
- Para Yang:
    ```python
    imprimir_datos(yang)
    yang.Brazo()
    ```

    **** Cada una separada con una línea de guiones:

    ``` python
   print("-------------------------------------------------------------------------------------")
    ```

## Resultados del código ejecutado correctamente:
  ```
 ⌂ Ruby
 Nombre completo: Ruby Rose
 Edad: 15
 Lugar de origen: Patch (Vale)
 Especie: Humana
 Semblanza: Petal Burst
 Arma: Crescent Rose
 ⌂ Curiosidad:
  - Uno de sus rasgos más resaltantes es que tiene los ojos plateados como su madre.
-------------------------------------------------------------------------------------
 ⌂ Weiss
 Nombre completo: Weiss Schnee
 Edad: 17
 Lugar de origen: Atlas
 Especie: Humana
 Semblanza: Glyphs
 Arma: Myrtenaster
 ⌂ Curiosidad:
  - Proviene de una familia dueña de la famosa Schnee Dust Company, distribuidora de Dust.
-------------------------------------------------------------------------------------
 ⌂ Blake
 Nombre completo: Blake Belladonna
 Edad: 17
 Lugar de origen: Isla de Menagerie
 Especie: Faunus
 Semblanza: Shadow
 Arma: Gambol Shroud
 ⌂ Curiosidad:
  - Cuando era más joven pertenecía a una organización llamada White Fang, pero luego huyó.
-------------------------------------------------------------------------------------
 ⌂ Yang
 Nombre completo: Yang Xiao Long
 Edad: 17
 Lugar de origen: Patch (Vale)
 Especie: Humana
 Semblanza: Burn
 Arma: Ember Celica
 ⌂ Curiosidad:
  - Perdió su brazo derecho por proteger a Blake, ahora tiene uno de metal hecho en Atlas.
  ```
