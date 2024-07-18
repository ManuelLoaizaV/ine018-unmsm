a = input ("Ingrese la cadena: ")
numero = len(a)
entero_a = 0

if a[0] == '-':
    inicio_a = 1
else:
    inicio_a = 0
    
for i in range(inicio_a, numero):
    entero_a = 10 * entero_a + (ord(a[i]) - ord('0'))
if a[0] == '-':
    entero_a = entero_a * -1
    
print(entero_a)