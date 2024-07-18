tabla = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z'
}

def textoAM (t):
    vt = []
    for char in t.upper():
        if char in tabla:
            vt.append(tabla[char])
    return ' '.join(vt)

def morseAT (m):
    vm= []
    morse_chars = m.split()
    for char in morse_chars:
        if char in tabla:
            vm.append(tabla[char])
    return ''.join(vm)

while True:
    l = input("> ").strip()
    if l == "":
        break
    elif l[0].isalpha():
        print( tabla(l))
    elif l[0] in ['.', '-']:
        print( morseAT(l))