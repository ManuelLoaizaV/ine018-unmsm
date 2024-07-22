from PIL import Image,ImageFilter
#import numpy as np
imagen=Image.open('pato.jpeg')
Ima_sharp=imagen.filter(ImageFilter.SMOOTH)
Ima_sharp.show()