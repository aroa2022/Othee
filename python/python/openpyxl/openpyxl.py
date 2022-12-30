from openpyxl import Workbook

def write():
    wb = Workbook()
    ws = wb.active
    ws["B1"] = "=SUM(1, 1)"
    wb.save("formula.xlsx")

write()