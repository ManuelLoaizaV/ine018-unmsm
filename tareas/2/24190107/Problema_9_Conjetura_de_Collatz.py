   
def Conjetura_Collaz(dato):
    valor = True
    while valor:
     if dato >= 2:
        if dato % 2 == 0:
           da = dato //2
           print(f"El valor de {dato}  es par, entonces { dato } / 2 = {da})")
        else :
            da = 3*dato + 1
            print(f"El valor de {dato} es impar, entonces 3 * { dato } + 1 = {da})")
        dato = da
     else:
        valor = False
      
 #aprendi a usar los corchetes y cada vez respetar los espacios correspondientes.
dato = int(input("Introduce un numero positivo: "))
Conjetura_Collaz(dato)