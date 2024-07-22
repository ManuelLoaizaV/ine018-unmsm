from PIL import Image,ImageFilter
#import numpy as np
imagen=Image.open('pato.jpeg')
ancho,alto=imagen.size
Ba_R, Ba_V, Ba_A=imagen.split()
Ima_V=Image.new(mode='L',size=(ancho,alto),color='black')
Ima_V=Image.merge('RGB',(Ima_V,Ba_V,Ima_V))
Ima_V.show()