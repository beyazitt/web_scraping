from PIL import Image
from PIL import ImageFilter
image = Image.open("kuş.jpg")

#image.show()  #Resmi açtı.

#image.save("kuş2.jpg")  #Aynı resmi farklı isimle kaydetti.

#image.rotate(180).save("kuş3.jpg") #Resim 180 derece döndürüldü. ve kuş3.jpg olarak kaydetti

#image.convert(mode = "L").save("kuş5.jpg")  #Resmi siyah beyaz yaptı

değiştir = (960,600)

#image.thumbnail(değiştir)#Resmin boyutlarını değiştirir.

#image.save("kuş6.jpg")
image.filter(ImageFilter.GaussianBlur(10)).save("kuş7.jpg") #Resmi blurlaştırdı.

kırpılacak_alan = (340,0,950,600)
image2 = Image.open("atatürk.jpg")
image2.crop(kırpılacak_alan).save("kuş9.jpg")