# Proyecto: Cálculo con SymPy
Resolver problemas de prácticas o exámenes finales de cálculo.
Utilizar la biblioteca SymPy.

## Funcionamiento y ejecución del proyecto:
Para este proyecto, nos piden utilizar la biblioteca SymPy de Python que lo que hace es manipular expresiones matemáticas, o resolver problemas matemáticos de nivel universitario, que nos permite construir una calculadora, además de hacer nuestros códigos de forma más simple y entendible.

Primero lo que hice fue instalar la biblioteca utilizando el comando «pip install sympy». Tras importar el paquete SymPy como «sp», la creación de un símbolo «x» representa un valor desconocido que se efectúa con el comando «x = sp.symbol(«x»)». Con esto, es posible crear varios símbolos, como «x» e «y», en función del número de incógnitas y estos símbolos se pueden sumar, restar, multiplicar y dividir a voluntad nuestra.

Para la mayoría de códigos use sp.sqrt() y sp.root() para representar raíces pero root() maneja cualquier índice raíz, lo que lo hace más versátil que simplemente usar sp.sqrt() para raíces cuadradas. Además, también hice uso de sen() que representa el sin() que representa la función trigonométrica seno. 

### En el caso del problema de la PC1:
Hice uso de la función solveset que lo que hace es que devuelve un objeto de conjunto y un objeto de conjunto se encarga de todos los tipos de salida. Para los casos en los que no "conoce" todas las soluciones, solo toma la ecuación, las variables a resolver y el argumento opcional domain sobre el que se resolverá la ecuación.


### En el caso del problema de la PC2:
Hice uso de la función diff(f(x),x), ya que nos sirve para el cálculo de derivadas,  donde f(x) es la función a derivar y x es la variable de derivación.
También hice uso de la función sympify() que permite simplificar una expresión ya que pertenece al grupo de "manipulaciones algebraicas" de Python que permiten manipular y simplificar expresiones y fórmulas.


### En el caso del problema del examen parcial:
Hice uso de la función limit ya que me permite encontrar los límites de forma sencilla según su sintaxis de limit(función, variable, punto). Así, para calcular el límite de f(x) como x -> 0, deberías usar la siguiente expresión limit(f, x, 0).
En la sentencia limit hay que explicitar la función, la variable y el punto donde queremos calcular el límite, separados por comas.

Tras esto, le doy al botón de ejecutar y he podido dar fé del resultado que me ha dado al corroborarlo con mi respuesta del examen o práctica dada.
