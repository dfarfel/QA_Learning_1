from openpyxl import Workbook
workbook=Workbook('C:/Users/dmoho/Desktop/TestCases.xlsx')
sheet=workbook.active
sheet['B1']="Varya"
sheet["A1"]="Koza"
sheet['C1']="Sranya"
workbook.save('C:/Users/dmoho/Desktop/Var.xlsx')
