from PIL import Image, ImageEnhance, ImageFilter, ImageChops

imagen_original = Image.open('rectora.jpg')
brillo = ImageEnhance.Brightness(imagen_original)
imagen_cambiada = brillo.enhance(2.0)
imagen_cambiada.save('rectora_brillosa.jpg')

# imagen_desenfocada.show()
def traduccion(ruta_imagen, desp_x, desp_y):
    imagen = Image.open(ruta_imagen)
    imagen_traducida = ImageChops.offset(imagen, desp_x, desp_y)
    imagen_traducida.save('rectora_desenfocada.jpg')
def escalar_imagen(ruta_imagen, escala):
    imagen = Image.open(ruta_imagen)

    ancho_nuevo = int(imagen.width * escala)
    alto_nuevo = int(imagen.height * escala)
    imagen_escalada = imagen.resize((ancho_nuevo, alto_nuevo))
    imagen_escalada.save('rectora_escalada.png')
    print('Tamaño original: ')
    print(imagen.size)
    print('Tamaño escalado: ')
    print(imagen_escalada.size)
def rotar_imagen(ruta_imagen, angulo):
    imagen = Image.open(ruta_imagen)
    imagen_rotada = imagen.rotate(angulo)
    imagen_rotada.save('rectora_rotada.png')
traduccion('rectora.jpg', 100, 100)
escalar_imagen('rectora.jpg', 3)
rotar_imagen('rectora.jpg', 120)

