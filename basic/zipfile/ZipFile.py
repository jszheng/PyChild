import zipfile, os
os.chdir('D:\\BaiduNetdiskDownload')
ZipRead = zipfile.ZipFile('近六年上海中考真题（word版）.zip')
# for filename in ZipRead.namelist():
#     print(filename)

getinto = ZipRead.getinfo('╜ⁿ┴∙─Ω╔╧║ú╓╨┐╝╒µ╠Γú¿word░µú⌐/└φ╗»/2012í½2016╔╧║ú╓╨┐╝╗»╤º╒µ╠Γ╛φ/2017─Ω╔╧║ú╩╨╗»╤º╓╨┐╝╒µ╠Γ.docx')
print(getinto.file_size)
print(getinto.compress_size)


#print('Compressed file is %sx smaller' % (round(getinto.file_size / getinto.compress_size, 2)))

print('Compressed file is %sx smaller' % (getinto.file_size / getinto.compress_size))
