# Código  Morse

En mayo de 1844, Samuel Morse envío el mensaje
"What hath God wrought!" vía telégrafo desde
Washington a Baltimore, marcando el inicio
de la era de la comunicación electrónica.
Para hacer posible transmitir información usando solo
la presencia o ausencia de un tono,
Morse diseñó un sistema de codificación en el cual
las letras y otros símbolos son representados como
sucesiones codificadas de tonos largos y cortos,
tradicionalmente llamados *puntos* y *guiones*.
En el código Morse, las 26 letras del alfabeto son representadas
por los siguientes códigos:

```
A .-
B -...
C -.-.
D -..
E .
F ..-.
G --.
H ....
I ..
J .---
K -.-
L .-..
M --
N -.
O ---
P .--.
Q --.-
R .-.
S ...
T -
U ..-
V ...-
W .--
X -..-
Y -.--
Z --..
```

Escriba un programa que lea las líneas de un usuario
y traduzca cada línea desde o hacia código Morse dependiendo
del primer caracter de la línea:
- Si la línea comienza con una letra,
traducirás esta a código Morse.
Cualquier caracter distinto a las 26 letras debe ser ignorado.
- Si la línea comienza con un punto o un guion,
esta debe ser leída como una serie de caracteres en
código Morse y traducidas a letras.
Cada sucesión de puntos y guiones estará separada por espacios.
Como no hay una codificación para el espacio entre palabras,
los caracteres del mensaje traducido estarán de corrido.

El programa debe terminar cuando un usuario ingresa una línea en blanco.
Una ejemplo de ejecución utilizando los mensajes entre Titanic y Carpathia en 1912 se ve de la siguiente manera:

```
Traductor de código Morse
> SOS TITANIC
... --- ... - .. - .- -. .. -.-.
> WE ARE SINKING FAST
.-- . .- .-. . ... .. -. -.- .. -. --. ..-. .- ... -
> .... . .- -.. .. -. --. ..-. --- .-. -.-- --- ..-
HEADINGFORYOU
>
```