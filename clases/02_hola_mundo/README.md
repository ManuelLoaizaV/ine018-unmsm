## Hola, mundo!

Ya sea que estén utilizando un IDE online como Replit,
Neovim y g++ en Linux,
o DevC++ y MinGW en Windows,
escribiremos el siguiente código en nuestro editor de texto:

```cpp
#include <iostream>

int main(void) {
    std::cout << "Hola, mundo!" << std::endl;    
    return 0;
}
```

Desde aquí comenzaremos a explorar qué pasa en cada línea.

## Directivas `#include`

En todo lenguaje queremos tener la posibilidad de importar
bibliotecas escritas previamente.
En C++ utilizamos las sentencias `#include`.

La sintaxis para dichas sentencias es la siguiente
cuando se trata de bibliotecas estándares del sistema:

```cpp
#include <NOMBRE_BIBLIOTECA>
```

Cuando se trata de bibliotecas definidas por los usuarios utilizamos lo siguiente:

```cpp
#include "NOMBRE_BIBLIOTECA"
```

Estas directivas son diferentes a todas las demás sentencias que hemos visto
puesto que no terminan en punto y coma.
C++ tiene como regla leer todo hasta el fin de línea frente a una sentencia `#include`.

En particular, estamos importando la biblioteca `<iostream>` porque nos da acceso a lo siguiente:
- `std::cout`
- `std::endl`

## La función `main`

Ahora exploraremos la definición de nuestra función `main` de nuestro programa.

En el mundo de las matemáticas, una función realiza tres cosas:

- Recibe uno o múltiples valores de entrada.
- Realiza cierto trabajo.
- Retorna un resultado.

Las funciones en C++ hacen exactamente lo mismo.
La sintaxis para definir una función es la siguiente:

```cpp
TIPO_DATO NOMBRE_FUNCION(PARAMETROS) {
    SENTENCIA(S)
}
```

Notemos la necesidad de abrir y cerrar llaves.
A esta pareja le llamamos un **bloque de código**,
el cual encapsulará líneas de código.

Por una cuestión de estilo,
cada vez que abramos un bloque de código
vamos a indentar un nivel más el código dentro de este
respecto a las llaves.

Un compilador de C++ va línea por línea a través del código,
comenzando desde la primera línea.

Por otro lado,
cuando corremos un programa que fue escrito en C++,
la ejecución siempre comienza en `main`.
Esta función se ejecuta automáticamente,
no tenemos que invocarla manualmente.

Un código que no tiene función `main` simplemente no compilará.

La sintaxis para retornar un valor de una función es la siguiente:

```cpp
return EXPRESION;
```

`EXPRESION` puede ser cualquier expresión que puede ser evaluada
con el tipo de retorno apropiado para nuestra función.

Recuerda que `main` siempre debería retorna 0 (cero)
tras la ejecución exitosa de un programa.
Podemos pensar esto como la manera en la cual `main` dice que no encontró ningún error.
Ese valor se envía de vuelta al sistema operativo y puede ser monitoreado e interpretado por otros programas.

A veces devolvemos valores no nulos desde `main` si algo sale mal
y queremos señalar a cualquiera que esté pendiente de nuestro programa que este no logró lo que queríamos.

## `std::cout`

`std::cout` es a lo que llamamos un **stream**.
Por defecto, actúa como una línea directa a nuestra consola.
Cualquier cosa que enviemos a él con el operador `<<` se imprime en la pantalla.
Hoy vimos dos cosas que podemos enviar a `std::cout`:
- Literal de caracteres: una cadena hardcodeada que aparece entre comillas como "Hola, mundo!".
- `std::endl`.

## `std::endl`

`std::endl` hace que una nueva línea se imprima en pantalla.
Sin esto, toda nuestra salida se imprime de corrido.

Por ejemplo, compilemos el siguiente código:

```cpp
#include <iostream>

int main(void) {
    // Note la ausencia de std::endl en las siguientes sentencias.
    std::cout << "Hola, mundo!";
    std::cout << "Manuel es genial, y tú también!";    
    return 0;
}
```

Veamos la salida tras ejecutar dicho programa:

```bash
manuel@thinkpad:~/UNMSM/ine018-unmsm$ ./a.out 
Hola, mundo!Manuel es genial, y tú también!manuel@thinkpad:~/UNMSM/ine018-unmsm$
```

Realicemos las correcciones respectivas al código anterior:

```cpp
#include <iostream>

int main(void) {
    std::cout << "Hola, mundo!" << std::endl;
    std::cout << "Manuel es genial, y tú también!" << std::endl;
    return 0;
}
```

Y nuestra salida será la siguiente:

