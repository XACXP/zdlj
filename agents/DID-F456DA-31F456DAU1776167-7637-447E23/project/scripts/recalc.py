import win32com.client as win32
import os
import sys
import time

def recalculate_excel(filepath):
    abs_path = os.path.abspath(filepath)
    print(f"Opening {abs_path}...")
    
    # Try to connect to a running Excel instance or start a new one
    try:
        excel = win32.GetActiveObject('Excel.Application')
    except:
        excel = win32.DispatchEx('Excel.Application')
    
    excel.Visible = False
    excel.DisplayAlerts = False
    
    try:
        wb = excel.Workbooks.Open(abs_path)
        print("Recalculating...")
        # Recalculate all formulas
        excel.CalculateFull()
        # Wait a bit for calculation to finish if it's asynchronous
        time.sleep(2)
        
        print("Saving...")
        wb.Save()
        wb.Close()
        print("Done.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        excel.Quit()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python recalc.py <excel_file>")
        sys.exit(1)
    recalculate_excel(sys.argv[1])
