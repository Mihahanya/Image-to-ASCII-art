import numpy as np
from PIL import Image
import sys, os
from numba import njit

from config import *

path_to_img = sys.argv[1] if len(sys.argv) != 1 else input('Path to image: ')
width = int(input('Width: '))

print('Processing...')

img = Image.open(path_to_img)
# Rescale image for symbols patterns
img = img.resize((width*PW, int(img.size[1]/img.size[0] * width / symbol_aspect) * PH)) 
pix = np.asarray(img.convert('L'))

H, W = pix.shape[0], pix.shape[1]

# Getting tone of every symbol by average brightness
symb_dir = 'symbols_img/'
tones = []
for i in range(95):
    p = np.asarray(Image.open(symb_dir + str(i) + '.png').convert('L'))
    tones.append(p.sum() / PW / PH)

# Normalising symbols tones
tones -= min(tones)
tones *= 255/max(tones)
tones = np.array(tones)

@njit
def check_pattern(pat):
    # Search for the nearest symbol by its tone
    ps = pat.sum() / len(pat) / len(pat[0])
    it = 0; min_d = 256
    for i in range(len(tones)):
        d = abs(tones[i] - ps)
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
