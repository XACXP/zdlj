
import math

# Inputs
D = 8.0  # 直径 (cm)
H = 18.0 # 高度 (cm)
Qty = 20000  # 数量
Material = "普通材质 (灰板)"
Film_Price_Sq = 0.5  # 覆哑膜单价 (元/平)
Glue_Price_Sq = 0.7  # 热熔胶单价 (元/平)

# Material Prices (Normal Greyboard)
Outer_Price_Sq = 3.5  # 外管平方价格 (元/平)
Inner_Price_Sq = 3.0  # 内管平方价格 (元/平)
Disc_Price_Sq = 3.7   # 圆片平方价格 (元/平)
Large_Paper_Price = 1.1 # 大规原纸单价

# Labor and Overheads
Daily_Wage_Pull = 200
Daily_Meters = 500
Daily_Wage_Roll = 200
Daily_Roll_Count = 6000
Daily_Wage_Assembly = 450
Daily_Assembly_Count = 7000
Daily_Wage_Label = 200
Daily_Label_Count = 6000
Packing_Wage = 0.03
Daily_Fixed_Cost = 1400
Daily_Capacity = 20000

# 1. Tube Costs
outer_area = (H + 2) * D * math.pi / 10000
outer_cost = outer_area * Outer_Price_Sq

inner_area = (D - 0.2) * math.pi * (H + 3) / 10000
inner_cost = inner_area * Inner_Price_Sq

glue_cost = outer_area * Glue_Price_Sq

# 2. Face Paper & Printing
# Face paper dimensions
fp_w = H + 2 # 20cm
fp_l = D * math.pi + 1.2 + D + 0.8 # 8*3.1415 + 9.5 = 25.13 + 9.5 = 34.63cm
# 8-up plate (290x440mm)
# Can we fit 1 unit? Yes. 2 units? 20cm*2 = 40cm < 44cm. 34.63cm < 29cm? No.
# If rotated: fp_l (34.63) < 44cm (Yes), fp_w (20) < 29cm (Yes).
# Only fits 1 set per 8-up plate because 20*2=40 < 44 but 34.63 > 29.
# Actually, check if 2 sets fit in 4-up (440x590).
# 4-up: 59cm/34.63=1, 44cm/20=2. Total 2 sets.
# Large paper (889x1192) has 4 units of 4-up = 8 sets per large paper.
sets_per_large = 8
paper_mat_cost = Large_Paper_Price / sets_per_large

# Printing (8-up machine, 10k/350 standard)
# 20k units, 1 set per 8-up = 20k sheets of 8-up.
# Total print cost = (20000 / 10000) * 350 = 700.
printing_cost = 700 / Qty # 0.035

film_cost = (fp_w * fp_l / 10000) * Film_Price_Sq

# 3. Labor
labor_pull = (Daily_Wage_Pull / Daily_Meters) * ( (H+2)/100 + (H+3)/100 )
labor_roll = (Daily_Wage_Roll / Daily_Roll_Count) * 3 # 3 roll edges
labor_assembly = Daily_Wage_Assembly / Daily_Assembly_Count
labor_label = Daily_Wage_Label / Daily_Label_Count
fixed_share = Daily_Fixed_Cost / Daily_Capacity

# 4. Others
disc_area = (D + 1) * (D + 1) * 2 / 10000
disc_cost = disc_area * Disc_Price_Sq
punching_cost = 0.05
carton_cost = 0.05
shipping_cost = 0.05

# Total
subtotal = outer_cost + inner_cost + glue_cost + paper_mat_cost + printing_cost + film_cost + labor_pull + labor_roll + labor_assembly + labor_label + Packing_Wage + fixed_share + disc_cost + punching_cost + carton_cost + shipping_cost
total_cost = subtotal * 1.05

print(f"Outer: {outer_cost:.4f}, Inner: {inner_cost:.4f}, Glue: {glue_cost:.4f}")
print(f"Paper: {paper_mat_cost:.4f}, Print: {printing_cost:.4f}, Film: {film_cost:.4f}")
print(f"Labor Pull: {labor_pull:.4f}, Roll: {labor_roll:.4f}, Assembly: {labor_assembly:.4f}, Fixed: {fixed_share:.4f}")
print(f"Discs: {disc_cost:.4f}, Others: 0.15")
print(f"Subtotal: {subtotal:.4f}, Final (1.05 loss): {total_cost:.4f}")
