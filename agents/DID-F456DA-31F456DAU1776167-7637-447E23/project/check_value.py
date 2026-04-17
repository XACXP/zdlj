import openpyxl

def check_value():
    wb = openpyxl.load_workbook(r'E:/123/常用文件/纸筒计算试用版001(1) - 副本.xlsx', data_only=True)
    sheet = wb['全纸筒核价表']
    print(f"O29: {sheet['O29'].value}")
    print(f"O57: {sheet['O57'].value}")
    
if __name__ == "__main__":
    check_value()
