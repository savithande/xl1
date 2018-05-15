import xlsxwriter

# creating a excel file or spreadsheet file

f = xlsxwriter.Workbook('sheet.xlsx')
worksheet = f.add_worksheet()   #adding sheet to the file


# set the headder formate is bold
bold=f.add_format({'bold': 1})


# creating a headder file
worksheet.write('A1','NAME',bold)
worksheet.write('B1','USN',bold)
worksheet.write('C1','PLACE',bold)
worksheet.write('D1','PhNo',bold)
repr(worksheet)

# setting of the length of each cell of the sheet
worksheet.set_column(0,0,13)
worksheet.set_column(1,1,13)
worksheet.set_column(2,2,13)
worksheet.set_column(3,3,13)
repr(worksheet)

#storing the data

# database of names
worksheet.write('A2','\n')
worksheet.write('A3','Adithya')
worksheet.write('A4','Adhithi')
worksheet.write('A5','Aradyha')

#database of id
worksheet.write('B2','\n')
worksheet.write('B3','4RA15Cs085')
worksheet.write('B4','3RA15CS008')
worksheet.write('B5','8RA15CS085')

#  place names storing
worksheet.write('C2', '\n')
worksheet.write('C3','HASSAN')
worksheet.write('C4','MYSORE')
worksheet.write('C5','BANGLORE')

# storing of the phno
worksheet.write('D2','\n')
worksheet.write('D3','9765465432')
worksheet.write('D4','1234567890')
worksheet.write('D5','8754632183')

#add background color to the headder file
bold.set_font_color('#FF00FF')
bold.set_bg_color('#FFFF00')



row=1
colum=0
f.close() #c losing the excel file