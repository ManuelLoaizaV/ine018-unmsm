with open('6entrada.txt',"r") as entrada:
  contenido = entrada.read().strip()
  
  c=int(contenido)
conversion = (9 *c / 5)+ 32

with open("6salida.txt", "w") as salida:
       salida.write(str(conversion))