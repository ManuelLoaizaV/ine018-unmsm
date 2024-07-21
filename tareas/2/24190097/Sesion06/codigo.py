masa = float(input("Ingrese la cantidad de kilogramos de masa: "))

print("E = m * c^2")
print(f"m = {masa} kg")

c = 2.99792459E8  # velocidad de la luz en m/s
print(f"c = {c} m/s")

E = masa * c * c

print(f"{E} J de energía")