# Clase:

## Robot 🤖 
En este ejemplo creé una clase `Robot`, que básicamente es un robot que tiene diferentes modos y ejecuta distintas tareas de acuerdo a ello. 

``` python
class Robot  
```

Aquí  mi clase `Robot` tiene los atributos `nombre` y  `modelo`, y también posee los métodos de `cambiar_modo` y `tarea`.

## Class `Robot`

- **Atributos:**
  - `nombre`: Es el nombre del robot.
  - `modelo`: Es el modelo del robot.
  - `modo`: Es el modo actual del robot (por defecto, lo dejé en  "descanso").
  ``` python
  class Robot:
    def __init__(self, nombre, modelo):
        self.nombre = nombre    
        self.modelo = modelo    
        self.modo = "descanso"   
  ```

- **Métodos:**

  - `__init__(self, nombre, modelo)`: Este es el constructor que inicializa el nombre, modelo y modo del robot.

  ``` python
    def __init__(self, nombre, modelo):
  ```

  - `cambiar_modo(self, nuevo_modo)`: Cambia el modo del robot si el nuevo modo es válido (o sea si es descanso, trabajo, reparación o exploración).
  
    Pero en caso no lo sea, se imprime: "Modo no válido.".
  ``` python
  def cambiar_modo(self, nuevo_modo):
        modos_actuales = ["descanso", "trabajo", "reparacion", "exploracion"]
        if nuevo_modo in modos_actuales:
            self.modo = nuevo_modo
            print(str(self.nombre) + " ha cambiado al modo " + str(self.modo) + ".")
        else:
            print("Modo no válido.")
  ```
  - `tarea(self)`: Imprime la tarea que el robot está realizando, todo ello dependiendo de su modo actual. (Trabaja dependiendo del modo de `cambiar_modo(self, nuevo_modo)`).
  ``` python
  def tarea(self):   
        if self.modo == "trabajo":
            print(str(self.nombre) + " está realizando tareas de trabajo.")
        elif self.modo == "reparacion":
            print(str(self.nombre) + " está realizando tareas de reparación.")
        elif self.modo == "exploracion":
            print(str(self.nombre) + " está explorando nuevas áreas.")
        else:
            print(str(self.nombre) + " está modo " + str(self.modo) + ", no realiza tareas.")
  ```

  - `Modelo(self)`: Imprime el modelo del robot ^^. En este caso le puse una mayúscula para que no se confunda con el atributo previamente mencionado.

  ``` python
  def Modelo(self):
        print("El modelo de " + str(self.nombre) + " es " + str(self.modelo) + ".")
  ```

## Ejecución:

1. **Creación de mi robot:**

   ```python
   mi_robot = Robot("Fuuka2", "IDLE")
   ```
    Aquí ya está creado nuestro robot. Se llama Fuuka2 y su modelo es IDLE ^^.

2. **Imprimo el nombre de mi robot:**

   ```python
   print(str(mi_robot.nombre) + ":")
   ```
   Aquí nos debería imprimir:
   - Fuuka2:

3. **Imprimo el modelo de mi robot:**
   ```python
   mi_robot.Modelo()
    ``` 
   Nos debería imprimir:
   - El modelo de Fuuka2 es IDLE.

4. **Cambio el modo de mi robot e imprimo la tarea que realiza:**
   ```python
    mi_robot.cambiar_modo("trabajo")
    mi_robot.tarea()
    ``` 
    En este caso imprimo:
    - Fuuka2 ha cambiado al modo trabajo.
    - Fuuka2 está realizando tareas de trabajo.
    
    Esto es porque ahora porque está en modo 'trabajo'.

5. **Cambio nuevamente el modo de mi robot e imprimo la tarea que realiza:**
   ```python
    mi_robot.cambiar_modo("descanso")
    mi_robot.tarea()
    ``` 
    En este caso imprimo:
    - Fuuka2 ha cambiado al modo descanso.
    - Fuuka2 está modo descanso, no realiza tareas.
    
    Esto es debido a que ahora está en modo 'descanso'.

## Resultados del código ejecutado correctamente:
  ```python
  Fuuka2:
  El modelo de Fuuka2 es IDLE.
  Fuuka2 ha cambiado al modo trabajo
  Fuuka2 está realizando tareas de trabajo.
  Fuuka2 ha cambiado al modo descanso
  Fuuka2 está modo descanso, no realiza tareas.
  ```