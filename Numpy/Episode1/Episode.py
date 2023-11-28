import numpy as np
from PIL import Image, ImageOps
# считаем картинку в numpy array\
name = 'lunar01_raw.jpg'
img = Image.open(name)
data = np.array(img)
# коэффицент подберем в зависимлсти от картинки
im2 = ImageOps.autocontrast(img, cutoff=10)
im2.show()

im2.save('Lun1.jpg')