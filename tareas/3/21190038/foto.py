#Los problemas para instalar pillow correctamente junto con darme cuenta que estaba instalado en otra version de python
#fue demasiado doloroso (ffs TT_TT)
import sys
print(sys.executable)

from PIL import Image, ImageEnhance, ImageChops, ImageFilter
foto = "meme.jpg"

with Image.open(foto) as meme:
    meme.load()


#Manipulando la imagen y sus medidas
cangrejo = meme.crop((100,200,1150,650))
cangrejo.save("cangrejo.jpg")
widegrejo = cangrejo.resize((cangrejo.width-50, cangrejo.height // 4))
widegrejo.save("widegrejo.jpg")

#Rotando la imagen
rotagrejo = cangrejo.rotate(80, expand = True, fillcolor = (255,0,0))
rotagrejo.save("rotagrejo.jpg")

#Manipulando las características de la imagen (color y contraste)
void = ImageEnhance.Contrast(meme).enhance(50) 
grejo = ImageEnhance.Color(meme).enhance(0)

#Fusionando las imágenes a partir de Image
voidgrejo_simple = Image.blend(void, grejo, 5)
voidgrejo_simple.save("voidgrejo_simple.jpg")

#Fusionando las imágenes a partir de ImageChops
voidgrejo_compuesto = ImageChops.difference(void,grejo)
voidgrejo_compuesto.save("voidgrejo_compuesto.jpg")

#Utilizando filtros
unkrabs = voidgrejo_compuesto.filter(ImageFilter.UnsharpMask(radius = 100))
unkrabs.save("unkrabs.jpg")

#Último cambio de color
void_meme = ImageEnhance.Color(unkrabs).enhance(0)
void_meme.save("void_meme.jpg")