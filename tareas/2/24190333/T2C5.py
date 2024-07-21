def es_numerica(s):
    return s.isdigit()
codigos_postales = {
    "Breña": [15082, 15083],
    "Magdalena del Mar": [7021, 15076, 15086],
    "San Miguel": [15086, 15087, 15088],
    "Pueblo Libre": [15083, 15084, 15086, 15088],
    "Jesus María": [2002, 15072, 15073, 15076, 15084],
    "Lima": [7006, 15001, 15003, 15004, 15006, 15018, 15046, 15079, 15081, 15082, 15083, 15085, 15088, 15093, 15101, 15822, 21001]
}
print ("Ingrese el distrito a buscar teniendo en cuenta las mayúsculas:")
distritos = {}
for distrito, codigos in codigos_postales.items():
    for codigo in codigos:
        if codigo in distritos:
            distritos[codigo].append(distrito)
        else:
            distritos[codigo] = [distrito]
while True:
    entrada = input("> ")
    if es_numerica(entrada):
        codigo = int(entrada)
        if codigo in distritos:
            for distrito in distritos[codigo]:
                print(distrito)
        else:
            print("El código postal no existe.")
    else:
        if entrada in codigos_postales:
            for codigo in codigos_postales[entrada]:
                print(codigo)
        else:
            print("El distrito no existe.")
