from PIL import Image
from PIL import ImageFilter

imagen = Image.open("erizo_original.jpg")

# Editar y visualizar el resultado final.
imagen_1 = imagen.filter(ImageFilter.BLUR)
imagen_1.show()

imagen_2 = imagen.filter(ImageFilter.CONTOUR)
imagen_2.show()

imagen_3 = imagen.filter(ImageFilter.EDGE_ENHANCE)
imagen_3.show()

dimensiones = (100, 100)
imagen_4 = imagen.resize(dimensiones)
imagen_4.show()

# Guardar los archivos de las imágenes modificadas en jpg.
imagen_1.save("erizo_1.jpg")
imagen_2.save("erizo_2.jpg")
imagen_3.save("erizo_3.jpg")
imagen_4.save("erizo_4.jpg")