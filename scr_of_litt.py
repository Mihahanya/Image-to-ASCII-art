from PIL import Image
import numpy as np

img = Image.open("ltrs.png").convert('L')
pix = np.asarray(img)

ls = '1234567890~`!@#$%^&*()-=_+{}[]:";\'<>?,./\\|qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM '

f = open('stats.csv', 'w', encoding='utf8', newline='')

for i in range(len(ls)):
    x = i*8+4

    sgm = pix[44:60, x:x+8]
    Image.fromarray(sgm).save(f'imgs/{i}.png')

    f.write((f'"{ls[i]}"' if ls[i] != '"' else "'\"'") + ";" + str(sgm.sum()) + ";\n")
