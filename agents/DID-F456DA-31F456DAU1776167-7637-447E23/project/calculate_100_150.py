
import math

# Inputs
D = 10.0  # 直径 (cm)
H = 15.0  # 高度 (cm)
Qty = 20000  # 数量
Material = "纯白材质 (口杯纸)"
Film_Price_Sq = 0.5  # 覆哑膜
Glue_Price_Sq = 0.7  # 热熔胶

# Material Prices (White Cup Paper)
Outer_Price_Sq = 4.8  # 外管 (元/平)
Inner_Price_Sq = 4.5  # 内管 (元/平)
Disc_Price_Sq = 4.8   # 圆片 (元/平)
Large_Paper_Price = 1.1 # 大规原纸

# 1. Tube Costs
outer_area = (H + 2) * D * math.pi / 10000
outer_cost = outer_area * Outer_Price_Sq

inner_area = (D - 0.2) * math.pi * (H + 3) / 10000
inner_cost = inner_area * Inner_Price_Sq

glue_cost = outer_area * Glue_Price_Sq

# 2. Face Paper & Printing
# Face paper dimensions
fp_w = H + 2 # 17cm
# Length: Circumference + overlap + roll margin + gap
fp_l = D * math.pi + 1.2 + D + 0.8 # 10*3.1415 + 12 = 43.415cm
# 8-up plate (290x440mm)
# fp_w (17) < 29. fp_l (43.4) < 44.
# Fits 1 set per 8-up. 
sets_per_8up = 1
sets_per_large = 8
paper_mat_cost = Large_Paper_Price / sets_per_large

# Printing (8-up machine, 10k/350 standard)
# 20k units, 1 set per 8-up = 20,000 sheets of 8-up.
# Total print cost = (20000 / 10000) * 350 = 700.
printing_cost = 700 / Qty # 0.035

film_cost = (fp_w * fp_l / 10000) * Film_Price_Sq

# 3. Labor
labor_pull = (200 / 500) * ( (H+2)/100 + (H+3)/100 ) # 0.4 * 0.35 = 0.14
labor_roll = 0.10 # 3 roll edges
labor_assembly = 0.064
labor_label = 0.033
Packing_Wage = 0.03
fixed_share = 1400 / 20000 # 0.07

# 4. Others
disc_area = (D + 1) * (D + 1) * 2 / 10000
disc_cost = disc_area * Disc_Price_Sq
punching_cost = 0.05
carton_cost = 0.07 # Larger boxes for D10
shipping_cost = 0.065 # Slightly more weight/volume

# Total
subtotal = outer_cost + inner_cost + glue_cost + paper_mat_cost + printing_cost + film_cost + labor_pull + labor_roll + labor_assembly + labor_label + Packing_Wage + fixed_share + disc_cost + punching_cost + carton_cost + shipping_cost
total_cost = subtotal * 1.05

print(f"Outer: {outer_cost:.4f}, Inner: {inner_cost:.4f}, Glue: {glue_cost:.4f}")
print(f"Paper: {paper_mat_cost:.4f}, Print: {printing_cost:.4f}, Film: {film_cost:.4f}")
print(f"Labor Pull: {labor_pull:.4f}, Roll: {labor_roll:.4f}, Assembly: {labor_assembly:.4f}, Fixed: {fixed_share:.4f}")
print(f"Discs: {disc_cost:.4f}, Others: 0.185")
print(f"Subtotal: {subtotal:.4f}, Final (1.05 loss): {total_cost:.4f}")
