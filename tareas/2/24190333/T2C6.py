def es_subcadena_palindroma(s, l, r):
    if l >= r: return True
    return s[l] == s[r] and es_subcadena_palindroma(s, l + 1, r - 1)
def es_palindroma(s):
    return es_subcadena_palindroma(s, 0, len(s) - 1)
palabra = input("Ingrese una palabra para verificar si es un palíndromo: ")
resultado = es_palindroma(palabra)
if resultado:
    print(f"La cadena {palabra} es palíndroma.")
else:
    print(f"La cadena {palabra} no es palíndroma.")