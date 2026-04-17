import win32com.client
import os
import sys

def update_excel():
    excel = win32com.client.Dispatch("Excel.Application")
    excel.Visible = False
    excel.DisplayAlerts = False
    
    source_file = r"E:\123\常用文件\纸筒计算改进中版001(1) .xlsx"
    target_file = os.path.abspath("Quotation_10x30_5000_Revised.xlsx")
    
    try:
        wb = excel.Workbooks.Open(source_file)
        
        # List all sheet names to verify
        sheet_names = [sh.Name for sh in wb.Worksheets]
        print(f"Sheet names: {sheet_names}")
        
        ws = None
        for sh in wb.Worksheets:
            if sh.Name == "全纸筒核价表":
                ws = sh
                break
        
        if ws is None:
            print("Error: Sheet '全纸筒核价表' not found")
            return
        
        # Set values
        # Row 9 corresponds to index 9
        ws.Cells(9, 1).Value = 10    # A9: Diameter
        ws.Cells(9, 2).Value = 30    # B9: Height
        ws.Cells(9, 3).Value = 5000  # C9: Qty
        ws.Cells(9, 5).Value = 26.5  # E9: Inner Tube Length
        
        # Save as new file
        wb.SaveAs(target_file)
        
        # Force recalculate
        excel.CalculateFull()
        
        # Print actual values in Row 9 to verify
        print(f"A9: {ws.Cells(9,1).Value}")
        print(f"B9: {ws.Cells(9,2).Value}")
        print(f"C9: {ws.Cells(9,3).Value}")
        print(f"E9: {ws.Cells(9,5).Value}")
        
        # Extract values from Row 32
        # Use .Value2 for potentially more accurate extraction of numbers/formulas
        results = {
            "Total Cost (H32)": ws.Cells(32, 8).Value,
            "纸管+胶成本 (B32)": ws.Cells(32, 2).Value,
            "圆片+配件 (C32)": ws.Cells(32, 3).Value,
            "面纸 (D32)": ws.Cells(32, 4).Value,
            "纸箱费用 (E32)": ws.Cells(32, 5).Value,
            "加工工资 (F32)": ws.Cells(32, 6).Value,
            "每个运费 (G32)": ws.Cells(32, 7).Value
        }
        
        print("RESULTS_START")
        for key, value in results.items():
            print(f"{key}: {value}")
        print("RESULTS_END")
        
        wb.Close(SaveChanges=True)
        print(f"File saved to: {target_file}")
        
    except Exception as e:
        print(f"Error: {e}")
        if 'wb' in locals():
            wb.Close(SaveChanges=False)
    finally:
        excel.Quit()

if __name__ == "__main__":
    update_excel()
