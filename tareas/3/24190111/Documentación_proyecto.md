## Libreria Pillow

- ### Descarga:
-Para esta parte tienes que crear tu entorno virtual con el destino en el archivo .py en el que estas trabajando, a partir de aca tienes que ir a la consola y escribir:
#### pip install Pillow
-Tienes que comprobar que este funcionando correctamente tomando un archivo de prueba.


- ### Importar: 
-Para utilizarlo tenemos que primero importarlo junto a las opciones que queramos usar en el caso, por ejemplo en el archivo de mi proyecto lo importe junto con:
#### from PIL import Image, ImageOps, ImageEnhance, ImageFilter
-Esto debido a que los usare en el codigo para modificar la imagen original.

- ### Ejecución:
Tomemos como ejemplo lo siguiente (parte del codigo fuente del proyecto):


new_image = ImageOps.grayscale(image)

    new_image.save("3_grises.jpg")


-En esta parte lo que quieres hacer es poner en escala de grises la imagen. Asi que primero tienes que modificar la imagen usando .grayscale(image) y luego guardar la modificacion en un nuevo archivo .jpg.
-Este proceso es analogo con las demas funcionalidades asi que depende del ejecutor que tanto cambios poder hacer en su imagen.
