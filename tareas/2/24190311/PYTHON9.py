def EsTrianguloRectangulo (a,b,c):
    if a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
        return True
    else:
        return False
    
a= float (input("Ingrese longitud:") )
b= float (input ("Ingrese longitud:"))
c= float (input ("Ingrese longitud"))

if EsTrianguloRectangulo (a,b,c):
    print("Es triangulo rectangulo")
else:
    print ("No es triangulo rectangulo")