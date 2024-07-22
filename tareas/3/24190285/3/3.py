from PIL import Image,ImageFilter
#import numpy as np
imagen=Image.open('pato.jpeg')
Ima_edge=imagen.filter(ImageFilter.EDGE_ENHANCE)
Ima_edge.show()