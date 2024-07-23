# <p style="color: red;"> Procesamiento de imágenes con Pillow


## <p style="color: pink;"> Pillow

Pillow es una biblioteca adicional gratuita y de código abierto para Python que permite abrir, manipular y guardar varios formatos de imagen. Su repositorio se encuentra disponible en GitHub y proporciona acceso al código fuente y documentación para usarla. Puedes encontrarlo buscando "Pillow GitHub" o visitando directamente la página del proyecto.

![alt text](image.png)

## <p style="color: pink;"> Instalación de Pillow

La forma más común de instalar Pillow es utilizando pip, que es el administrador de paquetes de Python.
Aquí están los pasos generales:

1. Abrir una Terminal

        `pip install pillow`

2. Verificar la Instalación

        `pip show pillow`

## <p style="color: pink;"> Instalación de un entorno virtual

a. Crear un Entorno Virtual
Primero, asegúrate de tener virtualenv instalado. Si no lo tienes, puedes instalarlo utilizando pip:

1. Instalar el entorno

        `pip install virtualenv`


2. Activar el entorno

        `venv\Scripts\activate`

3. Instalar Pillow en el Entorno Virtual

        `venv\Scripts\activate`

## <p style="color: pink;"> Uso de Pillow

Una vez que Pillow esté instalado en tu entorno (global o virtual), puedes comenzar a utilizarlo en tu código Python.

Ejemplo:

```py

from PIL import Image
imagen= Image.open('imagen.jpg')
#Para voltear imágenes
imagen.transpose (Image.FLIP_LEFT_RIGHT).save('imagen_volteada.jpg')

#Para rotar imágenes
imagen.rotate(120).save('creador_rotado.jpg')

#Para recortar imágenes
imagen.crop((200,150,550,300)).save('creador_recortado.jpg')

#Para poner en gris imágenes
imagen_grises= imagen.convert('L')
imagen_grises.save('creador_grises.jpg')

#Y muchas funciones más....

```

