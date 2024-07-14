# Encapsulamiento:

## Cuenta 📧
En este ejemplo quise centrarme en el pilar del "Encapsulamiento" utilizando una clase llamada `Cuenta`, que tenía una contraseña y nombre de usuario ^^.

``` python
class Cuenta: 
```
Aquí para aplicar el "Encapsulamiento" restringí todos los atributos pertenecientes a mi clase: `usuario` y `contraseña`.

## Class `Cuenta`
Como ya mencioné antes, aquí mi clase `Cuenta` tiene encapsulados a dos atributos: `usuario` y `contraseña`, utilizando el doble guion bajo (`__`) para hacerlos privados.

- **Atributos:**
  - `__usuario`: Es el nombre de usuario de la cuenta.
  - `__contraseña`: Es la contraseña de la cuenta.

    ```python
    class Cuenta:
        def __init__(self, usuario, contraseña):
            self.__usuario = usuario        
            self.__contraseña = contraseña  
    ```

- **Métodos:**
  - `__init__(self, usuario, contraseña)`: Este es el constructor que inicializa el nombre de usuario y la contraseña de nuestra cuenta.

     ``` python
      def __init__ (self, usuario, contraseña): 
          self.__usuario = usuario
          self.__contraseña = contraseña
      ```
     _**Ahora sabemos que nuestros atributos están encapsulados por el uso del doble guion bajo (`__`), entonces debido a eso, debemos utilizar los métodos de 'getter' y 'setter' para acceder y modificar estos atributos de manera controlada.**_

  - `get_usuario(self)`: En este caso, el método 'getter' nos permite acceder a nuestro usuario. Luego de eso, lo imprimimos
       ``` python
      def get_usuario(self):
        print ("El usuario actual es '" + str(self.__usuario) + "'.")
     ```
  - `set_usuario(self, usuario_nuevo)`: En este caso, el método 'setter' nos permite acceder a nuestro nombre de usuario y modificarlo. Luego de eso, lo imprimimos.

    ``` python
     def set_usuario(self, usuario_nuevo):
        usuario_antiguo = self.__usuario
        self.__usuario = usuario_nuevo
        print("Se ha cambiado el usuario '" + str(usuario_antiguo) + "' a '" + str(self.__usuario) + "'.")
    ```
    _**~ De igual forma con nuestros métodos destinados a la contraseña:**_

  - `get_contraseña(self)`: En este caso, el método 'getter' nos permite acceder a nuestra contraseña. Luego de eso, la imprimimos.

     ``` python
     def get_contraseña(self):
        print("La contraseña actual es '" + str(self.__contraseña) + "'.")
      ```
  - `set_contraseña(self, contraseña_nueva)`: En este caso, el método 'setter' nos permite acceder a nuestra contraseña y modificarla. Luego de eso, la imprimimos.
    ``` python
     def set_contraseña(self, contraseña_nueva):
        contraseña_antigua = self.__contraseña
        self.__contraseña = contraseña_nueva
        print ("Se ha cambiado la contraseña '" + str(contraseña_antigua) + "' a '" + str(self.__contraseña) + "'.")
    ```
## Ejecución:

1. **Creación de nuestra cuenta:**

     ```python
    mi_cuenta = Cuenta("Fuuka2", "abcd")
    ```
    Aquí ya está creada nuestra cuenta. Nuestro nombre de usuario sería Fuuka2 y nuestra contraseña (ultra secreta) es abcd.

2. **Obtengo e imprimo el usuario actual y la contraseña actual:**

     ```python
    mi_cuenta.get_usuario()
    mi_cuenta.get_contraseña()
    ```
    Esto debería imprimir:
    - El usuario actual es 'Fuuka2'.
    - La contraseña actual es 'abcd'.

