from PIL import Image,ImageFilter
import numpy as np
imagen=Image.open('pato.jpeg')
ancho,alto=imagen.size
Ba_R, Ba_V, Ba_A=imagen.split()
#ancho,alto=imagen.size()
Ima_R=Image.new(mode='L',size=(ancho,alto),color='black')
Ima_R=Image.merge('RGB',(Ba_R,Ima_R,Ima_R))
Ima_R.show()

