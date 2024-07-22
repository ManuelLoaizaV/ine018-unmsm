def Convert_Mayus(lines):
    noan = ""
    for letra in lines:
         if 'a' <= letra <= 'z':
            upper =chr(ord(letra) - 32)
            noan += upper
         else:
            noan += letra
        

    return noan
#intento acostumbrarme al codigo ascii.


lines = str(input("Introduce la cadena a trasformar: "))
resultado = Convert_Mayus(lines)
print(f"la cadena convertida sera { resultado } ")