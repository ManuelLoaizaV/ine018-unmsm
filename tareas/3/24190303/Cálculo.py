from sympy import symbols, diff, sqrt, cos, pi, lambdify
import matplotlib.pyplot as plt
import numpy as np

x = symbols('x')
F = (x - 5)*(2/3) + 0.1 * sqrt(20 - (x - 5)**2) * cos(10 * pi * (x - 5))
D = diff(F, x)
print("Derivada de la función F(x):")
print(D)

# No entendí muy bien pero son los rangos y precisión
Fnum= lambdify(x, F, 'numpy')
x = np.linspace(-5, 5, 100000)
y = Fnum(x)
plt.figure(figsize=(20, 20)) 

# Grafiqué la función pero no su derivada
plt.plot(x, y, label='Corazón')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfica de la función Corazón')

plt.show()
