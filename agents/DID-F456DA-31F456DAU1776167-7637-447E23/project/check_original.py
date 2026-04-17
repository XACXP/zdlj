import openpyxl

def check_original():
    wb = openpyxl.load_workbook(r'E:/123/常用文件/纸筒计算试用版001(1) - 副本.xlsx')
    sheet = wb['全纸筒核价表']
    print(f"H32: {sheet['H32'].value}")
    print(f"H55: {sheet['H55'].value}")
    
if __name__ == "__main__":
    check_original()
