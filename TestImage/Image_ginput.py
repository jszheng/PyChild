from PIL import Image
from pylab import *
import os

os.chdir('C:\\Users\\蔡静静\\Desktop')

im = array(Image.open('微信图片_20190921101850.jpg'))
imshow(im)
print('Please click 3 points')

x = ginput(3)
print('you click:', x)
show()