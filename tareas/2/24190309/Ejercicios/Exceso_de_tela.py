def Obtener_yardas(pulgadas):
    yardas = int(pulgadas / 36)
    if pulgadas % 36 > 0:
        yardas = yardas + 1
    return yardas

def Obtener_exceso_de_tela(pulgadas):
    return 36 * Obtener_yardas(pulgadas) - pulgadas

with open('Exceso_de_tela_entrada.txt', 'r') as archivo:
    pulgadas = int(archivo.readline())

with open('Exceso_de_tela_salida.txt', 'w') as imprimir:
    imprimir.write('Necesitamos ' + str(pulgadas) + ' pulgada(s)' + '\n')
    imprimir.write('Yardas a comprar: ' + str(Obtener_yardas(pulgadas)) + '\n')
    imprimir.write('Exceso de tela: ' + str(Obtener_exceso_de_tela(pulgadas)) + ' pulgada(s)' + '\n')