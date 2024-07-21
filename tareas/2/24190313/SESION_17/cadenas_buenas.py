def convertir_a_buena(s):
  caracteres = []
  for i in range(len(s)):
      if caracteres and caracteres[-1].islower() and caracteres[-1].upper() == s[i]:
          caracteres.pop()
      else:
          caracteres.append(s[i])
  r = ''.join(caracteres)
  return r
s = input(str("Ingrese una cadena: "))
print(f"Cadena convertida: {convertir_a_buena(s)}")