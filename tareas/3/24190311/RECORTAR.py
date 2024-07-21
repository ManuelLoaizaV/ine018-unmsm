from PIL import Image

imagen = Image.open('recortar.jpg')

region_a_recortar = (50, 50, 600, 500)  

imagen_recortada = imagen.crop(region_a_recortar)

imagen_recortada.save('recortado.jpg')

imagen.show()

imagen_recortada.show()