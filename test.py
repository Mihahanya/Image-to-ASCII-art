from PIL import Image, ImageChops, ImageStat
import numpy as np

a = np.asarray(Image.open('imgs/0.png').convert('L'))
b = np.asarray(Image.open('imgs/0.png').convert('L'))
#b = Image.open('51.png').convert('L')

def difference(a, b):
    d = 0
    for y in range(16):
        for x in range(8):
            a[y, x] += 0.1
            b[y, x] += 0.1
            d += (abs(a[y, x]**2 - b[y, x]**2))**0.5
    return d/16/8/255

print(difference(a, b))
