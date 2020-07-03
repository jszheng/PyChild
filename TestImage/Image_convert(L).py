from PIL import Image
from numpy import *
from pylab import *
import os

os.chdir('C:\\Users\\蔡静静\\Desktop')
im = Image.open('微信图片_20191128195049.jpg').convert('L')


im.save('微信图片_20191128195049.jpg')
