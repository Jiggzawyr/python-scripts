# Python program to read an excel file 
  
# import openpyxl module 
import openpyxl 
  
# Give the location of the file 
path = "gfg.xlsx"
  
# To open the workbook 
# workbook object is created 
wb_obj = openpyxl.load_workbook(path) 
  
# Get workbook active sheet object 
# from the active attribute 
sheet_obj = wb_obj.active 
  
# Cell object is created by using 
# sheet object's cell() method. 
cell_obj = sheet_obj['A1': 'B6']
  
# Print value of cell object 
# using the value attribute 
for cell1, cell2 in cell_obj:
    print(cell1.value, cell2.value)