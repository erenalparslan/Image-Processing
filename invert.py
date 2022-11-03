from PIL import Image

import numpy as np

# Eren Alparslan



img = Image.open('C:/Users/Eren/Desktop/muhlog.jpg') #Invert yapılacak dosya uzantısı girilir


img_arry = np.array(img)        #Pikseller diziye aktarılır


I_max = 255


img_arry = I_max - img_arry             #Ters çevirme işlemi yapılıyor


inverted_img = Image.fromarray(img_arry)                        #Ters çevrilmiş img değişkene atılır


inverted_img.save('C:/Users/Eren/Desktop/polat1.jpg')           #Ters çevrilmiş img nin kaydedileceği uzantı girilir
