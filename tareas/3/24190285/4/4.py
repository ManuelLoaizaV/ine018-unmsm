from PIL import Image,ImageFilter
#import numpy as np
imagen=Image.open('pato.jpeg')
Ima_boss=imagen.filter(ImageFilter.EMBOSS)
Ima_boss.show()