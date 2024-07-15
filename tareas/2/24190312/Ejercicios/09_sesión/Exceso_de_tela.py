def ObtenerYardas(pulgadas):
    yardas = pulgadas // 36
    if pulgadas % 36 > 0:
        yardas += 1
    return yardas

def ObtenerExcesoDeTela(pulgadas):
    return 36 * ObtenerYardas(pulgadas) - pulgadas

def ReporteCompraDeTela(pulgadas):
    print(f"Necesitamos {pulgadas} pulgada(s)")
    print(f"Yardas por comprar: {ObtenerYardas(pulgadas)}")
    print(f"Exceso: {ObtenerExcesoDeTela(pulgadas)} pulgada(s)")
    print()

def main():
    pulgadas_comprar = int(input("Ingrese el número de pulgadas de tela por comprar: "))
    ReporteCompraDeTela(pulgadas_comprar)

if __name__ == "__main__":
    main()
