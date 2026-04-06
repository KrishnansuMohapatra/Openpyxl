from openpyxl import Workbook
#create a new workbook
wb=Workbook()
#active that sheet
sheet=wb.active

#Rename the sheet
sheet.title="Student Data"

#write data in to shell
sheet["A1"]="Name"
sheet["B1"]="Age"
sheet["C1"]="Marks"

sheet["A2"]="Krishna"
sheet["B2"]=23
sheet["C2"]=78

sheet["A3"]="Subashis"
sheet["B3"]=21
sheet["C3"]=89

sheet["A4"]="Ravi"
sheet["B4"]=24
sheet["C4"]=85
#Save the workbook
wb.save("my_class.xlsx")

print("Excel file created successfully")