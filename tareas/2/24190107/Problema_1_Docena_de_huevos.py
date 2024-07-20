
def ObtenerDocenas (numero):
    docenas = int(numero/12)
    if  numero % 12 != 0: 
        docenas += 1
    return docenas

numero =int(input("Introduce la cantidad de huevos: "))
Cantidad=ObtenerDocenas(numero)
print(f"Docenas: {Cantidad} ")

#el orden es importante aqui, no puede ser , :0.