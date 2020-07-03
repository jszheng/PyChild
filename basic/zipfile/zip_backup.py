import os, zipfile


def backupzip(folder):
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zipfilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipfilename):
            break
        number = number + 1
    print('')
    print('Done')
    backupzip('C:\\Python\\PyChild')
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s......' % foldername)
