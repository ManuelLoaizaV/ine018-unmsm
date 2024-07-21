from PIL import Image, ImageFilter

imagen = Image.open('foto.jpg')

imagen_desenfocada = imagen.filter(ImageFilter.BLUR)

imagen_suavizado = imagen.filter(ImageFilter.SMOOTH)

imagen_desenfocada.save('desenfoque.jpg')
imagen_suavizado.save('suavizar.jpg')

imagen_desenfocada.show()
imagen_suavizado.show()