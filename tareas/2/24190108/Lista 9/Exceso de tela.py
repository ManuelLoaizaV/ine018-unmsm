def obtener_yardas(pulgadas):
    yardas = pulgadas / 36
    if pulgadas % 36 > 0:
        yardas += 1
    return yardas

def obtener_exceso_de_tela(pulgadas):
    return 36 * obtener_yardas(pulgadas) - pulgadas

def reporte_compra_de_tela(pulgadas):
    print(f"Necesitamos {pulgadas} pulgada(s)")
    print(f"Yardas a comprar: {obtener_yardas(pulgadas)}")
    print(f"Exceso de tela: {obtener_exceso_de_tela(pulgadas)} pulgada(s)")
    print()

def main():
    reporte_compra_de_tela(71)
    reporte_compra_de_tela(72)
    reporte_compra_de_tela(73)

main()