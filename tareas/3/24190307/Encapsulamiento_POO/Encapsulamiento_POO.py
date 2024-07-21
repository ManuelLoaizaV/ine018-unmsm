# ENCAPSULAMIENTO

class Cuenta:
    def __init__ (self, usuario, contraseña):
        self.__usuario = usuario
        self.__contraseña = contraseña
    # Aplico encapsulamiento para que no pueda
    # cambiar la contraseña ni el usuario 

    # Aquí usamos tanto 'get' como 'set' para acceder
    # A los atributos ^^

    def get_usuario(self):
        print ("El usuario actual es '" + str(self.__usuario) + "'.")
    # 'Get' para acceder al atributo y obtenerlo    

    def set_usuario(self, usuario_nuevo):
        usuario_antiguo = self.__usuario
        self.__usuario = usuario_nuevo
        print("Se ha cambiado el usuario '" + str(usuario_antiguo) + "' a '" + str(self.__usuario) + "'.")
        # 'Set' para acceder al atributo y modificarlo  

    def get_contraseña(self):
        print("La contraseña actual es '" + str(self.__contraseña) + "'.")
        # De igual forma... aquí para obtenerlo

    def set_contraseña(self, contraseña_nueva):
        contraseña_antigua = self.__contraseña
        self.__contraseña = contraseña_nueva
        print ("Se ha cambiado la contraseña '" + str(contraseña_antigua) + "' a '" + str(self.__contraseña) + "'.")
        # Y aquí para modificarlo
      
mi_cuenta = Cuenta("Fuuka2", "abcd")
mi_cuenta.get_usuario()
mi_cuenta.get_contraseña()
mi_cuenta.set_usuario("Fuuka_2")
mi_cuenta.set_contraseña("xyz")
mi_cuenta.get_usuario()
mi_cuenta.get_contraseña()

print("-------------------------------------------------------")

# Aquí vamos a volvernos salvajes uu
print("Usuario actual: '" + str(mi_cuenta._Cuenta__usuario) + "'.")
print("Contraseña actual: '" + str(mi_cuenta._Cuenta__contraseña) + "'.")
mi_cuenta._Cuenta__usuario = "CR7"
mi_cuenta._Cuenta__contraseña = "Goat"
print("Usuario Nuevo: '" + str(mi_cuenta._Cuenta__usuario) + "'.")
print("Contraseña Nueva: '" + str(mi_cuenta._Cuenta__contraseña) + "'.")
# Sorpresa! No es necesario usar ni el 'set' ni el 'get'
# Esto se debe a que en Python los atributos y los métodos
# Son púlbicos por defecto :, (:v xd)
# Pero para hacerlo debemos utlizar ._Cuenta__atributo, 
# También llamado 'Name mangling'