import win32com.client as win32
import os

def read_results_with_com(filepath):
    abs_path = os.path.abspath(filepath)
    excel = win32.DispatchEx('Excel.Application')
    excel.Visible = False
    try:
        wb = excel.Workbooks.Open(abs_path)
        sheet = wb.Sheets('全纸筒核价表')
        
        # Block 1 (Row 29 in openpyxl, corresponds to read line 32)
        total_1 = sheet.Range('P29').Value
        # Breakdown: C, E, G, J, M, O
        breakdown_1 = [sheet.Range(f"{c}29").Value for c in ['C', 'E', 'G', 'J', 'M', 'O']]
        
        # Block 2 (Row 57 in openpyxl, corresponds to read line 55)
        total_2 = sheet.Range('P57').Value
        # Breakdown: C, E, G, J, M, O
        breakdown_2 = [sheet.Range(f"{c}57").Value for c in ['C', 'E', 'G', 'J', 'M', 'O']]
        
        print("Block 1 (Roll Edge):")
        print(f"  Total Cost: {total_1}")
        print(f"  Breakdown (纸管+胶, 圆片+配件, 面纸, 纸箱费用, 加工工资, 运费):")
        print(f"    {breakdown_1}")
        
        print("\nBlock 2 (Tandigai):")
        print(f"  Total Cost: {total_2}")
        print(f"  Breakdown (纸管+胶, 圆片+配件, 面纸, 纸箱费用, 加工工资, 运费):")
        print(f"    {breakdown_2}")
        
        wb.Close(False)
    finally:
        excel.Quit()

if __name__ == "__main__":
    read_results_with_com('Quotation_9x15_10000.xlsx')
