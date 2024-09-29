import openpyxl
import pprint

wb = openpyxl.load_workbook('nombres.xlsx')
sheet = wb.active

names = [cell.value for cell in next(sheet.columns)]
# or
# names = [cell.value for cell in sheet['A']]

# Create a single list
single_list = names

# Create a string representation of the list
output = f'names = {pprint.pformat(single_list)}'

# Write the output to a file
with open('output.py', 'w') as f:
    f.write(output)

print('List saved to output.py')