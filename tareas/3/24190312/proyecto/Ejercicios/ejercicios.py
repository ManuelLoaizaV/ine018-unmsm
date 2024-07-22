from PIL import Image
imagen =Image.open("creador.jpg")
imagen =imagen.convert("RGB")
imagen.save('creador_cambiado.png')
imagen.thumbnail((200,200))
imagen.save('creador_miniatura.jpg') 
imagen =Image.open('creador_miniatura.jpg')
print(imagen.size)