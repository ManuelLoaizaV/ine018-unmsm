# Programación orientada a objetos:

A continuación se presentarán dos casos y en cada uno tomaremos el rol de secretaria/o.
Sabemos que `Reniec` es organizar y mantener el registro único de identificación de las personas naturales e inscribir los hechos y actos relativos a su capacidad y estado civil. 

Para entender los primeros conceptos: `Clase y Encapsulamiento`, imaginaremos que somos una secretaria/o que esta encargada/o de agregar los datos de los nuevos empleados en una empresa, para esto necesitamos datos personales que todos tenemos.

## Class:

``` python
class Persona  
```
Nuestra clase tendrá 3 atributos: `Nombre`, `Edad`, `N°DNI`.

En Python sería así:

``` python
def __init__(self, name, age, uid):
        self.nombre = name
        self.edad = age
        self.dni = uid  
```
Ahora que tenemos puesto y declarados nuestros atributos, procedemos con la extracción de datos.

Elegí este proyecto debido a que se me hizo muy interesante el hecho de que se puede recopilar datos, líneas e incluso informaciones específicas de cualquier página web. Me pareció bastante curioso lo automatizado que se vuelve el proceso de extracción de datos con una estructura en su código HTML y quise intentar este proceso por mi misma.

``` python
 #Extracción de datos
    def __str__(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}, DNI: {self.__dni}"
``` 
Ahora tendríamos que poner los datos de esta manera:

``` python
persona1 = Persona()
persona1.nombre = "Juan"
persona1.edad = 25
persona1.DNI = "12345678"
```

## Encapsulamiento:
Para esto tendremos que agregar

``` python
def __init__(self, name="", age=0, uid="")
```
En la parte superior de nuestro codigo para los atributos, teniendo como resultado final:

``` python
    def __init__(self, name="", age=0, uid=""):
        self.__nombre = name
        self.__edad = age
        self.__dni = uid
``` 
Para esto agregamos los guiones bajos, ahora tenemos que usar set y get, para colocar y obtener los datos.

``` python
    def set_Nombre(self, name):
        self.__nombre = name

    def get_Nombre(self):
        return self.__nombre
    
    def set_Edad(self, age):
        self.__edad = age
    
    def get_Edad(self):
        return self.__edad
    
    def set_DNI(self, uid):
        self.__dni = uid
    
    def get_DNI(self):
        return self.__dni
``` 
Luego instanciamos la clase:

``` python
persona1 = Persona("Juan", 20, "12345678")

persona2 = Persona("Ana", 25, "87654321")

persona3 = Persona("Pedro", 30, "87654321")
```
Esto nos debería dar:

`Nombre: Juan, Edad: 20, DNI: 12345678`
`Nombre: Ana, Edad: 25, DNI: 87654321`
`Nombre: Pedro, Edad: 30, DNI: 87654321`

Ahora para el siguiente código entenderemos los conceptos de `Herencia` y `Poliformismo`.
Mi querida secretaria/o comenzaremos a poner a nuestros empleados en sus respectivos puestos.

Para esto tendremos en cuenta los tipos de atributos que hay: privados, públicos y protegidos.

## Herencia
Establecemos la clase trabajador: `Class: Trabajador` este sería nuestro Padre >< 

``` python
class Trabajador:
    def __init__(self, nombre="", sueldo=1200.00, tipo=""):
        self._nombre = nombre
        self._sueldo = sueldo
        self._tipo = tipo
    
    def __str__(self):
        return f"Nombre: {self._nombre}, Sueldo: {self._sueldo}, Tipo: {self._tipo}"
``` 
Lo siguiente es nuestro primer hijo :D (Administrativo)

``` python
class Administrativo(Trabajador):
    #Atrbiuto de clase y de instancia

    def __init__(self, nombre="", sueldo=1200.00, tipo="", MBA=False, area=""):
        super().__init__(nombre, sueldo, tipo)
        self.__area = area
        self.__MBA = MBA

    def __str__(self):
        return f"{super().__str__()}, Area: {self.__area}, MBA: {self.__MBA}"
    
    def func1(self):
        print(f"Soy {self._nombre} y soy {self._tipo} en el area de {self.__area}")
``` 
Ya vieron el super? jiji, esta es una función predeterminada que nos da python para llamar al Padre del sistema.

Y aqui entra el poliformismo :D

## Poliformismo

Nuestra `func1` cumplirá otro trabajo como función que estaría en el siguiente hijo que se llamaría `Técnico`.

``` python
class Tecnico(Trabajador):
    def __init__(self, nombre="", sueldo=1200.00, tipo="", certificado="AWS", cod_machine=""):
        super().__init__(nombre, sueldo, tipo)
        self._certificado = certificado
        self.__cod_machine = cod_machine

    def __str__(self):
        return f"{super().__str__()}, Especialidad: {self.__especialidad}"
    
    def func1(self):
        print(f"Soy {self._nombre}, soy {self._tipo} y tengo el certificado {self._certificado}, y mi codigo de maquina es {self.__cod_machine}")
```
Es así como demostramos poliformismo :b en una función

Le damos los datos a poner:

``` python
Trabajador1 = Trabajador("Juan", 1500.00, "Administrativo")
Administrativo1 = Administrativo("Pedro", 2000.00, "Administrativo", True, "Recursos Humanos")
Tecnico1 = Tecnico("Ana", 1800.00, "Tecnico", "Azure", "1234")
```
Y esto nos debería dar:
Soy Pedro y soy Administrativo en el area de Recursos Humanos
Soy Ana, soy Tecnico y tengo el certificado Azure, y mi codigo de maquina es 1234