diccionario_morse={ 
  'A':'.-', 
  'B':'-...',
  'C':'-.-.', 
  'D':'-..', 
  'E':'.',
  'F':'..-.', 
  'G':'--.', 
  'H':'....',
  'I':'..', 
  'J':'.---', 
  'K':'-.-',
  'L':'.-..', 
  'M':'--', 
  'N':'-.',
  'O':'---', 
  'P':'.--.', 
  'Q':'--.-',
  'R':'.-.', 
  'S':'...', 
  'T':'-',
  'U':'..-', 
  'V':'...-', 
  'W':'.--',
  'X':'-..-', 
  'Y':'-.--', 
  'Z':'--..'
}
def texto_a_morse(texto):
  """Traduce texto a código Morse."""
  codigo_morse=""
  for letra in texto.upper():
    if letra.isalpha():
      codigo_morse+=diccionario_morse.get(letra, "")+" "
  return codigo_morse.strip()
  
def morse_a_texto(codigo_morse):
  """Traduce código Morse a texto."""
  texto=""
  palabras_morse=codigo_morse.split(" / ")
  for palabra_morse in palabras_morse:
    letras_morse=palabra_morse.split(" ")
    for letra_morse in letras_morse:
      for letra, codigo in diccionario_morse.items():
        if codigo==letra_morse:
          texto+=letra
    texto+=" "
  return texto.strip()


print("Traductor de código Morse")
while True:
  entrada=input("> ")
  if entrada=="":
    break
  if entrada[0].isalpha():
    codigo_morse=texto_a_morse(entrada)
    print(codigo_morse)
  elif entrada[0] in ('.', '-'):
      texto=morse_a_texto(entrada)
      print(texto)
  else:
      print("Entrada inválida.")