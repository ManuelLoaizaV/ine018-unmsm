import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Definimos el símbolo 'x'
x = sp.symbols('x')

# Definimos la función f(x)
def f(x):
    return sp.log(sp.cos(x)**2 + sp.sqrt(1 + sp.cos(x)**4)) + (3 * sp.sqrt(x**6) / (2 * x**3))

# Mostramos la definición de f(x)
print("f(x) está definida como:", f(x))

# Calculamos la derivada usando la función 'diff' de SymPy
derivada1 = sp.diff(f(x), x)

# Mostramos la derivada de f(x)
print("La derivada de f(x) es: ", derivada1)

# Convertimos la derivada en una función
f_prime = sp.lambdify(x, derivada1, 'numpy')

# Creamos un rango de valores de x para graficar
x_vals = np.linspace(0.1, 2, 400)
y_vals = f_prime(x_vals)

# Graficamos la función derivada
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='f\'(x)')
plt.title('Gráfica de la derivada de f(x)')
plt.xlabel('x')
plt.ylabel('f\'(x)')
plt.grid(True)
plt.legend()
plt.show()
