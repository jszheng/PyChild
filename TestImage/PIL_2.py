from PIL import Image
from pylab import *
import os

os.chdir('C:\\Users\\蔡静静\\Desktop')
im = array(Image.open('empire.jpg'))

imshow(im)

x = [100, 200, 300, 400]
y = [50, 150, 250, 350]

plot(x, y, '.')

plot(x[:2], y[:2])

title('Plotting: "empire.jpg"')
show()
