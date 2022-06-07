import openpyxl 
from openpyxl.drawing.image import Image
  
wb = openpyxl.Workbook() 
  
sheet = wb.active
  
# Adding a row of data to the worksheet (used to 
# distinguish previous excel data from the image) 
sheet.append([10, 2010, "Geeks", 4, "life"]) 
  
# A wrapper over PIL.Image, used to provide image 
# inclusion properties to openpyxl library 
img = Image("geek.jpg")
  
# Adding the image to the worksheet 
# (with attributes like position) 
sheet.add_image(img, 'A2') 
  
# Saving the workbook created
wb.save('sample.xlsx')