with open ('1_entrada.txt', 'r') as entrada:
  n = int(entrada.readline()) 

suma = n*n
termino_n = 2*n - 1 

with open('1_salida.txt', 'w') as salida:
  salida.write("La suma de 1 + ... + " + str(termino_n) + " es " + str(suma))
