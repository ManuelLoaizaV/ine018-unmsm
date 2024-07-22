from PIL import Image ,ImageDraw , ImageFont
Loto1 = Image.open("/home/gattiko/Escritorio/Perla/myenv/new carpet/Fotos/4.jpg")
Loto2 = Image.open("/home/gattiko/Escritorio/Perla/myenv/new carpet/Fotos/1.jpg")
Loto3 = Image.open("/home/gattiko/Escritorio/Perla/myenv/new carpet/Fotos/5.jpg")


# Intento crear un tamaño adecuado para cada imagen
Anc_Ind = 200
Alt_Ind = 200   
loto1 = Loto1.resize((Anc_Ind, Alt_Ind), Image.LANCZOS)
loto2 = Loto2.resize((Anc_Ind, Alt_Ind), Image.LANCZOS)
loto3 = Loto3.resize((Anc_Ind, Alt_Ind), Image.LANCZOS)

Anc_Tot = Anc_Ind * 3
Alto_Tot = Alt_Ind

collage = Image.new("RGB", (Anc_Tot , Alto_Tot), "white") 
#aqui me confundi un poco porque tenia que estar tanteando al principio 
# pero luego me guie de videos para colocar la posicion.
collage.paste(loto1 , (0, 0))
collage.paste(loto2, (200, 0))
collage.paste(loto3, (400, 0))

collage.save("Collage1.jpg")
collage.show()

# otro aqui , unos mas completo :o

Anc_Ind = 300 
Alt_Ind = 300 
LotoA = Image.open("/home/gattiko/Escritorio/Perla/myenv/new carpet/Fotos/A.jpg").resize((Anc_Ind, Alt_Ind), Image.LANCZOS)
LotoB = Image.open("/home/gattiko/Escritorio/Perla/myenv/new carpet/Fotos/B.jpg").resize((Anc_Ind, Alt_Ind), Image.LANCZOS)
LotoC = Image.open("/home/gattiko/Escritorio/Perla/myenv/new carpet/Fotos/C.jpg").resize((Anc_Ind, Alt_Ind), Image.LANCZOS)
LotoD = Image.open("/home/gattiko/Escritorio/Perla/myenv/new carpet/Fotos/D.jpg").resize((Anc_Ind, Alt_Ind), Image.LANCZOS)
LotoE = Image.open("/home/gattiko/Escritorio/Perla/myenv/new carpet/Fotos/E.jpg").resize((Anc_Ind, Alt_Ind), Image.LANCZOS)
LotoF= Image.open("/home/gattiko/Escritorio/Perla/myenv/new carpet/Fotos/F.jpg").resize((Anc_Ind, Alt_Ind), Image.LANCZOS)
LotoG = Image.open("/home/gattiko/Escritorio/Perla/myenv/new carpet/Fotos/G.jpg").resize((Anc_Ind, Alt_Ind), Image.LANCZOS)
LotoH= Image.open("/home/gattiko/Escritorio/Perla/myenv/new carpet/Fotos/h.jpg").resize((Anc_Ind, Alt_Ind), Image.LANCZOS)
#Redimensionamos el tamaño que usaremos
Anc_Tot = Anc_Ind * 3
Alto_Tot = Alt_Ind *3
#colocamos una nueva imagen, el tipo de color , el tamaño y el color de fondo 
collage = Image.new("RGB", (Anc_Tot , Alto_Tot), "Black") 
Escri = ImageDraw.Draw(collage)
Fuente = ImageFont.truetype("DejaVuSans-Bold.ttf", 70)
Escri.text((300 ,300), "Colores", (255, 255, 255), font=Fuente)
Escri.text((330,380), "   de  ", (255, 255, 255), font=Fuente)
Escri.text((320,460), " Lotos ", (255, 255, 255), font=Fuente)
#Raqui nos guiamos por las coordenadas , asi como (X,Y)
collage.paste(LotoA , (0, 0))
collage.paste(LotoB, (Anc_Ind, 0))
collage.paste(LotoC, (Anc_Ind * 2, 0))
collage.paste(LotoD , (0, Alt_Ind))
collage.paste(LotoH ,(Anc_Ind * 2, Alt_Ind))
collage.paste(LotoF ,(Anc_Ind * 2 ,Alt_Ind * 2))
collage.paste(LotoE ,(0, Alt_Ind * 2))
collage.paste(LotoG ,(Anc_Ind, Alt_Ind * 2))


collage.save("Collage2.jpg")
collage.show()