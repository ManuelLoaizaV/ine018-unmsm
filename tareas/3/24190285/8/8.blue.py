from PIL import Image,ImageFilter
#import numpy as np
imagen=Image.open('pato.jpeg')
ancho,alto=imagen.size
Ba_R, Ba_V, Ba_A=imagen.split()
Ima_A=Image.new(mode='L',size=(ancho,alto),color='black')
Ima_A=Image.merge('RGB',(Ima_A,Ima_A,Ba_A))
Ima_A.show()