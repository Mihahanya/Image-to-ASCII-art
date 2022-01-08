from PIL import Image, ImageFilter
import numpy as np

img = Image.open("src/ltrs.png").convert('L')
pix = np.asarray(img)

ls = '1234567890~`!@#$%^&*()-=_+{}[]:";\'<>?,./\\|qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM '

f = open('stats.csv', 'w', encoding='utf8', newline='')

for i in range(len(ls)):
    x = i*8+4

    sgm = pix[44:60, x:x+8]
    imgl = Image.fromarray(sgm)
    #imgl.save(f's/{i}.png')

    imgl = imgl.filter(ImageFilter.GaussianBlur(radius=1))
    imgl.save(f'sb/{i}.png')

    #f.write((f'"{ls[i]}"' if ls[i] != '"' else "'\"'") + ";" + str(sgm.sum()) + ";\n")

f.close()
