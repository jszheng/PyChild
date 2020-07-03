import zipfile, os


New_Zip = zipfile.ZipFile('composition.zip', 'w')
for folder, subfolder, files_list in os.walk('D:\\蔡静静\\Documents\\郑允哲作文\\陈老师作文'):
     for file in files_list:
        New_Zip.write(os.path.join(folder,file), compress_type=zipfile.ZIP_DEFLATED)


New_Zip.close()

