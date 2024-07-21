from math import sqrt
num=int(input("Digite un numero: "))
if ((int(sqrt(num)) * (sqrt(num)))== num):
    print (f'El numero {num} es cuardado perfecto.')
else:
    print (f'El numero {num} NO es cuardado perfecto')
