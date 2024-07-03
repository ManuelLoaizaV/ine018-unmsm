from collections import deque
a="hHOLAGaaaaAAAA"
stack="xaA"
def esBool(abcd):
    
    for letra in range(len(abcd)):
        if letra<len(abcd)-1:
            if abcd[letra]==abcd[letra+1].lower() and abcd[letra+1].isupper():
                return True
    
    return False


def cadena_buena(a,stack):
    
    while esBool(a) :
        stack=""
        for letra in range(len(a)):
            if letra == 0:
                if a[0].isupper() or not(a[0] == a[1].lower() and a[1].isupper()):
                    stack+=a[0]                
            elif letra == len(a) - 1:
                if a[letra].islower() or (a[letra-1].isupper() or (a[letra-1].upper() != a[letra])):
                    stack+=a[len(a)-1]
            elif 0 < letra < len(a) - 1:
                if  (a[letra].isupper() or not(a[letra] == a[letra+1].lower() and a[letra+1].isupper())) and (a[letra].islower() or (a[letra-1].isupper() or (a[letra-1].upper() != a[letra]))):
                    stack+=a[letra]
        a=stack
    else:
        stack=a
    print(stack)
 
     
cadena_buena(a,stack)