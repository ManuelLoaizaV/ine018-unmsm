import math
def main():

    with open('6_entrada.txt','r') as entrada:
        a= float(entrada.readline())
        b= float(entrada.readline())

    c= math.sqrt(a * a + b * b)

    with open('6_salida.txt','w') as salida:
        salida.write("La hipotenusa de este triangulo rectangulo es " +str(c))

if __name__== "__main__":
    main()
