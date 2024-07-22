from PIL import Image, ImageFilter, ImageOps, ImageEnhance

def main():
    
    imagen = Image.open("HALA MADRID.jpg")
    
    #1.
    print("1. Edicion de iluminación en proceso.")
    new_imagen = ImageEnhance.Brightness(imagen).enhance(2.3)
    new_imagen.save("EdicionDeIluminacion.jpg")
    print("1.1. Edicion de iluminación realizada con éxito.")
    
    #2.
    print("2. Edicion de saturación en proceso.")
    new_imagen = ImageEnhance.Color(imagen).enhance(2)
    new_imagen.save("EdicionDeSaturación.jpg")
    print("2.1. Edicion de saturación realizada con éxito.")
   
    #3.
    print("3. Edicion de filtro en proceso.")
    new_imagen = imagen.filter(ImageFilter.SMOOTH)
    new_imagen.save("EdicionDeFiltro.jpg")
    print("3.1. Edicion de filtro realizada con éxito.")

    #4.
    print("4. Edicion de tono de grises en proceso.")
    new_imagen = ImageOps.grayscale(imagen)
    new_imagen.save("EdicionTonoDeGrises.jpg")
    print("4.1. Edicion de tono de grises realizada con éxito.")

    #5.
    print("5. Edicion de desenfoque en proceso.")
    new_imagen = imagen.filter(ImageFilter.GaussianBlur(5))
    new_imagen.save("EdicionDeDesenfoque.jpg")
    print("5.1. Edicion de desenfoque realizada con éxito.")

    #6.
    print("6. Edicion de tamaño en proceso.")
    new_imagen = imagen.resize((640, 480))
    new_imagen.save("EdiciónDeTamaño.jpg")
    print("6.1. Edicion de tamaño realizada con éxito.")

    print('Finalización de la fotografía procesada exitosamente.')

if __name__ == "__main__":
    main()
