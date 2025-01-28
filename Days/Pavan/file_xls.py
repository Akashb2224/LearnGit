import openpyxl
import openpyxl.workbook

# Create a new Excel workbook
wb = openpyxl.Workbook()

# Select the active worksheet
ws = wb.active

# Write data to the worksheet
ws.append(["This is my first line"])
ws.append(["This is my second line"])
ws.append(["This is my third line"])

# Save the workbook to a file
wb.save(r'C:\Users\akash\OneDrive\Desktop\file.xlsx')



