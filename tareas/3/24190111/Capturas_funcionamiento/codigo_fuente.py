from PIL import Image, ImageOps, ImageEnhance, ImageFilter

def main():
    # Aca se carga la imagen profe
    image = Image.open("imagen.jpg")

    # Rotamos la imagen
    new_image = image.rotate(45)
    new_image.save("1_rotar_45.jpg")

    # Le ponemos un filtro a la imagen
    new_image = image.filter(ImageFilter.FIND_EDGES)
    new_image.save("2_filtro.jpg")

    # Lo volvemos gris
    new_image = ImageOps.grayscale(image)
    new_image.save("3_grises.jpg")

    # más brillo
    new_image = ImageEnhance.Brightness(image).enhance(1.5)
    new_image.save("4_brillo.jpg")

    # más saturación
    new_image = ImageEnhance.Color(image).enhance(2)
    new_image.save("5_saturacion.jpg")

    # DESENFOQUE
    new_image = image.filter(ImageFilter.GaussianBlur(5))
    new_image.save("6_desenfoque.jpg")

    # TAMAÑO
    new_image = image.resize((640, 480))
    new_image.save("7_tamano.jpg")

if __name__ == "__main__":
    main()
