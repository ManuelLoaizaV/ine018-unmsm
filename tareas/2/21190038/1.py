#ejercicio_sesión_6

cantidad = int(input())

docenas = cantidad/12

if(cantidad%12 != 0):
    docenas += 1


print(int(docenas))
