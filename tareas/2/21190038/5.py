monse = {
    'A' : '.-','B' : '-...','C' :'-.-.','D' : '-..','E' : '.','F' : '..-.','G' : '--.','H' : '....','I' : '..','J' : '.---',
    'K' : '-.-','L' : '.-..','M' : '--','N' : '-.','O' : '---','P' : '.--.','Q' : '--.-','R' : '.-.','S' : '...','T' : '-',
    'U' : '..-','V' : '...-','W' : '.--','X' : '-..-','Y' : '-.--','Z' : '--..',
}


mensaje = input()
cambio =[]
morse = []

for letra in mensaje:
    cambio.append(letra)

for letra in cambio:
    morse.append(monse.get(letra,''))



print(''.join(morse))