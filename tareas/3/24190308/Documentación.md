
DOCUMENTACIÓN DEL FUNCIONAMIENTO
=============
## PILLOW
Pillow es una biblioteca de Python que se utiliza para trabajar con imágenes. Esta herramienta ofrece un gran número de funcionalidades.
### Funcionalidades

1. **Abrir y guardar imágenes**:  Pillow puede abrir imágenes en muchos formatos como JPEG, PNG, BMP, GIF, TIFF, entre otros, y también puede guardarlas en estos formatos.
2. **Manipulación de imágenes:**  Incluye funciones para redimensionar, recortar, rotar, y aplicar filtros y efectos a las imágenes.
3. **Dibujo en imágenes:** Permite dibujar formas, texto y otros gráficos en las imágenes.
4. **Procesamiento de píxeles:** Puedes acceder y modificar los datos de los píxeles directamente.
5. **Conversión de modos de imagen:** Soporta la conversión entre diferentes modos de imagen, como RGB, Grayscale, y otros.

### Instalación
Para usar Pillow, como yo lo hice en Google colab el primer paso para la instación fue colocar el siguiente comando:
`!pip Install Pillow`

 Después de esto, como Google colab no tiene acceso directo a los archivos de mi computadora, tuve que subir el archivo ejecutando el siguiente código:
`from google.colab import files uploaded = files.upload()`

 Ya realizados los procedimientos anteriores, para realizar los cambios a mi imagen, tuve que importar de la biblioteca Pillow las siguientes herramientas:
`from PIL import Image, ImageFilter, ImageEnhance, ImageOps`
- **Image:** Es la clase principal de Pillow para manejar imágenes. Permite abrir, crear, manipular y guardar imágenes en diversos formatos.
- **ImageFilter:** Tiene una gran variedad de filtros predeterminados.
- **ImageEnhance:** Se utiliza para ajustar y mejorar la calidad visual de las imágenes mediante la modificación de diferentes parámetros, como el brillo, el contraste, la saturación y la nitidez. 
- **ImageOps:** Contiene funciones para realizar operaciones en imágenes, como la inversión de colores, la corrección de gamma, la adición de bordes, y más.

### Ejecución
Después de haber subido la imagen a google collab, utilicé el siguiente código para definir concretamente cual sería el archivo con el que trabajaría utilizando: `ruta_imagen = list(uploaded.keys())[0]` y  `imagen = Image.open(ruta_imagen)`. Posteriormente, utilicé las herramientas mencionadas referentes a la biblioteca Pillow. Por ejemplo, para rotar mi imagen 135 grados, coloqué: `imagen_rotada = imagen.rotate(135)`, luego guardé la imagen `imagen_rotada.save('imagen_rotada.jpg')` y finalmente añadí un mensaje para saber que le proceso había sido realizado con éxito y se había guardado con el nombre que especifiqué, empleando: `print("La imagen ha sido rotada satisfactoriamente y guardada como: 'imagen_rotada.jpg'")`.
Realicé un procedimiento similar para todas las modifaciones que quería realizarle a mi imagen y así cultimar con el proceso ejecutando la función principal.