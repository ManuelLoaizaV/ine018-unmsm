def convertir_a_buena(cadena):
    lista = list(cadena)
    i = 0
    while i < len(lista)-1:
        if lista[i] != lista[i+1] and lista[i].lower() == lista[i+1].lower():
            del lista[i]
            del lista[i]
        else:
            i+=1
    cadena1 = "".join(lista)
    print("La cadena buena es:",cadena1)

cadena = "HholaMmunndoO"
convertir_a_buena(cadena)