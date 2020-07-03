import os, zipfile


os.chdir('D:\\Python\\PyChild')
examplezip = zipfile.ZipFile()
examplezip.extractall()
examplezip.close()
