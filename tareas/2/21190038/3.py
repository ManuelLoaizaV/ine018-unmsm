#ejercicio_sesión_14

lista = input()
notas = lista.split(" ")
total = 0
cantidad = len(notas)

for nota in notas:
    suma = int(nota)
    total += suma

media = total/cantidad


print(float(media))