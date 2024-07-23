from PIL import Image
imagen = Image.open('creador.jpg')
print(imagen.format)
print(imagen.size)
print(imagen.mode)