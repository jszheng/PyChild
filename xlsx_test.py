import openpyxl, os, pprint
Path = 'C:\\Users\\蔡静静\Desktop'
os.chdir(Path)
Filename = 'xlsx_test.xlsx'
wb = openpyxl.load_workbook(Filename)
sheet = wb['Sheet1']
countryData = {}
for row in range(2,sheet.max_row + 1):
    State = sheet['B' + str(row)].value
    country = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    countryData.setdefault(State, {})
    countryData[State].setdefault(country, {'tracks': 0, 'pop': 0})
    countryData[State][country]['tracks'] += 1
    countryData[State][country]['pop'] += int(pop)

print('Writing results...')
result = open('census2010.py', 'w')
result.write('all data' + pprint.pformat(countryData))
result.close()
print('Done')

