from PIL import Image, ImageFilter , ImageEnhance

image_path = r"C:\Users\USER\Documents\GitHub\ine018-unmsm\tareas\3\24190098\imagen_original.jpg"
original_image = Image.open(image_path)

# Mostrar la imagen original
original_image.show()
# Convertir la imagen a escala de grises
grayscale_image = original_image.convert('L')
grayscale_image.show()
grayscale_image.save(r"C:\Users\USER\Documents\GitHub\ine018-unmsm\tareas\3\24190098\escala_de_grises.jpg")

# Aplicar un filtro de desenfoque gaussiano
blurred_image = original_image.filter(ImageFilter.GaussianBlur(radius=20))
blurred_image.show()
blurred_image.save(r"C:\Users\USER\Documents\GitHub\ine018-unmsm\tareas\3\24190098\desenfocado.jpg")

#  Rotar la imagen
rotated_image = original_image.rotate(180)
rotated_image.show()
rotated_image.save(r"C:\Users\USER\Documents\GitHub\ine018-unmsm\tareas\3\24190098\rotacion_180.jpg")

#  Invertir los colores
inverted_image = Image.eval(original_image, lambda x: 255 - x)
inverted_image.show()
inverted_image.save(r"C:\Users\USER\Documents\GitHub\ine018-unmsm\tareas\3\24190098\color_invertido.jpg")

# Aumentar brillo
enhancer = ImageEnhance.Brightness(original_image)
bright_image = enhancer.enhance(2)  # Aumenta el brillo en un 50%
bright_image.show()
bright_image.save(r"C:\Users\USER\Documents\GitHub\ine018-unmsm\tareas\3\24190098\brillante.jpg")