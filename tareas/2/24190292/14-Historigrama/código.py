import re
def LeerDocumento(archivoRuta):
    with open(archivoRuta , 'r') as archivo:
        contenido = archivo.read()
    return contenido

def ExtraigoNumeros(contenido):
    numeros= re.findall(r'-?\d+',contenido)
    numeros = [int(num) for num in numeros]
    return numeros

def Salidas(archivoRuta):
    with open(archivoRuta,'w') as archivo:
        a=0
        for dat in historigrama:
            if a < 10:
                archivo.write("0")
            archivo.write(f"{a}: ")
            for _ in range(dat):
                archivo.write("*")
            archivo.write("\n")
            a+=2


Entrada = 'EntradaHist.txt'
Salida = 'SalidaHist.txt'
contenido = LeerDocumento(Entrada)
numeros= ExtraigoNumeros(contenido)
 
historigrama = [0,0,0,0,0,0,0,0,0,0,0]
for bal in numeros:
    if 0<=bal<2: 
        historigrama[0]+=1
    if 2<=bal<4:
        historigrama[1]+=1
    if 4<=bal<6: 
        historigrama[2]+=1
    if 6<=bal<8:
        historigrama[3]+=1
    if 8<=bal<10: 
        historigrama[4]+=1
    if 10<=bal<12:
        historigrama[5]+=1
    if 12<=bal<14: 
        historigrama[6]+=1
    if 14<=bal<16:
        historigrama[7]+=1
    if 16<=bal<18: 
        historigrama[8]+=1
    if 18<=bal<20:
        historigrama[9]+=1
    if 20 == bal:
        historigrama[10]+=1

Salidas(Salida)

