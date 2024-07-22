import sympy as sp
print ("PREGUNTA 3 PC1")
print ("La gran rueda de la fortuna de un gran casino, tiene un diámetro de 120 metros y una altura máxima de 135 metros.")
print ("La rueda tarda aproximadamente media hora en completar una vuelta completa.")
print ("La altura H sobre el suelo a la cual se encuentra una capsula está dada por:")
print ("H(t) = 75 + 60sen(πt/15 - π/2) ; t ≥ 0")
print ("Donde el tiempo t está en minutos.")
print ("Calcula el periodo, amplitud, y su desplazamiento de fase")
t= sp.symbols('t')

H = 75 + 60*sp.sin((sp.pi*t/15)+(sp.pi/2))
sp.pprint(H)
a = sp.pi/15
T = 2* sp.pi/a
A = sp.Abs(60)
valor = -sp.pi / 2
MOvimiento= -valor/a
print("Con los datos sacados del dato dado se calular el: " )
print(f"El Período: {T}")
print(f"La Amplitud: {A}")
print(f"El Desplazamiento: {MOvimiento}")