# Configuración del entorno de desarrollo

Tarea creada el 28 de mayo del 2024.

Entrega: 11 de junio del 2024, 23:59pm.

![Python environment](https://imgs.xkcd.com/comics/python_environment.png)

Uno de los sentimientos más amargos como ingeniero
es no poder trabajar en lo que te propusiste hacer.
Pasaste todo el día configurando el repositorio en tu entorno local.
¿Qué es peor?
Es la primera semana en tu nuevo trabajo, proyecto o curso,
y estuviste buscando errores que te salían en el terminal
o ejecutando comandos aleatorios de internet.

## ¿Qué hay que hacer?

Esta tarea consta de tres partes que te ayudarán a configurar correctamente
tu entorno de desarrollo para el curso.

### Configuración de Visual Studio Code

#### Windows

- Primera parte: Pasos para instalar VSCode
    1. Ir a [este enlace](https://code.visualstudio.com/docs/setup/windows)
    y descargar VSCode para Windows.
    2. Seguir las instrucciones en dicha página bajo la sección **Instalación**.
- Segunda parte: Instalar un compilador para C++
    1. Seguir las instrucciones de [este enlace](https://code.visualstudio.com/docs/cpp/config-mingw).
    En particular, las instrucciones bajo **Installing the MinGW-w64 toolchain**.
    2. Finalmente, puedes verificar que todo funcionó ejecutando el comando
    ```shell
    g++ --version
    ```

> [!TIP]
> Si prefieres una guía visual,
> te recomendamos ver el [video tutorial oficial de Microsoft](https://www.youtube.com/watch?v=oC69vlWofJQ)
> para la instalación del compilador en Windows.
> Recuerda que puedes activar los subtítulos en el video de YouTube si el inglés se te dificulta.

#### Mac

- Primera parte: Pasos para instalar VSCode
    1. Ir a [este enlace](https://code.visualstudio.com/docs/setup/mac)
    y descargar VSCode para Mac.
    2. Seguir las instrucciones en dicha página bajo la sección **Instalación**.

- Segunda parte: Instalar un compilador para C++
    1. Seguir las instrucciones de [este tutorial](https://cs.millersville.edu/~gzoppetti/InstallingGccMac.html).
    2. Verificar que tenemos Homebrew instalado corriendo el siguiente comando:
    ```shell
    brew --version
    ```
    Si obtienes algo como
    ```shell
    Homebrew 4.2.16
    ```
    saltemos al paso 4.
    En otro caso, prosigamos con el paso 3.
    3. Correr el comando
    ```shell
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```
    para instalar Homebrew, un gestor de paquetes.
    4. Correr el comando
    ```shell
    brew install gcc
    ```
    que instalará el compilador.

> [!NOTE]
> Si completa la tarea en alguna distribución de Linux,
> ya sea mediante una instalación dual-boot,
> una máquina virtual o WSL,
> recibirán todo el puntaje de participación del curso;
> es decir, 5% de la nota final.

### Prueba de concepto

Implemente, compile y ejecute satisfactoriamente un programar desde Visual Studio Code.

![Configuración exitosa de Manuel](/tareas/1/successful_setup.png)

Los siguientes tres archivos formarán parte de la entrega:

- El código fuente del programa implementado.
- Una captura de pantalla de la ejecución exitosa.
- Un archivo en el cual explica qué dificultades tuvo o qué aprendió en el proceso de completar la tarea.

### ¿Qué es Git y cómo se usa?

La razón para utilizar un árbol Git es que
se vayan familiarizando con las principales herramientas de colaboración
para el desarrollo de software que encontrarán.
Podrán usar Git para colaborar en cada uno de los equipos,
y podrán usar el flujo definido por la plataforma GitHub
para realizar las entregas una vez que terminen con cada tarea.

Emplearemos en particular la forma de trabajo impulsada por el sitio GitHub,
muy popular en comunidades de desarrollo de software.
¡Espero que todos aprendan algo más acerca de cómo aprovecharlo!

Siendo un firme entusiasta del software libre,
me resulta importante iniciarlos en el uso de esta importante
herramienta de desarrollo colaborativo,
así como su interacción en tanto red social.

#### ¿Cómo lo usaremos en el curso?

1. Todos los alumnos deben tener una cuenta en GitHub.
2. Siempre que el profesor anuncie una tarea en clase, creará un subdirectorio dentro del área correspondiente.
3. Todos los alumnos harán un *fork* del árbol y desarrollarán su tarea en su *fork*.
    - Si la tarea es en equipos, basta con que uno de ustedes lo haga pero
    no olviden documentar claramente quiénes son los integrantes del equipo.
4. Para todas las entregas, usa el esquema de nombre estandarizado que presentaremos a continuación:

```
[tipo_entrega]/[numero]/[código]/
```

- Esto es, por ejemplo, si voy a entregar la primera tarea, lo hago en el directorio `tareas/1/20185048`.
- Si estamos resolviendo algo en equipo, el directorio se crea con los códigos de los integrantes
en orden lexicográfico, separado por guiones.
Si la segunda tarea la hago con Carlos Leal, el directorio de entrega sería
`tareas/2/20185048-24190292`.

5. Registren el desarrollo de su proyecto.
En todas las entregas no triviales
se calificará el que haya un avance visible reflejado en varios *commits*.

> [!NOTE]
> Importa que los mensajes en la bitácora
> resuman el trabajo realizado paso a paso.

6. Cuando estén contentos con el desarrollo, creen un *pull request*.
Eso, y únicamente eso, contará como entrega de una tarea.

Un par de tutoriales para aprender a usar Git y GitHub:
- [git - la guía sencilla](https://rogerdudler.github.io/git-guide/index.es.html)
- [GitHub Desktop](https://desktop.github.com/)
