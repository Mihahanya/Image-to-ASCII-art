import numpy as np
from PIL import Image
import sys, os
from numba import njit

path_to_img = sys.argv[1] if len(sys.argv) != 1 else input('Path to image: ')
width = int(input('Width: '))

print('Processing...')

pw = 8
ph = 16

img = Image.open(path_to_img)
img = img.resize((width*pw, int(img.size[1]/img.size[0]*width)//2 * ph))
pix = np.asarray(img.convert('L'))

h = pix.shape[0]
w = pix.shape[1]

patterns = []
p_dir = 'imgs/'
for root, dirs, files in os.walk(p_dir):
    for filename in files:
        p = np.asarray(Image.open(p_dir + filename).convert('L'))
        patterns.append(p)
patterns = np.array(patterns)

gradient = '1234567890~`!@#$%^&*()-=_+{}[]:";\'<>?,./\\|qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM '

#@njit(fastmath=True)
def difference(a, b):
    d = 0
    for y in range(16):
        for x in range(8):
            a[y, x] += 0.1
            b[y, x] += 0.1
            d += (abs(a[y, x] ** 2 - b[y, x] ** 2)) ** 0.5
    return d / 16 / 8 / 255

#@njit
def check_pattern(pat):
    it = 0
    min_d = 123456789
    for i in range(len(patterns)):
        d = difference(patterns[i], pat)
        if d < min_d:
            min_d = d
            it = i
    return it

f = open('res.txt', 'w')

for y in range(ph, h, ph):
    for x in range(pw, w, pw):
        part = pix[y-ph:y, x-pw:x]
        r = check_pattern(part)
        f.write(gradient[r])
    f.write('\n')
    print(round(y / h * 100, 1))

f.close()
