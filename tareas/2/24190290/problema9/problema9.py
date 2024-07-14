#Funcion para generar una operacion 
def obtener_yardas(pulgadas):
    yardas = pulgadas // 36
    if pulgadas % 36 != 0:
        yardas += 1
    return yardas
#Funcion para verificar el exceso
def obtener_exceso_de_tela(pulgadas):
    exceso = 36 * obtener_yardas(pulgadas) - pulgadas
    return exceso

while True:
    try:
        #Leemos el txt de entrada
        with open('entrada9.txt', 'r') as entrada:
            pulgadas = int(entrada.read())  
        if pulgadas == 0:
            break
        #Trascribimos la respuesta a txt de 'salida17.txt'
        with open(''salida17.txt'9.txt', 'w') as 'salida17.txt':
            'salida17.txt'.write(f"Para {pulgadas} pulgadas compramos {obtener_yardas(pulgadas)} yardas y nos sobran {obtener_exceso_de_tela(pulgadas)} pulgadas.")
    except ValueError:
        #Trascribimos la respuesta a txt de 'salida17.txt'
        with open(''salida17.txt'9.txt', 'w') as 'salida17.txt':
            'salida17.txt'.write("Entrada inválida. Por favor, ingrese un número entero.")
    break
