
# Procesamiento de imágenes con Pillow
Antes de empezar definamos que es Pillow.
Es una biblioteca de imágenes de Python el cual agrega capacidades de procesamiento de imágenes a su intérprete de Python.

Mi tarea consistia en hacer uso de esta biblioteca para explorar y probar las diferentes funcionalidades que ofrece.

## Instalacion

Para instalar Pillow ,en cualquier sistema operativo.

🔗 Link [![Pillow](https://pillow.readthedocs.io/en/stable/installation/basic-installation.html)](https://pillow.readthedocs.io/en/stable/index.html)




## Bibliotecas
Para empezar, PIL (Python Imaging Library) y Pillow  se refieren a la misma funcionalidad basica para trabajar con imágenes en Python pero Pillow es la versión más moderna y mantenida activamente del proyecto original PIL
Algunas Bibliotecas que usamos ya que son son parte del paquete PIL en Pillow.

```py
  from PIL import Image 
  import ImageEnhance ,ImageDraw
  import ImageFont ,ImageFilter
```
Se utiliza para traer Bibliotecas a nuestro archivo.
```py 
import Image
```
Se utiliza para abrir, crear y manipular imagenes.
```py 
import ImageEnhance
```
Proporciona herramientas para mejorar o ajustar diferentes aspectos de la imagen, como brillo, contraste, color y nitidez.
```py  
import ImageDraw
```
Se utiliza para dibujar en imágenes, como agregar texto, formas y líneas.

```py  
import ImageFont
```
Se usa para gestionar las fuentes tipográficas cuando se dibuja texto en una imagen. Puedes cargar fuentes TrueType y especificar el tamaño del texto.

```py 
import ImageFilter 
```
Proporciona varios filtros predefinidos para aplicar a las imágenes, como desenfoque, nitidez y contornos.


# Funcionamiento
Para comenzar inicializamos llamando a la biblioteca Pillow, y seleccionamos un imagen.
```py
  from PIL import Image 
  Imag =  Image.open("/home/gattiko/Escritorio/Perla/myenv/new carpet/Fotos/Loto.jpg")
```
`Image.open()` Podemos seleccionar la ubicacion de una imagen.
###  Ajustes.py
En este archivo usamos diferentes bibliotecas.

 ```py
  from PIL import Image , ImageEnhance ,ImageDraw, ImageFont
  
```
**En el ejemplo de `ImageEnhance.Sharpness(image)`**
```py
Ajus = ImageEnhance.Sharpness(Imag)
Imag_Sharp =Ajus.enhance(2.0)
Imag_Sharp.save("imagen_sharp.jpg")
Imag_Sharp.show()
```
Usamos algunas funciones para cambiar el brillo, contraste y la nitidez``ImageEnhance.Brightness(image)`` ``ImageEnhance.Contrast(image)``
``ImageEnhance.Sharpness(image)``
El mismo principio se aplica a los ajustes de brillo, contraste y nitidez.

Controlamos la nitidez:

 >Donde **1.0  = la imagen normal**
 y "x" un numero racional.
>
 >**x < 1.0** Disminuye la nitidez.
>
 >**x > 1.0**  Incrementa la nitidez.

**En el ejemplo de `ImageDraw.Draw()`** 
```py
Escri = ImageDraw.Draw(Imag)
Fuente = ImageFont.truetype("DejaVuSans.ttf", 60)
Escri.text((100, 100), "Loto!", (0, 0, 0), font=Fuente)
Imag.save("imagen_texto.jpg")
Imag.show()
```
Podemos escribir en la imagen junto a 
`ImageFont.truetype()`para llamar la fuente y el tamaño
`ImageDraw.text(position, text, fill, font)`.
De ahi implementamos este codigo para añadir la posicion dentro de la imagen, el texto que escribire, y la fuente ya cargada o llamada.

Creamos un objeto de dibujo *Escri* para dibujar en *Imag*.
El texto "Loto!" se dibuja en la posición (100, 100), en  color negro, utilizando la fuente "DejaVuSans" de tamaño 60.
Como ultimo paso usamos la funcion `Imag.show()` para mostrarnos la imagen.


###  Redimensionar.py 
 ```py
  from PIL import Image 
```
**En el ejemplo de `Image.resize(size, resample)`**
```py
Tamaño = Imag.resize((600, 1200))
Tamaño.save("Imagen_Redimensionada1.jpg")
Tamaño.show()
```
Redimensiona la imagen *Imag* a un tamaño de 600 píxeles de ancho y 1200 píxeles de alto, Guarda la imagen redimensionada en un archivo llamado *Imagen_Redimensionada1.jpg* `Image.save()` y la muestra usando`Tamaño.show()`.

**En el ejemplo de `Image.rotate(angle, expand, fillcolor)`**
```py 
Multiples = Imag.rotate(45,expand = 1, fillcolor="Red")
Multiples.save("Imagen_Multiple.jpg")
Multiples.show()
```
Rota la imagen *Imag* en 45 grados, ajusta el lienzo para que la imagen completa sea visible , rellena las áreas vacías con color rojo, la guarda en un archivo llamado *Imagen_Multiple.jpg*  `Multiples.save()` y la muestra `Multiples.show()`.


### Imagen_Filtros.py
 ```py
  from PIL import Image ,ImageFilter
```
**En el ejemplo de `Imag.split()`**
```py
Ba_R, Ba_V, Ba_A = Imag.split()
Ancho, Alto = Imag.size
Imag_negro = Image.new(mode="L", size=(Ancho, Alto), color="Black")

Imag_R = Image.merge("RGB", (Ba_R, Imag_negro, Imag_negro))
Imag_R.show()
Imag_R.save("Imagen_Roja.jpg")

Imag_V = Image.merge("RGB", (Imag_negro, Ba_V, Imag_negro))
Imag_V.show()
Imag_V.save("imagen_Verde.jpg")

Imag_A = Image.merge("RGB", (Imag_negro, Imag_negro, Ba_A))
Imag_A.show()
Imag_A.save("Imagen_Azul.jpg")
```

Divide la imagen `Imag.split()` en sus componentes de color: Rojo (R), Verde (V) y Azul (A). 
Las bandas de color se asignan a *Ba_R, Ba_V y Ba_A* respectivamente.
`Imag.size` Obtiene las dimensiones de la imagen Imag, 
`Image.new` y crea una nueva imagen negra con el modo "L" (escala de grises).

`Image.merge` Fusiona las bandas de color para crear una nueva imagen en la que solo el canal rojo está presente, mientras que los canales verde y azul son negros. Guarda esta imagen como *Imagen_Roja.jpg* `Imag_R.save()` y la muestra `Imag_R.show()`y el mismo procedimiento con los demas colores.

### Collage.py
```py
  from PIL import Image ,ImageDraw , ImageFont
```

**En el primer collage**,carga tres imagenes,creamos una nueva imagen blanca de 600x200 píxeles para el collage `Image.new`.
Pegamos las tres imagenes redimensionadas en el collage en las posiciones especificadas usando coordenadas dentro 600x200 `collage.paste`,guardamos el collage como *Collage1.jpg* `Image.save()` y lo muestra `Image.show()`.

**En el segundo collage**,Carga Y redimensiona ocho imágenes a
300x300 píxeles usando el filtro 
Image.LANCZOS`Image.resize()`.
Creamos una nueva imagen negra de 900x900 para el collage `Image.new`,añadimos texto blanco al collage usando una fuente TrueType `ImageDraw.text`,pegamos las ocho imagenes redimensionadas en las posiciones especificas `collage.paste` y guardamos *Collage2.jpg*`Image.save()`  y lo muestra `Image.show()`.



## Funciones Utilizadas

`Image.open`Abre una imagen desde el archivo especificado.

`Image.new(mode, size, color)` Crea una nueva imagen vacía con el modo, tamaño y color de fondo especificados.

`Image.paste(im, box)` Pega una imagen (im) en la posición especificada por box (una tupla de coordenadas).

`Image.filter(filter)`  Aplica un filtro a la imagen

`Image.merge(mode, bands)` Combina varias bandas individuales en una sola imagen.

`Image.show()` Muestra la imagen.

`ImageEnhance.Brightness(image)`Ajusta el brillo de la imagen especificada.

`Image.save(filepath)` Guarda la imagen en el archivo especificado.

`ImageEnhance.Contrast(image)` Ajusta el contraste de la imagen especificada.

`ImageEnhance.Sharpness(image)` Ajusta la nitidez de la imagen especificada.

`ImageDraw.Draw(image)` Permite dibujar en la imagen especificada.

`ImageFont.truetype(font, size)` Carga una fuente desde un archivo con el tamaño especificado.

`Image.split()` Divide la imagen en sus bandas individuales

`ImageDraw.text(position, text, fill, font)` Dibuja texto en la imagen en la posición especificada con el color de relleno y la fuente dados.

`Image.point(function)`  Aplica una función a cada punto en la banda de la imagen.

`Image.putalpha(band)`  Reemplaza el canal alfa de la imagen con la banda dada.

`Image.rotate(angle, expand, fillcolor)` Rota la imagen en el ángulo especificado,expandir el tamaño de la imagen,llena las áreas vacías resultantes de la rotacion.

`Image.transpose(method)` Aplica una transposición a la imagen

`Image.resize(size, resample)`  Cambia el tamaño de la imagen al tamaño especificado.


