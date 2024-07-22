# Pillow
La biblioteca de imágenes de Python agrega capacidades de procesamiento de imágenes a su intérprete de Python.

Esta biblioteca proporciona un amplio soporte de formatos de archivo, una representación interna eficiente y capacidades de procesamiento de imágenes bastante potentes.

La biblioteca de imágenes principal está diseñada para un acceso rápido a los datos almacenados en unos pocos formatos de píxeles básicos. Debería proporcionar una base sólida para una herramienta de procesamiento de imágenes general.


## Instalación
Para instalar la librería Pillow en el sistema diríjase a `Simbolo del sistema` y ejecute el siguiente comando:
```python
>pip install pillow
```
Se comprueba que está funcionando correctamente tomando un archivo de prueba.

## Importación 
Para ejecutar y utilizar los comandos de la librería Pillow se debe importar desde VSC con el siguiente código:
```python
from PIL import Image, ImageFilter, ImageFont, ImageFont...
```
La cantidad de bibliotecas a importar dependerá de los comandos que se vayan a utilizar.

## Ejecución
Para conocer mejor los comandos y herramientas de esta librería en [este enlace](https://pillow.readthedocs.io/en/stable/index.html) se muestra a gran detalle su funcionamiento.
1. Para cargar una imagen desde un archivo, utilice la función `open()`  en el módulo `Image`:
```python
from PIL import Image
img = Image.open("nombre.jpg")
```
2. La biblioteca de imágenes de Python proporciona diferentes filtros, para poder ejecutarlos se debe importar el módulo `ImageFilter`:
```python
from PIL import Image, ImageFilter
```
Algunos ejemplos serían:

   a) Para desenfocar se utiliza el comando `BoxBlur`, adicionalmente se coloca la `cantidad de desenfoque` que se quiere entre paréntesis "()".
   ```python
   img=img.filter(ImageFilter.BoxBlur(''))
   ```
   b) Para rotar se utiliza el comando `rotate`, adicionalmente se coloca la herramienta `angle` la cual definirá el `ángulo de rotación` que se quiere:
   ```python
   img=img.rotate(angle='')
   ```
   c) Para mezclar imágenes, primero cargue dos imágenes, las cuales deben ser del mismo tamaño.
   ```python
   img1=Image.open("imagen1.jpg")
   img2=Image.open("imagen2.jpg")
   ```
   Seguidamente se utiliza el comando `blend`, adicionalmente se coloca la herramienta `alpha` la cual definirá la proporción con la que las imágenes se puedan mezclar:
   ```python
   img=Image.blend(img1,img2,alpha=0.5)
   ```
3. Una vez haya terminado de editar su imagen, utilice la función `show` para mostrar la imagen ya editada, y luego ejecutar su código.
```python
img.show()
```
