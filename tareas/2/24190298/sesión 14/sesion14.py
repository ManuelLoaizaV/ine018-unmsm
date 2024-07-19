def ConvertirMayusculas(s):
    n=len(s)
    cadenafinal=""
    for i in range(0,n):
        if 'a'<= s[i]<= 'z':
            cadenafinal= cadenafinal+chr(ord(s[i])-ord('a')+ ord('A'))
        else:
            cadenafinal=cadenafinal+s[i]
    return cadenafinal

if __name__ == "__main__":
    s= input("Escriba la cadena que pasará a mayúsculas: ")
    print(ConvertirMayusculas(s))