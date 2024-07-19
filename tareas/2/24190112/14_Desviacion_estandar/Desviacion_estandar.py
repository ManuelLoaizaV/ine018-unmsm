import re
import math

def Leer(archivo_entrada):
    with open(archivo_entrada, encoding="utf-8") as entrada:
        texto = entrada.read()
    return texto

def Extraer(texto):
    numeros = re.findall(r'-?\d+', texto)
    numeros = [float(num) for num in numeros]
    return numeros

def Escribir(archivo_salida, datos):
    with open(archivo_salida, "w", encoding="utf-8") as salida:
        resultado = Calcular_desviacion_estandar(datos)
        salida.write(f"La desviación estándar de la lista de números dada es: {resultado:.2f}")
        
#Para sumar en una lista que seria como el equivalente a un vector es mas fácil.

def Calcular_desviacion_estandar(datos):
    
    media = sum(datos) / len(datos)

    suma_cuadrados_diferencias = sum((dato - media)**2 for dato in datos)

    varianza = suma_cuadrados_diferencias / len(datos)

    desviacion_estandar = math.sqrt(varianza)

    return desviacion_estandar

def main():
    archivo_entrada = "entrada_ejercicio14.txt"
    archivo_salida = "salida_ejercicio14.txt"
    
    texto = Leer(archivo_entrada)
    datos = Extraer(texto)

    Escribir(archivo_salida, datos)

if __name__ == "__main__":
    main()
