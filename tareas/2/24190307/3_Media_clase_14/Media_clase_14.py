def media(str):
    lista_numeros = []
    # Me duele llamarlo lista en vez de vector xd
    # Vacío para introducir datos

    for numeros in str:
        valores = int(numeros)
        lista_numeros.append(valores)
    # Iterando, lo que no me gusta en C++ y prefiero mi for con el tamaño :,

    if len(lista_numeros) == 0:
        return 0.0
    # En caso no introduzca nada e.e
    suma = 0
    for sumandos in lista_numeros:
        suma += sumandos
    
    medias = suma / len(lista_numeros)
    return medias

with open("Media_entrada.txt", "r") as entrada:
    linea = entrada.readline().split()
    linea2 = entrada.readline().split()
    #Esta linea es una lista de str me dice, creo que... lo entiendo    

resultado = media(linea)
resultado2 = media(linea2)

with open("Media_salida.txt", "w") as salida:
    salida.write("La media de {" + ", ".join(linea) + "} es " + str(resultado) +"\n" +
                 "La media de {" + ", ".join(linea2) + "} es " + str(resultado2))