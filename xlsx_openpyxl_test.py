import openpyxl, os

os.chdir('C:\\Users\\蔡静静\Desktop')
wb = openpyxl.load_workbook('python_example.xlsx')
print(type(wb))

# names = wb.get_sheet_names()
# print(names)

newnames = wb.sheetnames
print(newnames)

# sheet = wb.get_sheet_by_name('Sheet1')
# print(sheet)

sheet = wb['Sheet1']
print(sheet)
print(type(sheet))
print(sheet.title)

'''anothersheet = wb.get_active_sheet()
print(anothersheet)'''
#TODO
# search for the use of get_active_sheet


