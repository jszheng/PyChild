import os, re
for foldername, subfolder, files in os.walk('D:\\蔡静静\\文档'):
    searchfile = re.search('\.docx')
    print(searchfile)