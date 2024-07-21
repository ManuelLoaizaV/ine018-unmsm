def main():
    cod = {"Breña": [15082, 15083],}
    distritos = {}

    for distrito, codigos in cod.items():
        for codigo in codigos:
            
            if codigo in distritos:

                distritos[codigo].append(distrito)
            else:
                distritos[codigo] = [distrito]

    with open("20_entrada.txt", "r") as entrada:
        consultas = entrada.read().splitlines()

    respuestas = []
    for entrada in consultas:
        if entrada.isdigit():
            codigo = int(entrada)

            if codigo in distritos:

                respuesta = "Los distritos para el código postal " + str(codigo) + " son: " + ", ".join(distritos[codigo])
                respuestas.append(respuesta)
            else:

                respuestas.append("El código postal " + str(codigo) + " no existe.")
        else:

            if entrada in cod:
                
                respuesta = "Los códigos postales para el distrito " + entrada + " son: " + ", "
                respuestas.append(respuesta)

            else:
                respuestas.append("El distrito " + entrada + " no existe.")

    with open("20_salida.txt", "w") as salida:
        salida.write(respuesta)

if __name__ == "__main__":
    main()
