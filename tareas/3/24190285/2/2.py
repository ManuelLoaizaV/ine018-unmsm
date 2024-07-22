from PIL import Image,ImageFilter
import numpy as np
imagen=Image.open('pato.jpeg')
Ima_cont=imagen.filter(ImageFilter.CONTOUR)
Ima_cont.show()
