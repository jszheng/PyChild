from PIL import Image
import os

os.chdir('C:\\Users\\蔡静静\\Desktop')
pil_open = Image.open('empire.jpg')
pil_im = Image.open('empire.jpg').convert('L')
# pil_im_open = Image.open('empire.jpg')

pil_im.save('empire.jpg')





