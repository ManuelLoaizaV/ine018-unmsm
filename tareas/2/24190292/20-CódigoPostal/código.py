codigos_postales_cada_cuidad = {}
codigos_postales_cada_cuidad["Breña"] = {15082, 15083}
codigos_postales_cada_cuidad["Magdalena del Mar"] = {7021, 15076, 15086}
codigos_postales_cada_cuidad["San Miguel"] = {15086, 15087, 15088}
codigos_postales_cada_cuidad["Pueblo Libre"] = {15083, 15084, 15086, 15088}
codigos_postales_cada_cuidad["Jesus María"] = {2002, 15072, 15073, 15076, 15084}
codigos_postales_cada_cuidad["Lima"] = {17006, 15001, 15003, 15004, 15006, 15018, 15046, 15079, 15081, 15082, 15083, 15085, 15088, 15093, 15101, 15822, 21001}

codigoAciudad = {}
for ciudad in codigos_postales_cada_cuidad:
    for numeros in codigos_postales_cada_cuidad[ciudad]:
        if numeros in codigoAciudad:
            codigoAciudad[numeros]+=[ciudad]
        else:
            codigoAciudad[numeros]=[ciudad]
        
print("ingresa el nombre de tu ciudad o el código postal que bucas") 
while True:
    print(">>",end=" ")
    a=input()
    if a in codigos_postales_cada_cuidad:
        print(codigos_postales_cada_cuidad[a])
    elif a.isdigit():
        if int(a) in codigoAciudad:
            print(codigoAciudad[int(a)])
        else:
            print("no existe el código postal en mi memoria")
    else:
        print("No existe tu ciudad en mi memoria")