3. **Cambio el nombre de usuario y contraseña, e imprimo de sus mensajes:**

     ```python
    mi_cuenta.set_usuario("Fuuka_2")
    mi_cuenta.set_contraseña("xyz")
    ```
    Esto debería imprimir:
    - Se ha cambiado el usuario 'Fuuka2' a 'Fuuka_2'.
    - Se ha cambiado la contraseña 'abcd' a 'xyz'.

 3. **Obtengo e imprimo el usuario actual y la contraseña actual nuevamente, luego de ser cambiadas:**

     ```python
    mi_cuenta.get_usuario()
    mi_cuenta.get_contraseña()
    ```
    Esto debería imprimir:
    - El usuario actual es 'Fuuka_2'.
    - La contraseña actual es 'xyz'.

## Resultados del código ejecutado correctamente:
  ```
  El usuario actual es 'Fuuka2'.
  La contraseña actual es 'abcd'.
  Se ha cambiado el usuario 'Fuuka2' a 'Fuuka_2'.
  Se ha cambiado la contraseña 'abcd' a 'xyz'.
  El usuario actual es 'Fuuka_2'.
  La contraseña actual es 'xyz'.
  ```
# ⚠️ Notas Adicionales:
PD: Introduciré una línea de guiones para diferenciar lo que viene a continuación de lo anterior ^^
``` python
print("-------------------------------------------------------")
```
¡Bien! Haremos un pare aquí 🛑, y en este caso probaremos algo nuevo:

## ¿Qué pasa si...?

  ```python
  print("Usuario actual: '" + str(mi_cuenta._Cuenta__usuario) + "'.")
  print("Contraseña actual: '" + str(mi_cuenta._Cuenta__contraseña) + "'.")
  ```

  - El primero... _¿me arrojará el nombre actual?_
  - El segundo... _¿me arrojará la contraseña actual?_

**Resultados en 3... 2... 1...**

```
Usuario actual: 'Fuuka_2'.
Contraseña actual: 'xyz'.
```
**En ese momento yo quedé: ¿QUÉ? :v**

Probemos otro:

```python
mi_cuenta._Cuenta__usuario = "CR7"
mi_cuenta._Cuenta__contraseña = "Goat"
print("Usuario Nuevo: '" + str(mi_cuenta._Cuenta__usuario) + "'.")
print("Contraseña Nueva: '" + str(mi_cuenta._Cuenta__contraseña) + "'.")
  ```
  - Esto... _¿cambiará el nombre y la contraseña a lo que he escrito?_
 
 **Resultados en 3... 2... 1...**

```
Usuario Nuevo: 'CR7'.
Contraseña Nueva: 'Goat'.
```
**Ya allí estaba modo 🤡**

# Respuesta a ello:

Resulta que en Python, los atributos y métodos son públicos por defecto. Aunque hemos aplicado encapsulamiento, aún es posible acceder y modificar los atributos directamente utilizando el *"name mangling"* (Lo que usé en los casos anteriores: `_Cuenta__usuario` y `_Cuenta__contraseña`). Esto lo pudimos demostrar aquí.

**Finalmente, dentro de mi ejemplo, también coloqué dicha sección de código:**

```python
mi_cuenta._Cuenta__usuario = "CR7"
mi_cuenta._Cuenta__contraseña = "Goat"
print("Usuario Nuevo: " + str(mi_cuenta._Cuenta__usuario))
print("Contraseña Nueva: " + str(mi_cuenta._Cuenta__contraseña))
 ```

## Ahora sí, resultados de TODO el código ejecutado correctamente:

```
El usuario actual es 'Fuuka2'.
La contraseña actual es 'abcd'.
Se ha cambiado el usuario 'Fuuka2' a 'Fuuka_2'.
Se ha cambiado la contraseña 'abcd' a 'xyz'.
El usuario actual es 'Fuuka_2'.
La contraseña actual es 'xyz'.
-------------------------------------------------------
Usuario actual: 'Fuuka_2'.
Contraseña actual: 'xyz'.
Usuario Nuevo: 'CR7'.
Contraseña Nueva: 'Goat'.
  ```