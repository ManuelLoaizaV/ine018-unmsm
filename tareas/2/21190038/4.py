cadena = input()
prueba = []
buena = []

for letra in cadena:
    prueba.append(letra)

tamaño = len(prueba)
l = 0

while(l < tamaño):
    if(buena and buena[-1].islower() and buena[-1].upper() == prueba[l]):
        buena.pop()
    else:
        buena.append(prueba[l])
    l += 1


print(''.join(buena))

