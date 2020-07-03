from PIL import Image
import os
os.chdir('C:\\Users\\蔡静静\\Desktop')
HW_Im = Image.open('微信图片_20190921101903.jpg')

print(HW_Im.size)
width, height = HW_Im.size
print(width)
print(height)

print(HW_Im.filename)
print(HW_Im.format)
print(HW_Im.format_description)


# im = Image.new('RGBA', (100,200), 'purple')
# im.save('purpleImage.png')

# purpleIm = Image.open('purpleImage.png')
#
# croppedIm = purpleIm.crop((335, 345, 565, 560))
# croppedIm.save('cropped.png')


im_red = Image.new('RGBA', (100, 200), 'red')
im_red.save('redImage.png')

redIm = Image.open('redImage.png')
redcopyIm = redIm.copy()
redcopyIm.paste(redIm, (0,0))
redcopyIm.paste(redIm, (400,500))
redcopyIm.save('copyIm.png')


