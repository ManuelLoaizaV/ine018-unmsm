from PIL import Image,ImageFilter
#import numpy as np
imagen=Image.open('pato.jpeg')
Ima_find=imagen.filter(ImageFilter.FIND_EDGES)
Ima_find.show()