```bash
manuel@thinkpad:~/UNMSM/ine018-unmsm$ ./a.out 
Hola, mundo!
Manuel es genial, y tú también!
manuel@thinkpad:~/UNMSM/ine018-unmsm$
```

## Comentarios

He utilizado comentarios durante toda la clase para poder.
Observamos que C++ soporta dos tipos de comentarios:
- C-style o multi-line:
Si tipeamos `/*`, luego cualquier cosa después de eso
es considerado un comentario hasta que por primera vez encontremos un `*/`.
- C++-style o single-line:
Si tipeamos `//`, luego cualquier cosa después de eso
es considerado un comentario hasta alcanzar el final de la línea.

Veamos un ejemplo:
```cpp
/*
 * Este es un comentario!
 * Esto también es parte del mismo comentario!
A pesar de que estas líneas no tengan un asterisco al inicio,
siguen siendo parte del comentario.
 * Cuando nos topemos con el final de la siguiente línea, el comentario terminará.
 */

#include <iostream>

int main(void) {
    std::cout << "Hola, mundo!" << std::endl;  // Este también es un comentario!
    return 0;
}
```

## Namespaces

> [!NOTE]
> No necesitamos estar familiarizados con cómo los namespaces funcionan en este curso.
> Mientras te sientas cómodo escribiendo `using namespace std;` en tus códigos, puedes continuar.

Cuando trabajamos en proyectos grandes,
solemos importar múltiples bibliotecas de diferentes fuentes.
De esta manera, un problema que surge es que ciertas bibliotecas
pueden tener funciones con los mismos nombres.

Por ejemplo,
una biblioteca de redes que establece conexiones con otras computadoras en una red
puede tener una función llamada `CrearConexion`,
y una biblioteca de bases de datos que establece conexión
con una base de datos persistida en disco puede tener también una función llamada `CrearConexion`.
Si nuestro proyecto depende de ambas bibliotecas
y llamamos `CrearConexion`, necesitamos una manera de determinar a cuál de las dos funciones nos referimos.

En C++ usamos namespaces para lidiar con este problema.
Un namespace es una colección nombrada de entidades.
Una biblioteca de redes podría orquestar un namespace `net`,
y una biblioteca de bases de dotas podría estructurar un namespace `db`.
Luego llamaríamos a estas funciones `CrearConexion` de la siguiente manera:

```cpp
net::CrearConexion();
db::CrearConexion();
```

Las funcionalidades de C++ que utilizaremos a lo largo del ciclo
están todas definidas en el namespace llamado `std`, el cual hace referencia a la palabra "standard".
Por ejemplo, `cout` y `endl` están en el namespace `std`.
Tener que tipear `std::` para cada función u objeto de estas bibliotecas estándares
serían una pérdida de tiempo, aparte de tener líneas de código bastante largas.

Así, utilizando la sentencia `using namespace std;` antes que todas nuestras definiciones
le estamos diciendo a C++ que busque en el namespace `std`
las componentes de las bibliotecas que hemos utilizado para construir nuestro programa
sin tener que tipear `std::` delante de cada una de ellas.

Este sería el nuevo código:

```cpp
#include <iostream>

using namespace std;

int main(void) {
    // Eliminamos ambas ocurrencias de std:: abajo.
    cout << "Hola, mundo!" << endl;
    return 0;
}
```

Si eliminamos tanto `using namespace std;` como `std::`, nuestro programa no compilará:

```bash
manuel@thinkpad:~/UNMSM/ine018-unmsm$ g++ clases/02/hola_mundo.cpp 
clases/02/hola_mundo.cpp: In function ‘int main()’:
clases/02/hola_mundo.cpp:4:5: error: ‘cout’ was not declared in this scope; did you mean ‘std::cout’?
    4 |     cout << "Hola, mundo!" << endl;
      |     ^~~~
      |     std::cout
In file included from clases/02/hola_mundo.cpp:1:
/usr/include/c++/11/iostream:61:18: note: ‘std::cout’ declared here
   61 |   extern ostream cout;          /// Linked to standard output
      |                  ^~~~
clases/02/hola_mundo.cpp:4:31: error: ‘endl’ was not declared in this scope; did you mean ‘std::endl’?
    4 |     cout << "Hola, mundo!" << endl;
      |                               ^~~~
      |                               std::endl
In file included from /usr/include/c++/11/iostream:39,
                 from clases/02/hola_mundo.cpp:1:
/usr/include/c++/11/ostream:684:5: note: ‘std::endl’ declared here
  684 |     endl(basic_ostream<_CharT, _Traits>& __os)
      |     ^~~~
```
