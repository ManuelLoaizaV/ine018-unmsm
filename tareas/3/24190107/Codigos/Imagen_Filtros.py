from PIL import Image , ImageFilter
Imag =  Image.open("/home/gattiko/Escritorio/Perla/myenv/new carpet/Fotos/Loto.jpg")
#unos filtros para las imagenes .

#Convertiremos la imagen que tenemos en blanco y negro o  escala de grises.
Imag_Gris =Imag.convert("L")
Imag_Gris.save("Imagen_gris.jpg")
Imag_Gris.show() 

#filtro desenfoque
Imag_blur = Imag.filter(ImageFilter.BLUR)
Imag_blur.save("Imagen_Blur.jpg")
Imag_blur.show()


# Aplicar el filtro de contorno
Imag_contour = Imag.filter(ImageFilter.CONTOUR)
Imag_contour.save("Imagen_Contour.jpg")
Imag_contour.show()


# Aplicar el filtro de mejora de bordes
Imag_edge = Imag.filter(ImageFilter.EDGE_ENHANCE)
Imag_edge.save("Imagen_Edge.jpg")
Imag_edge.show()

# Aplicar el filtro de encontrar bordes
Imag_find_edges = Imag.filter(ImageFilter.FIND_EDGES)
Imag_find_edges.save("Imagen_Find_Edges.jpg")
Imag_find_edges.show()

#Aplica un filtro de agudización.
Imag_sharpen = Imag.filter(ImageFilter.SHARPEN)
Imag_sharpen.save("Imagen_Sharpen.jpg")
Imag_sharpen.show()

# Aplicar el filtro de detalle
Imag_detail = Imag.filter(ImageFilter.DETAIL)
Imag_detail.save("Imagen_Detail.jpg")
Imag_detail.show()

#Aplicamos los colores de rgb , dividiendolos en bandas de color(Rojo, Verde y Azul)
#Para crear imagenes que resalten ese banda de color
Ba_R, Ba_V, Ba_A = Imag.split()
Ancho, Alto = Imag.size
Imag_negro = Image.new(mode="L", size=(Ancho, Alto), color="Black")
#split divide en bandas de colores R,V,A.
Imag_R = Image.merge("RGB", (Ba_R, Imag_negro, Imag_negro))
Imag_R.show()
Imag_R.save("Imagen_Roja.jpg")
#Las bandas verde y azul son reemplazados por el color negro.
Imag_V = Image.merge("RGB", (Imag_negro, Ba_V, Imag_negro))
Imag_V.show()
Imag_V.save("imagen_Verde.jpg")

#Crear una nueva imagen usando el canal azul y las imágenes negras para los canales rojo y verde
Imag_A = Image.merge("RGB", (Imag_negro, Imag_negro, Ba_A))
Imag_A.show()
Imag_A.save("Imagen_Azul.jpg")

