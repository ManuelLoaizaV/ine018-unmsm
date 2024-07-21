def mayusculas(s):
    n = len(s)
    resultado = []
    for i in range(n):
        if 'a' <= s[i] <= 'z':
            resultado.append(chr(ord(s[i]) - 32))
        else:
            resultado.append(s[i])
    return ''.join(resultado)

print(mayusculas("Manuel Loaiza"))
print(mayusculas("alex cisneros"))
print(mayusculas("ARIADNA ROSSA"))
print(mayusculas("pi=3.1415926535897932"))
s = "UnMsm2024"
print(mayusculas(s))
