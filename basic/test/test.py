import openpyxl
from openpyxl import Workbook


wbFormulas = openpyxl.load_workbook('create_xlsx.xlsx', data_only=True)
sheet_2 = wbFormulas['Sheet1']
print(sheet_2['A3'].value)

