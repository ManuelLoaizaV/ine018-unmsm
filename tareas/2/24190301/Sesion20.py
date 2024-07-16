codigos_postales = {
  "Pueblo Libre": [15083, 15084, 15086, 15088],
  "Magdalena del Mar": [15086],
  "San Miguel": [15086],
  "Jesus María": [2002, 15072, 15073, 15076, 15084],
  "Lima": [7006, 15001, 15002, 15004, 15006, 15018, 15046, 15079, 15081, 15082, 15083, 15085, 15088, 15093, 15101, 15822, 21001],
}

def si_es_codigo(codigo):
  codigo = int(codigo)
  esta = False
  for distrito,codigos in codigos_postales.items():
          if codigo in codigos:
              esta = True
              print(distrito)
  if not esta:
              print("Elcodigo postal no existe")

def si_es_distrito(distrito):
  if distrito in codigos_postales:
      for codigo in codigos_postales[distrito]:
          print(codigo)
  else:
    print("El distrito no existe")

cadena = input("Ingrese el codigo postal o distrito: ")
if cadena.isdigit():
 si_es_codigo(cadena)
else:
  si_es_distrito(cadena)
