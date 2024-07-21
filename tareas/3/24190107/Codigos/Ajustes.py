from PIL import Image , ImageEnhance ,ImageDraw, ImageFont
Imag =  Image.open("/home/gattiko/Escritorio/Perla/myenv/new carpet/Fotos/Loto.jpg")

#este codigo lo vi en videos, para introducirme a la libreria pillow.
#show sirve para abrir la imagen
Imag.show()

#cambiamos el brillo
Ajus = ImageEnhance.Brightness(Imag)
Imag_bri = Ajus.enhance(1.5)
Imag_bri.save("imagen_bri.jpg")
Imag_bri.show()

#cambiamos el constraste
Ajus = ImageEnhance.Contrast(Imag)
Imag_Cont = Ajus.enhance(1.5)
Imag_Cont.save("imagen_cont.jpg")
Imag_Cont.show()

#cambiamos el nitidez
Ajus = ImageEnhance.Sharpness(Imag)
Imag_Sharp =Ajus.enhance(2.0)
Imag_Sharp.save("imagen_sharp.jpg")
Imag_Sharp.show()

#Escribir en la imagen.
Escri = ImageDraw.Draw(Imag)
Fuente = ImageFont.truetype("DejaVuSans.ttf", 60)

Escri.text((100, 100), "Loto!", (0, 0, 0), font=Fuente)
Imag.save("imagen_texto.jpg")
Imag.show()

#Desenfoque
Imag = Image.open("/home/gattiko/Escritorio/Perla/myenv/new carpet/Fotos/Loto.jpg").convert("RGBA")
alpha = Imag.split()[3]
#reducir la transpariencia
alpha = alpha.point(lambda p: p * 0.5) 
Imag.putalpha(alpha)
Imag.save("imagen_transparente.png")
Imag.show()
#no es como esperaba

#aqui cambiamos el formato de la imagen
Imag = Image.open("/home/gattiko/Escritorio/Perla/myenv/new carpet/Fotos/Loto.jpg")
Imag.save("imagen_convertida.png")
