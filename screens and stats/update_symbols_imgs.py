from PIL import Image, ImageFilter
import numpy as np

direct = '../blurred_symbols'

img = Image.open("symbols_img.png").convert('L')
pix = np.asarray(img)

symbols = '1234567890~`!@#$%^&*()-=_+{}[]:";\'<>?,./\\|qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM '

f = open('stats.csv', 'w', encoding='utf8', newline='')

for i in range(len(symbols)):
    x = i*8+4

    segment = pix[44:60, x:x+8]
    imgl = Image.fromarray(segment)

    # Blur images
    imgl = imgl.filter(ImageFilter.GaussianBlur(radius=1.3))

    imgl.save(f'{direct}/{i}.png')

    # Write stats to csv file
    #f.write((f'"{symbols[i]}"' if symbols[i] != '"' else "'\"'") + ";" + str(segment.sum()) + ";\n")

f.close()
