#POLIMORFISMO
class Perro():
    def hacer_sonido(self):
        print("Guau")

class Gato():
    def hacer_sonido(self):
        print("Miau")

class Cocodrilo():
    def hacer_sonido(self):
        print("Grrr")

def hacer_sonido_del_animal(animal):
    animal.hacer_sonido()

perro = Perro()
gato = Gato()
cocodrilo = Cocodrilo()

hacer_sonido_del_animal(perro)
hacer_sonido_del_animal(gato)
hacer_sonido_del_animal(cocodrilo)