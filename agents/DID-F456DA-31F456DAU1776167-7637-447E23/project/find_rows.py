import openpyxl

def find_rows():
    wb = openpyxl.load_workbook(r'E:/123/常用文件/纸筒计算试用版001(1) - 副本.xlsx')
    sheet = wb['全纸筒核价表']
    for row in range(25, 60):
        r = [sheet.cell(row=row, column=c).value for c in range(1, 10)]
        # Filter out empty rows
        if any(v is not None for v in r):
            print(f"Row {row}: {r}")

if __name__ == "__main__":
    find_rows()
