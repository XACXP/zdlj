
import math

# Inputs
C6 = 7.5  # 直径
D6 = 16   # 高度
E6 = 100000  # 数量
F6 = 0.5  # 覆膜单价
G6 = 19   # 内管长度 (H+3)
H6 = 1    # 内管卷边
I6 = 0.7  # 热熔胶单价

C15 = 4.8 # 外管平方价格 (口杯纸)
C19 = 4.5 # 内管平方价格 (口杯纸)
E15 = 4.8 # 圆片平方价格 (口杯纸)

J6 = 200  # 拉管1天工资
K6 = 500  # 1天米数
B9 = 200  # 卷边1天工资
C9 = 6000 # 1天次数
D9 = 450  # 装配1天工资
E9 = 7000 # 1天个数
L9 = 200  # 贴标1天工资
M9 = 6000 # 1天次数
N9 = 1400 # 1天厂租
O9 = 20000 # 1天产量 (用户设定)
M22 = 0.03 # 打包工资

# Face Paper Calculation (based on user's 4-up logic)
# 4-up sheet (440x590) fits 2 units.
# Large scale sheet (889x1192) fits 4 units of 4-up sheets.
# So 1 Large sheet = 8 units.
paper_cost_per_unit = 1.1 / 8  # 0.1375

# Printing Cost (4-up)
# User correction: 550 yuan per 10,000 sheets.
# 100k units = 50k sheets of 4-up.
printing_total = 350 + (E6 / 2 / 10000) * 550
printing_per_unit = printing_total / E6 # 0.031

# Formulas from Excel
# Row 14, Col C (外管圆周面积)
C14 = (D6 + 2) * C6 * 3.1415 / 10000
# Row 17, Col C (外管价格)
C17 = C15 * C14
# Row 18, Col C (内管圆周面积)
C18 = (C6 - 0.2) * 3.14159 * (G6 + H6) / 10000
# Row 21, Col C (内管价格)
C21 = C19 * C18
# Row 23, Col C (热熔胶成本)
C23 = C14 * I6

# Row 14, Col E (圆片面积2片)
E14 = (C6 + 1) * (C6 + 1) * 2 / 10000
# Row 16, Col E (圆片价格)
E16 = E15 * E14
# Row 17, Col E (贴+冲压1)
E17 = 0.05

# Face Paper
G14 = C6 * 3.1415 + 1.2 + C6 + 0.8
G15 = D6 + 2
# G18 (纸张费用)
G18 = paper_cost_per_unit
# G19 (覆膜费用)
G19 = F6 * G15 * G14 / 10000
# G20 (印刷费用)
G20 = printing_per_unit

# Wages
M14 = J6 / K6 * (D6 + 2) / 100 + J6 / K6 * (G6 + H6) / 100
M16 = L9 / M9
M17 = B9 / C9
M18 = 2 + H6
M19 = M18 * M17
M21 = D9 / E9
M23 = N9 / O9

# Totals
C29 = C17 + C21 + C23 # 纸管+胶
E29 = E16 + E17       # 圆片+配件
G29 = G20 + G19 + G18 # 面纸费用
J29 = 0.05            # 纸箱 (default)
M27 = M14 + M16 + M19 + M21 + M22 + M23 # 加工工资合计
M29 = M27

O29 = round(C29 + E29 + J29 + M29 + G29 + 0.05, 3) # + 0.05 for 运费? O29 in excel is ROUND(C29+E29+J29+M29+G29+O29,3)
# O29 (运费) is 0.05 in row 29 Col O.

print(f"外管价格 (C17): {C17:.4f}")
print(f"内管价格 (C21): {C21:.4f}")
print(f"热熔胶成本 (C23): {C23:.4f}")
print(f"圆片价格 (E16): {E16:.4f}")
print(f"冲压/贴费 (E17): {E17:.4f}")
print(f"纸张费用 (G18): {G18:.4f}")
print(f"覆膜费用 (G19): {G19:.4f}")
print(f"印刷费用 (G20): {G20:.4f}")
print(f"拉管工资 (M14): {M14:.4f}")
print(f"贴标工资 (M16): {M16:.4f}")
print(f"卷边工资 (M19): {M19:.4f}")
print(f"装配工资 (M21): {M21:.4f}")
print(f"打包工资 (M22): {M22:.4f}")
print(f"厂租分摊 (M23): {M23:.4f}")
print(f"---")
print(f"纸管+胶成本 (C29): {C29:.4f}")
print(f"圆片+配件 (E29): {E29:.4f}")
print(f"面纸费用 (G29): {G29:.4f}")
print(f"纸箱费用 (J29): {J29:.4f}")
print(f"加工工资 (M29): {M29:.4f}")
print(f"运费 (O29): 0.05")
print(f"总成本 (O29_total): {O29:.4f}")
