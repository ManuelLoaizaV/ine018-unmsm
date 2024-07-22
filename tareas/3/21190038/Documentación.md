LIBRERÍA PILLOW

-Obtención

  Lo primero que se tiene que hacer es descargar la librería pillow mediante un comando en la consola.
  -> pip install pillow
  -> pip install --upgrade pillow (en caso ya este instalado y necesite actualizarse)
  Asimismo, tener en cuenta el directorio donde se va a instalar, ya que si se tiene dos versiones de python puede suceder que la instalación
  se haga en la versión incorrecta.

-Uso

  Lo primero que se tiene que hacer es importar la librería. Esta es un fork del PIL por lo tanto de este mismo se tiene que extraer.
  -> from PIL import Image
  Esta línea de código permitirá el uso de pillow para trabajar con imágenes. Además se pueden importar más opciones como:
  ->ImageChops, ImageFilter, ImageEnhance, entre otros
  
  A partir de aquí se procede a hacer uso de diferentes métodos para editar la imagen que van desde manipular los colores hasta aplicar efectos.
  -> Ejemplos: .crop, .resize, .rotate, .blend, ImageEnhance.Color, ImageEnhance.Color, ImageChops.difference, .filter(ImageFilter.UnsharpMask())
  -> Ejemplo del código:
  
    void = ImageEnhance.Contrast(meme).enhance(50) 
    grejo = ImageEnhance.Color(meme).enhance(0)
    voidgrejo_simple = Image.blend(void, grejo, 5)
    
    *La imagen tuvo cambios en el contraste y color por separado, para luego unirlos en una sola imagen

