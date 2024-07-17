def Mayusculas(s):
  resultado = []
  for char in s :
    if 'a' <= char <= 'z' :
      resultado.append(chr(ord(char) - ord('a') + ord('A') ))
    else: 
      resultado.append(char)
  return ''.join(resultado)

with open('mayusculas_entrada.txt', 'r') as archivo:
  s = archivo.readline()

with open('mayusculas_salida.txt', 'w') as imprimir:
  imprimir.write(str(Mayusculas(s)))