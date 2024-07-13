codigos_postales= {}
codigos_postales["Brena"] = {15082, 15083}
codigos_postales["Magdalena del Mar"] = {7021, 15076, 15086}
codigos_postales["San Miguel"] = {15086, 15087, 15088}
codigos_postales["Pueblo Libre"] = {15083, 15084, 15086, 15088}
codigos_postales["Jesus Maria"] = {2002, 15072, 15073, 15076, 15084}
codigos_postales["Lima"] = {7006, 15001, 15003, 15004, 15006, 15018, 15046, 15079, 15081, 15082, 15083, 15085, 15088, 15093, 15101, 15822, 21001}

distritos= {}

for distrito, codigos_postales_del_distrito in codigos_postales.items():
    for codigo in codigos_postales_del_distrito:
        if codigo in distritos:
            distritos[codigo]+= [distrito]
        else:
            distritos[codigo] = [distrito]


with open ('4_entrada.txt', 'r') as entrada:
 entrada = str(entrada.readline()) 

with open('4_salida.txt', 'w') as salida: 
 if entrada.isdigit():
    if int(entrada) in distritos:
        salida.write(", ".join(distritos[int(entrada)])+"\n")

    else:
        salida.write("El codigo postal no existe.\n")

 else:
    if entrada in codigos_postales:
        for codigo in codigos_postales[entrada]:
            salida.write(", ".join(codigo)+"\n")
    else:
            salida.write("El distrito no existe.\n")
