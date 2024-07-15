def ConvertirABuena(s):
  """Convierte una cadena a una "buena" cadena."""
  while True:
    cadena_mala = False
    for i in range(len(s) - 1):
      if s[i].islower() and s[i + 1].isupper():
        s = s[:i] + s[(i + 1) + 1:]
        cadena_mala = True
        break
    if not cadena_mala:
      break
  return s

print(ConvertirABuena("UNMSM"))
print(ConvertirABuena("s"))
print(ConvertirABuena("xabBAycCz"))
print(ConvertirABuena("xaaabbbBBBAAAd"))