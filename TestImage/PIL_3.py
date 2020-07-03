from PIL import Image
from pylab import *
im = array(Image.open('empire.jpg').convert('L'))

figure()

gray()

contour(im, origin='image')
axis('equal')
axis('off')


# next
figure()
hist(im.flatten(), 128)
show()