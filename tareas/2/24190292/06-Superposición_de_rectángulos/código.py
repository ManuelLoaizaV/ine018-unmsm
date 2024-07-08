import re
def LeerDocumento(archivoRuta):
    with open(archivoRuta , 'r') as archivo:
        contenido = archivo.read()
    return contenido

def ExtraigoNumeros(contenido):
    numeros= re.findall(r'-?\d+',contenido)
    numeros = [int(num) for num in contenido]
    return numeros

def superponenrectángulos(a,b,alto_1,ancho_1,x,y,alto_2,ancho_2):
        if y > b + alto_1 or b > y + alto_2:
            return False
        if a + ancho_1 < x or x + ancho_2 < a:
            return False
        if a < x and x + ancho_2 < a + ancho_1 and y + alto_2 < b + alto_1 and b < y:
            return False
        if a > x and x + ancho_2 > a + ancho_1 and y + alto_2 > b + alto_1 and b > y:
            return False
        return True

def Salida(archivoRuta,texto):
    with open(archivoRuta,'w') as archivo:
        archivo.write(texto)

def main():
    archivoRuta = 'entrada.txt'
    contenido = LeerDocumento(archivoRuta)
    n = ExtraigoNumeros(contenido)
    
    if superponenrectángulos(n[0],n[1],n[2],n[3],n[4],n[5],n[6],n[7]):
        texto="Los rectánglos se intersecan? -> verdad"
    else:
        texto="Los rectánglos se intersecan? -> falso"
    Salida(archivoRuta,texto)

if __name__ == "__main__":
    main()
