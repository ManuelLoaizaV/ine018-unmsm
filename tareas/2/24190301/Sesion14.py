def calcular_desviacion_estandar(listaDeNumeros):
    numeros = listaDeNumeros.split()
    listaDeNumeros = [int(x) for x in numeros]
    promedio = sum(listaDeNumeros)/len(listaDeNumeros)
    n=0
    sumaCuadrada=0
    while n<len(listaDeNumeros):
        sumaCuadrada = sumaCuadrada + (promedio-listaDeNumeros[n])**2
        n+=1

    sumaCuadrada = sumaCuadrada / len(listaDeNumeros)
    desviacionEstandar = sumaCuadrada**0.5
    print("La desviacion estandar es: ",desviacionEstandar)

numeros = "1 2 3 4 5"
calcular_desviacion_estandar(numeros)

