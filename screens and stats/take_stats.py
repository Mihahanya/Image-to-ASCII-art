import numpy as np
from PIL import Image

text = '1234567890~`!@#$%^&*()-=_+{}[]:";\'<>?,./\|qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM '

print('Letter, Total brightness, Average brightness')

symb_dir = '../symbols_img/'
for i in range(95):
    p = np.asarray(Image.open(symb_dir + str(i) + '.png').convert('L'))
    print('\''+text[i]+'\',', str(p.sum())+',', p.sum() / p.shape[0] / p.shape[1])

