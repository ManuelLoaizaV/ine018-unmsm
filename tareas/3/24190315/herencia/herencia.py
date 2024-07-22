#HERENCIA
class Figura:
	area = 0.0
	perimetro = 0.0

	def __init__(self,nombre):
		self.nombre = nombre

	def Area(self):
		return self.area

	def Perimetro(self):
		return self.perimetro

class Triangulo(Figura):
	def calcularArea(self,base,altura):
		self.area = (base*altura)/2

class Cuadrado(Figura):
	def calcularArea(self,lado):
		self.area = lado*lado
	def calcularPerimetro(self,lado):
		self.perimetro = 4*lado

figura1 = Triangulo("Triangulo 1")
figura1.calcularArea(10,6)

figura2 = Triangulo("Triangulo 2")
figura2.calcularArea(12,18)

figura3 = Cuadrado("Cuadrado 1")
figura3.calcularArea(10)
figura3.calcularPerimetro(10)

figura4 = Cuadrado("Cuadrado 2")
figura4.calcularArea(16.5)
figura4.calcularPerimetro(16.5)

print("El area de la figura %s es %s" %(figura1.nombre,figura1.Area()))
print("El area de la figura %s es %s" %(figura2.nombre,figura2.Area()))
print("El area de la figura %s es %s y su perimetro es %s" %(figura3.nombre,figura3.Area(),figura3.Perimetro()))
print("El area de la figura %s es %s y su perimetro es %s" %(figura4.nombre,figura4.Area(),figura4.Perimetro()))