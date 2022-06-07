from openpyxl import Workbook
  
# Call a Workbook() function of openpyxl  
# to create a new blank Workbook object 
workbook = Workbook()
  
# Anytime you modify the Workbook object 
# or its sheets and cells, the spreadsheet 
# file will not be saved until you call 
# the save() workbook method. 
workbook.save(filename="sample.xlsx")