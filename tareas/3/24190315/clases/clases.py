#CLASES
class EcuacionCuadratica:
	def __init__(self,coea,coeb,coec):
		self.a = coea
		self.b = coeb
		self.c = coec
		self.raices = []

	def Raices(self):
		return self.raices

	def calcular(self):
		d = self.b**2-4*self.a*self.c
		if d == 0:
			x1 = -1*self.b/(2*self.a)
			self.raices.append(x1)
		elif d>0:
			x1 = (-1*self.b+d**0.5)/(2*self.a)
			x2 = (-1*self.b-d**0.5)/(2*self.a)
			self.raices.append(x1)
			self.raices.append(x2)
		else:
			self.raices = []

ecuacion1 = EcuacionCuadratica(1,10,21)
ecuacion1.calcular()
ecuacion2 = EcuacionCuadratica(1,-5,-24)
ecuacion2.calcular()
ecuacion3 = EcuacionCuadratica(1,0,-25)
ecuacion3.calcular()

print("Las raices de la ecuacion 1 son: %s" %ecuacion1.Raices())
print("Las raices de la ecuacion 2 son: %s" %ecuacion2.Raices())
print("Las raices de la ecuacion 3 son: %s" %ecuacion3.Raices())