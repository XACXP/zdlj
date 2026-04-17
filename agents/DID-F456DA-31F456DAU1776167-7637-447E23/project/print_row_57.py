import openpyxl

def print_row_57():
    wb = openpyxl.load_workbook(r'E:/123/常用文件/纸筒计算试用版001(1) - 副本.xlsx', data_only=True)
    sheet = wb['全纸筒核价表']
    for c in range(1, 20):
        print(f"Col {c} ({chr(64+c)}): {sheet.cell(row=57, column=c).value}")

if __name__ == "__main__":
    print_row_57()
