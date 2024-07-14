import math

#Introducimos o leemos el txt de entrada
with open('entrada6.txt', 'r') as entrada:
    A = float(entrada.read())

#operamos
pulgadas = A / 0.0254
pie = pulgadas / 12

#Trascribe la respuesta al txt de salida
with open('salida6.txt', 'w') as salida:
    salida.write(f"Pulgadas: {pulgadas}\n")
    salida.write(f"Pies: {pie}\n")