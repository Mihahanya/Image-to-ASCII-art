import numpy as np
from PIL import Image
import sys, os
from numba import njit

from config import *

path_to_img = sys.argv[1] if len(sys.argv) != 1 else input('Path to image: ')
width = int(input('Width: '))

print('Processing...')

img = Image.open(path_to_img)
# Rescale image
img = img.resize((width*PW, int(img.size[1]/img.size[0]*width / symbol_aspect) * PH))
pix = np.asarray(img.convert('L'))

H, W = pix.shape[0], pix.shape[1]

# Getting symbol patterns
p_dir = 'blurred_symbols/'
patterns = []
for i in range(len(gradient)):
    p = np.asarray(Image.open(p_dir + str(i) + '.png').convert('L'))
    patterns.append(p)

p = np.array(patterns).flatten()
patterns = np.array(patterns, dtype='float64')

# Normalising symbols patterns
patterns -= np.full((PH, PW), min(p))
patterns *= np.full((PH, PW), 255/max(p))

@njit(fastmath=True)
def difference(a, b):
    d = 0
    for y in range(PH):
        for x in range(PW):
            #d += (a[y, x] - b[y, x])**2
            d += abs(a[y, x] - b[y, x])
    return d

@njit
def check_pattern(pat):
    # Finds the most similar symbol
    it = 0; min_d = 2560000
    for i in range(len(patterns)):
        d = difference(patterns[i]/255, pat/255)
        if d < min_d:
            min_d = d; it = i
    return it

f = open('res.txt', 'w')

# Traversing the image by sectors the size of the symbol image and writing result
for y in range(PH, H, PH):
    for x in range(PW, W, PW):
        part = pix[y-PH:y, x-PW:x]
        r = check_pattern(part)
        f.write(gradient[r])
    f.write('\n')
    print(round(y / H * 100, 1))

f.close()
