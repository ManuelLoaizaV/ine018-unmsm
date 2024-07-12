def ObtenerYardas(pulgadas):
    yardas=pulgadas//36
    if pulgadas%36>0:
      yardas+=1
    return yardas

def  ObtenerExcesoDeTela(pulgadas): 
     return 36 * ObtenerYardas(pulgadas) - pulgadas 

def ReporteCompraDeTela(pulgadas):
    with open('2_salida.txt', 'w') as salida:
       salida.write("Necesitamos: " + str(pulgadas) + " pulgada(s)\n" 
      "Yardas a comprar: " + str(ObtenerYardas(pulgadas)) +"\n"
      "Exceso de tela: "  + str (ObtenerExcesoDeTela(pulgadas)) + " pulgadas(s)\n")

with open ('2_entrada.txt', 'r') as entrada:
  pulgadas = int(entrada.readline()) 

  ReporteCompraDeTela(pulgadas)
