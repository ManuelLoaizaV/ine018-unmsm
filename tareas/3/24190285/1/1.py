from PIL import Image,ImageFilter
import numpy as np
imagen=Image.open('pato.jpeg')
Ima_blur=imagen.filter(ImageFilter.BLUR)
Ima_blur.show()
