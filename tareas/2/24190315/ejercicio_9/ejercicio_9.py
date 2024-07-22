def obtener_yardas(pulgadas):
    yardas = pulgadas // 36
    if pulgadas%36 > 0:
        yardas = yardas + 1
    return yardas

def obtener_exceso_de_tela(pulgadas):
    return 36 * obtener_yardas(pulgadas) - pulgadas

def reporte_compra_de_tela(pulgadas):
    print("Necesitamos %s pulgada(s)" %pulgadas)
    print("Yardas a comprar: %s" %obtener_yardas(pulgadas))
    print(f"Exceso de tela: %s pulgada(s)" %obtener_exceso_de_tela(pulgadas))
    print()

reporte_compra_de_tela(71)
reporte_compra_de_tela(72)
reporte_compra_de_tela(73)