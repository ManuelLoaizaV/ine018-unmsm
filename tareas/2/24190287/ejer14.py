n = int(input())
numeros = []
    
for i in range(n):
    num= float(input())
    numeros.append(num)
    
if len(numeros) == 0:
    media = 0.0  
else: 
    suma = sum(numeros)
    media = suma/len(numeros)

print(media)