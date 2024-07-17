def Convertir_a_buena(s) :
    caracteres = []
    for i in s :
        if caracteres and 'a' <= tope <= 'z' and 'A' <= chr(ord(i))  <= 'Z':
          caracteres.pop()
        else:
          caracteres.append(i)
          tope = i
    r = []
    while caracteres:
        r += caracteres.pop()
    r.reverse()
 
    return ''.join(r)

with open('Cadenas_buenas_entrada.txt', 'r') as archivo:
    s = archivo.readline()

with open('Cadenas_buenas_salida.txt' , 'w') as imprimir:
    imprimir.write(str(Convertir_a_buena(s)))