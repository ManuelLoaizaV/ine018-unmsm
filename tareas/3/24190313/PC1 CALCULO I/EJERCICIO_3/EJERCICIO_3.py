import sympy as sp

print ("Ejercicio 3:")
print ("La gran rueda de la fortuna de un gran casino, tiene un diámetro de 120 metros y una altura máxima de 135 metros.")
print ("La rueda tarda aproximadamente media hora en completar una vuelta completa.")
print ("La altura H sobre el suelo a la cual se encuentra una capsula está dada por:")
print ("H(t) = 75 + 60sen(πt/15 - π/2) ; t ≥ 0")
print ("Donde el tiempo t está en minutos.")
print ("Calcula el periodo, amplitud y desplazamiento de fase")

t = sp.symbols('t')

h = 75 + 60*sp.sin((sp.pi*t/15)+(sp.pi/2))

coef_t = sp.pi / 15
periodo = 2 * sp.pi / coef_t

amplitud = sp.Abs(60)

constante_seno = -sp.pi / 2
desplazamiento_fase = -constante_seno / coef_t

print(f"Período: {periodo}")
print(f"Amplitud: {amplitud}")
print(f"Desplazamiento de fase: {desplazamiento_fase}")