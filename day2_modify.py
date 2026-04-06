from openpyxl import load_workbook

#load existing workbook
wb= load_workbook("my_class.xlsx")

#Select sheet(by name)

sheet=wb["Student Data"]

#Read a cell value
print("Before change: ",sheet["A2"].value)

#Modify value
sheet["A2"]="Krishnansu"

#save changes
wb.save("my_class_updated.xlsx")
