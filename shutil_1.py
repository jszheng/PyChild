import os
for filename in os.listdir():
    if filename.endswith('.docx'):
        os.unlink(filename)
#        print(filename)


#betterchoice
import send2trash
baconfile = open('baconfile.txt', 'w')
baconfile.write('Bacon is not vegetable')
baconfile.close()
send2trash.send2trash('bacon.txt')