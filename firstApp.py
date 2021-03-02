from PIL import Image
import sys
from numpy import *

im1 = Image.open('mario.jpg')
im2 = Image.open('rocket.jpg')
resize = (400, 400)
resizedImage = im1.resize(resize, Image.ANTIALIAS)
resizedImage2 = im2.resize(resize, Image.ANTIALIAS)

imarr = asarray(resizedImage)
imarr2 = asarray(resizedImage2)

print(imarr.shape)
print(imarr2.shape)

imarra = 256-(imarr + 300)

print(imarr.shape)

newImage = Image.fromarray(imarra)

newImage.show()
