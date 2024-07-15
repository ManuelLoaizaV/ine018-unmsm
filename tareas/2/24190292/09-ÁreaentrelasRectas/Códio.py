import re
import math
def LeerDocumento(archivoEntrada):
    with open(archivoEntrada, 'r') as archivo:
        contenido = archivo.read()
    return contenido

def Extraer(contenido):
    numeros=re.findall(r'-?\d+\.?\d*',contenido)
    numeros=[float(num) for num in numeros]
    return numeros

def Escribir(archivoSalida,texto):
    with open(archivoSalida, 'w') as archivo:
        archivo.write(texto)

def absisa_de_interseccion(m1 , b1, m2, b2):
    return ( b2 - b1 )/( m1 - m2 )
    
    
def distancia( x , y , x1, y1 ):
    return math.sqrt(( x - x1 )**2 + ( y - y1 )**2 )

def CalcularAreaEntreLasRectas(m1,  b1, m2,  b2, m3, b3):
    x1=absisa_de_interseccion(m1 ,b1 ,m2, b2)
    y1= m1 * x1 + b1
    x2=absisa_de_interseccion(m2 ,b2 ,m3, b3)
    y2= m2 * x2 + b2
    x3=absisa_de_interseccion(m1 ,b1 ,m3, b3)
    y3= m3 * x3 + b3
    
    distancia1 = distancia(x1 , y1 , x2 , y2 )
    distancia2 = distancia(x2 , y2 , x3 , y3 )
    distancia3 = distancia(x1 , y1 , x3 , y3 )
    
    p = (distancia1 + distancia2 + distancia3)/2
    area=math.sqrt(p * (p - distancia1) * (p - distancia2) * (p - distancia3))

    return area
    
def main():
    Entrada = 'entradaAreas.txt'
    Salida = 'salidaAreas.txt'
    contenido = LeerDocumento(Entrada)
    n = Extraer(contenido)
    m1, b1, m2, b2, m3, b3 = n
    resultado=round(CalcularAreaEntreLasRectas(m1,b1,m2,b2,m3,b3),2)
    texto="el área es : " + str(resultado)
    Escribir(Salida,texto)    
if __name__ == "__main__":
    main()