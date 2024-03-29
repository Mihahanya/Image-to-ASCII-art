import numpy as np
from PIL import Image
import sys

from config import *

path_to_img = sys.argv[1] if len(sys.argv) != 1 else input('Path to image: ')
width = int(input('Width: '))

print('Processing...')

img = Image.open(path_to_img)
img = img.resize(( width, int(img.size[1]/img.size[0]*width / symbol_aspect) ))
pix = np.asarray(img.convert('L'))

#gradient = ' .:!/r(l1Z4H9W8$@'
#gradient = ' `:,!*zTY]kGm%NQ@'
gradient = ' `.\'*+xoOX#0@'
#gradient = ' ░▒▓█'
l = len(gradient)-1
f = open('res.txt', 'w', encoding="utf-8")

for y in range(img.size[1]):
    for x in range(img.size[0]):
        p = pix[y, x]/255
        f.write(gradient[l-round(p*l)])
    f.write('\n')

f.close()
