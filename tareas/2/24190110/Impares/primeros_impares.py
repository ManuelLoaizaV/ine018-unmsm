with open('entrada.txt','r') as archivo:
    n = int(archivo.read())
suma=n*n
with open('salida.txt','w') as archivo2:
    archivo2.write(f'La suma de 1 + ... + "{2 * n-1 }"es: "{suma}\n')
