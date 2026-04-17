
import math

# Inputs
D = 9.0  # 直径 (cm)
H = 8.0  # 高度 (cm)
Qty = 10000  # 假设数量为1万个进行保本核算
Material = "纯白材质 (口杯纸)"
Film_Price_Sq = 0.5  # 覆哑膜
Glue_Price_Sq = 0.7  # 热熔胶

# Material Prices (White Cup Paper)
Outer_Price_Sq = 4.8  # 外管 (元/平)
Inner_Price_Sq = 4.5  # 内管 (元/平)
Disc_Price_Sq = 4.8   # 圆片 (元/平)
Large_Paper_Price = 1.1 # 大规原纸

# Special Process: Hot Stamping (烫金)
# 15x15mm = 1.5x1.5cm. 
# 烫金费通常包括：电化铝材料 + 版费分摊 + 加工费。
# 1万个起订量，烫金版费约 100-150元，分摊 0.015。
# 加工费约 0.05-0.08 元/个。
Hot_Stamping_Cost = 0.08 # 综合计入 0.08 元/个

# 1. Tube Costs
outer_area = (H + 2) * D * math.pi / 10000
outer_cost = outer_area * Outer_Price_Sq

inner_area = (D - 0.2) * math.pi * (H + 3) / 10000
inner_cost = inner_area * Inner_Price_Sq

glue_cost = outer_area * Glue_Price_Sq

# 2. Face Paper & Printing
# Face paper dimensions
fp_w = H + 2 # 10cm
fp_l = D * math.pi + 1.2 + D + 0.8 # 9*3.1415 + 11 = 28.27 + 11 = 39.27cm
# 8-up plate (290x440mm)
# fp_w (10) * 2 = 20 < 29. fp_l (39.27) < 44.
# So we can fit 2 sets per 8-up plate.
sets_per_8up = 2
sets_per_large = 16
paper_mat_cost = Large_Paper_Price / sets_per_large

# Printing (8-up machine, 10k/350 standard)
# 10k units, 2 sets per 8-up = 5,000 sheets of 8-up.
# Still charging min 10k sheets or setup fee ~350.
printing_cost = 350 / Qty # 0.035

film_cost = (fp_w * fp_l / 10000) * Film_Price_Sq

# 3. Labor
labor_pull = (200 / 500) * ( (H+2)/100 + (H+3)/100 ) # 0.4 * 0.21 = 0.084
labor_roll = (200 / 6000) * 3 # 0.10
labor_assembly = 450 / 7000 # 0.0643
labor_label = 200 / 6000 # 0.0333
Packing_Wage = 0.03
fixed_share = 1400 / 20000 # 0.07

# 4. Others
disc_area = (D + 1) * (D + 1) * 2 / 10000
disc_cost = disc_area * Disc_Price_Sq
punching_cost = 0.05
carton_cost = 0.06
shipping_cost = 0.055

# Total
subtotal = outer_cost + inner_cost + glue_cost + paper_mat_cost + printing_cost + film_cost + Hot_Stamping_Cost + labor_pull + labor_roll + labor_assembly + labor_label + Packing_Wage + fixed_share + disc_cost + punching_cost + carton_cost + shipping_cost
total_cost = subtotal * 1.05

print(f"Outer: {outer_cost:.4f}, Inner: {inner_cost:.4f}, Glue: {glue_cost:.4f}")
print(f"Paper: {paper_mat_cost:.4f}, Print: {printing_cost:.4f}, Film: {film_cost:.4f}, HotStamp: {Hot_Stamping_Cost:.4f}")
print(f"Labor Pull: {labor_pull:.4f}, Roll: {labor_roll:.4f}, Assembly: {labor_assembly:.4f}, Fixed: {fixed_share:.4f}")
print(f"Discs: {disc_cost:.4f}, Others: 0.165")
print(f"Subtotal: {subtotal:.4f}, Final (1.05 loss): {total_cost:.4f}")
