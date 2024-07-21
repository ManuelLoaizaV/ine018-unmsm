# <p style="color: blue;"> Web Scraping con Selenium

A continuación explicaré resumidamente en qué consiste Selenium y sus aplicaciones.

## <p style="color: cyan;"> Selenium

Selenium contiene herramientas de automatización de pruebas para aplicaciones web. Ello nos permite mejorar la eficiencia y la interacción entre el desarrollador y la página web a usar. 

Entre algunas aplicaciones en las que se usa Selenium son las pruebas automatizadas, el desarrollo web y la depuración, y el scraping de datos, que es exactamente de lo que se tratará este proyecto.

## <p style="color: cyan;"> Instalaciones correspondientes
1. Primero, nos aseguramos de instalar esta biblioteca que será fundamental en el proyecto con:

        `pip install selenium`

2. Luego, instalaremos el Chrome Driver en su página, y esto nos ayudará a la automatización de la prueba en el navegador de Chrome.

## <p style="color: cyan;"> Funciones usadas
<p style="color: pink;"> 1. By: 

Se usa para encontrar elementos de una página web, con diferentes formas de búsqueda, como el nombre, el ID y el xpath.

<p style="color: pink;"> 2. WebDriverWait: 

Se utiliza para darle tiempo explícitamente a la carga de la página para asegurar que todos los elementos estén listos para ser usados en el scraping.

<p style="color: pink;"> 2. ExpectedConditions: 

Contiene condiciones que ya han sido predefinidas para poder usarlas y que el código espere hasta que se cumpla esta condición antes de seguir con el script de prueba.

## <p style="color: cyan;"> Ejecución del código
1. Importamos todas las librerías necesarias para los bloques de código siguientes.

2. Usaremos el driver de Chrome para la apertura de la página de prueba. Luego, abriremos la página de donde se accederá a las carreras.

3. Creamos una lista de datos vacía y esperando a que cargue todos los datos que solicitamos, se agregan estos a la lista.

4. Debido a que no todas las 67 carreras se encuentran en la misma página, codearemos el funcionamiento de un click a la siguiente página y repetiremos el proceso.

5. Terminamos imprimiendo la lista ya hecha con los títulos de las carreras obtenidas de la página.


<p style="color: gray;"> Y esto es todo :DDD