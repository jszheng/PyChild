from PIL import Image, ImageDraw, ImageFont
import os

im_board = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(im_board)
draw.text((20, 150), 'Hello', fill='black')
fontsFolder = 'FONT_FOLDER'
arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 32)
draw.text((100, 150), 'Howdy', fill='gray', font=arialFont)

im_board.save('text.png')



