import win32com.client as win32
import os

def debug_excel(filepath):
    abs_path = os.path.abspath(filepath)
    excel = win32.DispatchEx('Excel.Application')
    excel.Visible = False
    try:
        wb = excel.Workbooks.Open(abs_path)
        for s in wb.Sheets:
            print(f"Sheet name: '{s.Name}'")
        
        sheet = wb.Sheets('全纸筒核价表')
        print(f"A9: {sheet.Range('A9').Value}")
        print(f"B9: {sheet.Range('B9').Value}")
        print(f"C9: {sheet.Range('C9').Value}")
        print(f"E9: {sheet.Range('E9').Value}")
        
        print(f"H32: {sheet.Range('H32').Value}")
        print(f"H32 formula: {sheet.Range('H32').Formula}")
        
        wb.Close(False)
    finally:
        excel.Quit()

if __name__ == "__main__":
    debug_excel('Quotation_9x15_10000.xlsx')
