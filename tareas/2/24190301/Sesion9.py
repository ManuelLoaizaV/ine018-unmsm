def conjetura_de_collatz(numero):
    while numero != 1:
     if numero%2==0:
        print(numero, " es par, entonces tomo la mitad: ", numero/2)
        numero = numero /2
     else:
        print(numero, " es impar, entonces hago 3n+1: ", 3*numero+1)
        numero = 3*numero + 1
numero = 15
conjetura_de_collatz(numero)
