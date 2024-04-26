## ¿Por qué C++?
¡C++ es aún un lenguaje muy popular!

![2023 developer survey](/assets/gifs/2023-developer-survey.gif)

[*Stack Overflow Developer Survey 2023.*](https://survey.stackoverflow.co/2023/#most-popular-technologies-language)

Lo utilizamos en cursos:
- Lenguaje de programación.
- Programación avanzada.
- Arquitectura de computadoras.
- Computación paralela.
- Robótica médica.

Y también en la vida real!

![Usuarios de C++](/assets/images/cpp-users.png)

*Java, Spirit, Windows 11, World of Warcraft, Google Chrome.*

Además, es bastante rápido.

![Tiempos de ejecución de programas en distintos lenguajes](/assets/images/cpp-time-comparison.png)

[*Fourment M, Gillings MR. A comparison of common programming languages used in bioinformatics. BMC Bioinformatics. 2008 Feb 5;9:82.*](https://doi.org/10.1186/1471-2105-9-82)

## ¿Qué es C++?

### Assembly
Primero meditemos sobre assembly:
- Instrucciones increíblemente simples (sumar, restar, mover bits).
- Un buen código en assembly es extremadamente veloz.
- Control total sobre nuestros programas. 

```asm
section .text
global _start              ;must be declared for linker (ld)
_start:                    ;tell linker entry point
 mov edx,len               ;message length
 mov ecx,msg               ;message to write
 mov ebx,1                 ;file descriptor (stdout)
 mov eax,4                 ;system call number (sys_write)
 int 0x80                  ;call kernel
 mov eax,1                 ;system call number (sys_exit)
 int 0x80                  ;call kernel
section .data
msg db 'Hola, mundo!',0xa  ;our dear string
len equ $ - msg            ;length of our dear string
```

¿Por qué no usamos siempre assembly?
- Requerimos mucho código para implementar tareas simples.
- Difícil de entender el código de otras personas.
- Poco portátil pues está amarrado a la arquitectura del computador.

Desarrollar con assembly era muy difícil pero las computadoras solo entendían assembly.

Nuestros ancestros se hicieron la siguiente lluvia de ideas:
- El código fuente puede ser escrito en un lenguaje más intuitivo.
- Un programa adicional puede convertir este código fuente en assembly.

¡A ese programa adicional le llamamos compilador!

Un **compilador** es un programa que toma código
y construye un programa que podemos correr.

### C

Ken Thompson y Dennis Ritchie crearon C en 1972.

![KT & DR](/assets/images/kt-dr.jpg)

*KT y DR, creadores del lenguaje C.*

> Ken Thompson también es co-diseñador de Go desde el 2007,
un lenguaje simple, veloz y divertido para desarrollo back-end
y se ha convertido en [una tendencia durante los últimos años](https://trends.stackoverflow.co/?tags=go).

C hizo fácil escribir código que sea
- Rápido.
- Simple.
- Multiplataforma.

Su simplicidad lo hizo muy popular, lo cual también era su debilidad:
- No existían **objetos** ni **clases**.
- Difícil de escribir código que funcione **genéricamente**.
- **Tedioso** al escribir programas largos.

### C++

En 1983, Bjarne Stroustrup creó C++.
Nada mejor que escuchar al creador explicar el porqué en la siguiente entrevista:

[![Bjarne Stroustrup](http://img.youtube.com/vi/JBjjnqG0BP8/0.jpg)](https://www.youtube.com/watch?v=JBjjnqG0BP8)

*Bjarne Stroustrup: Why I Created C++.*

Él quería un lenguaje que cumpla con lo siguiente:
- Rápido.
- Simple.
- Multiplatafotma.
- **Que tenga características de alto nivel**.

![Evolución de C++](/assets/images/cpp-evolution.png)
*Evolución de C++.*

Su filosofía era la siguiente:
- Solo añadir características si resuelven un problema real.
- Los programadores deben ser libres de elegir su propio estilo.
- Permitir al programador control absoluto si lo desea.
- No sacrificar el rendimiento excepto como último recurso.
- Imponer seguridad en tiempo de compilación siempre que sea posible.

### Sintaxis versus semántica

Definamos los siguientes términos:
- Sintaxis: las reglas para construir sentencias gramaticales en un lenguaje.
- Semántica: Significado.

Estas definiciones son independientes de referirse a un lenguaje humano o un lenguaje de programación.

Consideremos el siguiente ejemplo:

> Amortajadas las pupilas, traza su aullido pastoral un perro.

Hay muchas cosas ocurriendo en esta oración, sintácticamente hablando.
La puntuación al final de la oración es parte de la sintaxis, al igual que la coma.
La oración comienza con un complemento adverbial ("Amortajadas las pupilas").
El verbo de la oración es "traza",
el cual indica la acción realizada por el sujeto ("un perro").
El complemento directo del verbo es "su aullido pastoral".
Es una oración gramaticalmente correcta.

La semántica de la oración está relacionada con
una metáfora explosiva y religiosa.
Las yuxtaposiciones inflaman las diferencias entre impulsos religiosos y naturalistas.
Por ejemplo, "aullido pastoral" combina lo simple e idílico de "pastoral"
con lo violento y desesperado de "aullido".
Un poema como este no se construye sobre una comprensión preconcebida de la realidad.
Al contrario, está desagarrado por gestos brutales de hiperrealidad.


¿Por qué esto es relevante?

Conforme descubramos todo lo que podemos hacer con C++,
iremos aprendiendo la sintaxis que tenemos que seguir
(i.e. cómo escribir las líneas de código que el compilador digerirá)
y la semántica asociada (i.e. qué hace o significa dicha sintaxis).

### Pero ... ¿qué es C++?
