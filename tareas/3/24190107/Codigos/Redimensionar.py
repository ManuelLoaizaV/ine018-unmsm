from PIL import Image

Imag =  Image.open("/home/gattiko/Escritorio/Perla/myenv/new carpet/Fotos/Loto.jpg")
#  Intento redimensionar las imagenes
Tamaño = Imag.resize((600, 1200))
Tamaño.save("Imagen_Redimensionada1.jpg")
Tamaño.show()
# y usamos la funcion LANCZOS para redimensionar de una mejor manera 
# pero no logre ver tanta diferencia.
Tamaño= Imag.resize((600, 1200), Image.LANCZOS)
Tamaño.save("Imagen_Redimensionada2.jpg")
Tamaño.show()
#Recortare las imagenes 
Recortado = Imag.crop((100, 100, 400, 400))
Recortado.save("Imagen_Recortada1.jpg")
Recortado.show()
#Rotare las imagenes de 45 y 90 
Rotacion = Imag.rotate(45)
Rotacion.save("Imagen_Rotada1.jpg")
Rotacion.show()
Rotacion = Imag.rotate(90)
Rotacion.save("Imagen_Rotada2.jpg")
Rotacion.show()

# voltear las imagenes de lados.
Volteado_D= Imag.transpose(Image.FLIP_LEFT_RIGHT)
Volteado_D.save("Imagen_Volteado1.jpg")
Volteado_D.show()

# voltear las imagenes de Oarte superior e inferior.
Volteado_L = Imag.transpose(Image.FLIP_TOP_BOTTOM)
Volteado_L.save("Imagen_Volteado2.jpg")
Volteado_L.show()

#  wow una nueva forma de editar las imagenes,rotamos las i
Multiples = Imag.rotate(45,expand = 1, fillcolor="Red")
Multiples.save("Imagen_Multiple.jpg")
Multiples.show()

Multiples1 = Imag.rotate(150,expand = 1, fillcolor="Green")
Multiples1.save("Imagen_Multiple.jpg")
Multiples1.show()