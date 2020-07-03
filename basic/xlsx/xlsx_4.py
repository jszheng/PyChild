import openpyxl, os
filename = 'C:\\Users\\蔡静静\Desktop'
os.chdir(filename)
file = 'python_example.xlsx'
wb = openpyxl.load_workbook(file)

sheet = wb.active
'''title = sheet.title
print(title)
sheet.title = 'Spam Bacon Eggs Sheet'
newtitle = wb.sheetnames
print(newtitle)'''


wb.save('py_example.xlsx')


