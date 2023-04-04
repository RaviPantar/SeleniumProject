import xlrd

workbook = xlrd.open_workbook('Datafile.xls')
sheet = workbook.sheet_by_index(0)

rowCount = sheet.nrows
colCount = sheet.ncols
print(rowCount)
print(colCount)

for cur_row in range(1, rowCount):
    user_name = sheet.cell_value(cur_row, 0)
    password = sheet.cell_value(cur_row, 1)
    print(user_name + " " + password)

