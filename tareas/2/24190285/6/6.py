with open('6entrada.txt',"r") as entrada:
  contenido = entrada.read().strip()
  #se lee el txt de entrada
  c=int(contenido)
conversion = (9 *c / 5)+ 32
#se reemplaza el valor de c
with open("6salida.txt", "w") as salida:
       salida.write(str(conversion))
#se muestra el resultado en el txt de salida