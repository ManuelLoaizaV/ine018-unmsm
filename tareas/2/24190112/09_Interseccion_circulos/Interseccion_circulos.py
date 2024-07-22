import re
import math

def Leer(archivo_entrada):
    with open(archivo_entrada, encoding="utf-8") as entrada:
        texto = entrada.read()
    return texto

def Extraer(texto):
    numeros = re.findall(r'-?\d+', texto)
    numeros = [int(num) for num in numeros]
    return numeros

def Distancia_centros(x1,y1,x2,y2):
    dist1 = x1 - x2
    dist2 = y1 - y2
    distancia = math.sqrt(dist1*dist1 + dist2*dist2)
    return distancia

def Escribir(archivo_salida, x1, y1, r1, x2, y2, r2):
    with open(archivo_salida, "w", encoding="utf-8") as salida:
        if Intersectan(x1,y1,r1,x2,y2,r2):
            salida.write(f"Los circulos con centros {x1} , {y1} y {x2} , {y2} se intersectan.")
        else:
            salida.write(f"Los circulos con centros {x1} , {y1} y {x2} , {y2} no se intersectan.")

def Intersectan(x1,y1,r1,x2,y2,r2):
    if(Distancia_centros(x1,y1,x2,y2) <= r1 + r2):
        return True
    else:
        return False

def main():
    archivo_entrada = "entrada_ejercicio9.txt"
    archivo_salida = "salida_ejercicio9.txt"
    
    texto = Leer(archivo_entrada)
    num = Extraer(texto)
    
    x1, y1, r1, x2, y2, r2 = num
    Escribir(archivo_salida, x1, y1, r1, x2, y2, r2)

if __name__ == "__main__":
    main()
