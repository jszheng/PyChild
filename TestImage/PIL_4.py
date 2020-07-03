from PIL import Image
from pylab import *


im = array(Image.open('empire.jpg'))
imshow(im)
print('please click 3 times')
x = ginput(3)
# print(type(x))
print('You clicked: ', x)
show()