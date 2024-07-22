from PIL import Image
imagen= Image.open('creador.jpg')
imagen.transpose (Image.FLIP_LEFT_RIGHT).save('creador_volteado.jpg')
imagen.rotate(120).save('creador_rotado.jpg')
imagen.crop((200,150,550,300)).save('creador_recortado.jpg')
imagen_grises= imagen.convert('L')
imagen_grises.save('creador_grises.jpg')
from PIL import ImageFilter
imagen_filtrada = imagen.filter(ImageFilter.BLUR)
imagen_filtrada.save('creador_filtrado.jpg')
