from PIL import Image, ImageFilter
img=Image.open("lana.jpg")

img_1=img.rotate(angle=60,fillcolor="white",expand=True)
img_1.show()

img_2=img.crop(box=(20,20,200,200))
img_2.show()

img_3=img.filter(ImageFilter.BoxBlur(10))
img_3.show()

img_4=img.filter(ImageFilter.CONTOUR)
img_4.show()

img_5=img.filter(ImageFilter.EDGE_ENHANCE)
img_5.show()

img_6=img.filter(ImageFilter.SMOOTH)
img_6.show()

img1=Image.open("lana1.jpg")
img2=Image.open("lana2.jpg")
img_7=Image.blend(img1,img2,alpha=0.5)
img_7.show()

img_1.save("lana_1.jpg")
img_2.save("lana_2.jpg")
img_3.save("lana_3.jpg")
img_4.save("lana_4.jpg")
img_5.save("lana_5.jpg")
img_6.save("lana_6.jpg")
img_7.save("lana_7.jpg")
