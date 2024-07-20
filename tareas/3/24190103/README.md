## Funcionamiento del proyecto
El proyecto consiste en scrapear las carreras que aparecen en la lista de carreras de pregrado de la UNMSM. El termino scrapear significa, en palabras sencillas, extraer información de una página web, por ejemplo, si quisieras buscar una carrera dentro de las tantas que hay, podrías almacenarlas todas en un txt y luego aplicando ciertos filtros, reducir tu enorme lista a una que contenga solo carreras de ingeniería, o relacionadas al área de salud. Afortunadamente la página de San Marcos ya cuenta con la opción de filtrar, pero en un caso hipotético donde no lo haya, o la información sea demasiada y quieras aplicar filtros más rigurosos, Web Scraping sería una muy buena alternativa. A continuación, explico el funcionamiento de mi código.

En la parte superior se colocan, similar a c++, las bibliotecas que se usarán y que permitirán el uso de ciertos comandos. La biblioteca principal que uso en este proyecto es Selenium.

```py

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager #pip install webdriver-manager

```

La __primera línea__, me permite usar el comando `sleep(t)` donde t es el tiempo en que mi código hace una pausa para que la pagina termine de cargarse y los siguientes comandos puedan funcionar correctamente.

La __segunda línea__, importa webdriver, que es la herramienta que permite interactuar con el navegador.

La __tercera línea__, me permite usar el comando By con el uso más adelante para buscar elementos en específico, ya sea por su clase, ID, XPATH, entre otros.

La __cuarta y quinta línea__, son las más importantes porque con ellas voy a designar a Chrome como el navegador que usare para realizar mi proyecto. Para ello uso las siguiente líneas de código:

```py

driver = webdriver.Chrome (
  service = Service(ChromeDriverManager().install())
)

```
Con ChromeDriverManager ya no tengo la necesidad de instalar manualmente el webdriver específico para mi versión de Chrome, porque ahora lo hace de forma automática. Cabe mencionar que use Chrome porque pienso yo que al ser el navegador más usado debe ser el que tenga mejor compatibilidad y presente menos fallas durante la ejecución, desde mi punto de vista.

Las líneas de arriba sirvieron para configurar el entorno de trabajo a usar, las siguientes líneas son, por así decirlo, las que realmente lo pondrán en marcha.

Empiezo usando `driver.get` para especificar la url que se abrirá en mi navegador.

```py

driver.get('https://unmsm.edu.pe/formacion-academica/carreras-de-pregrado')

```

Luego uso el comando `sleep` para darle tiempo a mi página a que vaya cargando antes de realizar los próximos comandos

```py

sleep(3)

carreras_list = []

```

También de paso creo una lista en la cual almacenaré las carreras que extraiga más adelante.

Usando el método de búsqueda por XPATH ubico a las etiquetas p con la clase 'mb-13px color-rojo-sm'. Dicha clase la obtuve inspeccionando en la página de San Marcos y noté que ellas contenían el nombre de las carreras de pregrado. Al ser varios elementos con la misma clase uso el comando `driver.find_elements`, notese que está en plural. Entonces guardo todas ellas en mi variable 'carreras', y con ayuda de un for almaceno una a una dentro mi lista creada anteriormente.

```py

  carreras = driver.find_elements(By.XPATH, '//p[@class="mb-13px color-rojo-sm"]')
  for carrera in carreras:
      carreras_list.append(carrera.text)
  sleep(2)

```

Uso sleep para esperar un poco antes de iniciar mi siguiente comando.

En vista que es una lista algo extensa, las carreras no fueron colocadas en una página, sino que la dividieron en 9 páginas, por lo que si quería seguir obteniendo las demás necesitaba moverme a la siguiente página. Entonces nuevamente use el comando `driver.find_element` para buscar el botón que me lleva a la siguiente página (resulto que no fue un botón, sino un hipervínculo), para ello nuevamente una inspección de la página y ubicar al responsable de dirigirme a la siguiente página.

![navigator](/tareas/3/24190103/Proyect_web_scraping/images/navigator.png)

```py

  next = driver.find_element(By.XPATH, '//a[@class="d-inline-block sig-paginator"]')
  next.click()
  sleep(1)

```

Lo nuevo aquí fue que no solo era necesario ubicar al elemento, sino que también debía realizar un click para pasar de página, entonces una vez ubicado y guardado en mi variable `next`, uso el comando `next.click()` para realizar dicha acción.
En esta parte invertí regular tiempo porque no lograba hacer que ocurra, tengo costumbre de no borrar líneas de código fallidos porque puedo revisarlos más adelante y recordar en que me equivoque, por eso en mi código original se puede apreciar algunos de los intentos que me tomo y muchos otros que borre que no aparecen en mi versión final. 

![errores](/tareas/3/24190103/Proyect_web_scraping/images/errores.png)

Ya casi por terminar, al notar que la acción iba a repetirse al menos 9 veces por la cantidad de páginas que tiene, decidí colocarlos en un bucle.

```py

for i in range(9):
    
    ...[código]...

```

Por último, uso `.join()` para guardar los elementos de mi lista en strings y separarlos en cada línea los cuales guardo en mi variable 'final' y los exporto en un txt.

```py

sleep(1)
final = '\n'.join(carreras_list)

with open('output.txt', 'w') as file:
   file.write(final)

```

Solo basta con tener instalado Google Chrome y correr el archivo python para que el resto se realice de manera automática.
