from PIL import Image

imagen = Image.open('imagen.jpg')

imagen_gris = imagen.convert('L')

imagen_gris.save('imagen_gris.jpg')

imagen_gris.show()