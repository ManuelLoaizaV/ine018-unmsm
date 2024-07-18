codigos_postales = {
    'Breña': ['15082', '15083'],
    'Magdalena del Mar': ['15071', '15076', '15086'],
    'San Miguel' : ['15086', '15087', '15088'],
    'Pueblo Libre': ['15083', '15084', '15086', '15088'],
    'Jesus María' : ['2002', '15072', '15073', '15076', '15084'],
    'Lima' : ['07006', '15001', '15003', '15004', '15006', '15018', '15046', '15079', '15081', '15082', '15083', '15085', '15088', '15093', '15101', '15822', '21001'],
}

def obtener_codigo_postal_por_digito(codigo):
    distritos = []
    for distrito,codigos in codigos_postales.items():
        for c in codigos:
            if c == codigo:
                distritos.append(distrito)
    if len(distritos) == 0:
        return("EL código postal no existe")
    else:
        return distritos            


def obtener_codigo_postal_por_distrito(distrito):
    if distrito not in codigos_postales:
        return("El distrito no existe")
    else: 
        return codigos_postales[distrito]
    
def main(entrada):
    if entrada.isnumeric():
        return obtener_codigo_postal_por_digito(entrada)
    else:
        return obtener_codigo_postal_por_distrito(entrada)

print(main('15083'))