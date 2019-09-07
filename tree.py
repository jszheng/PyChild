import os
for foldername, subfolders, filenames in os.walk('D:\\Python'):
    print('The current folder is: ' + foldername + '\n')

    for subfolder in subfolders:
        print('Subfolder of ' + foldername + ' is: ' + subfolder)

    for filename in filenames:
         print('Files inside ' + foldername + ' is: ' + filename)


         print('')


