def InvertirCadena(s):
    r = ""
    for i in range(len(s) - 1, -1, -1):
      r += s[i]
    return r

def ConvertirABuena(s):
    caracteres = []
    
    for i in s:
        if caracteres and caracteres[-1].islower() and caracteres[-1].upper() == i:
            caracteres.pop()
        else:
            caracteres.append(i)
    
    r = ""
    while caracteres:
        r += caracteres.pop()
    
    with open('4_salida.txt', 'w') as salida: 
     salida.write(str(InvertirCadena(r))) 


with open ('4_entrada.txt', 'r') as entrada:
  s = str(entrada.readline()) 

ConvertirABuena(s)
