with open('conversion_metrica_entrada.txt', 'r') as archivo:
  metros = int(archivo.readline())

pulgadas = metros / 0.0254
pies = pulgadas / 12

with open('conversion_metrica_salida.txt', 'w') as imprimir:
  imprimir.write('Distancia en pulgadas: ' + str(pulgadas) + '\n')
  imprimir.write('Distancia en pies: ' + str(pies) + '\n')
