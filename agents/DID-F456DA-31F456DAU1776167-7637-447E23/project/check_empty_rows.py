import openpyxl

def check_empty_rows():
    wb = openpyxl.load_workbook(r'E:/123/常用文件/纸筒计算试用版001(1) - 副本.xlsx')
    sheet = wb['全纸筒核价表']
    for row in range(1, 40):
        r = [sheet.cell(row=row, column=c).value for c in range(1, 5)]
        if all(v is None for v in r):
            print(f"Row {row} is empty")

if __name__ == "__main__":
    check_empty_rows()
