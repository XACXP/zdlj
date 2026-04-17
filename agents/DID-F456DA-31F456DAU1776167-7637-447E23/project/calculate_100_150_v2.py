
import math

# Inputs
D = 10.0  # 直径 (cm)
H = 15.0  # 高度 (cm)
Qty = 20000  # 数量
Material = "纯白材质 (口杯纸)"

# Machine Correction: 8-up max paper 36x52cm
# Face paper dimensions: 
# Height side: H + 2 = 17cm
# Length side: D*pi + 1.2 + D + 0.8 = 31.415 + 12 = 43.415cm
# Orientation check on 36x52cm:
# Option 1: 52/43.4 = 1, 36/17 = 2. Total = 2 sets per 8-up.
sets_per_8up = 2
sets_per_large = sets_per_8up * 8 # Large sheet is 8 times 8-up

# Material Prices (White Cup Paper)
Outer_Price_Sq = 4.8
Inner_Price_Sq = 4.5
Disc_Price_Sq = 4.8
Large_Paper_Price = 1.1

# 1. Tube Costs
outer_area = (H + 2) * D * math.pi / 10000
outer_cost = outer_area * Outer_Price_Sq
inner_area = (D - 0.2) * math.pi * (H + 3) / 10000
inner_cost = inner_area * Inner_Price_Sq
glue_cost = outer_area * 0.7

# 2. Face Paper
paper_mat_cost = Large_Paper_Price / sets_per_large # 1.1 / 16 = 0.0688
# Printing: 350 per 10k sheets. 
# 20k units / 2 sets per sheet = 10k sheets.
# Total print cost = 350.
printing_cost = 350 / Qty # 0.0175

fp_w = 17
fp_l = 43.415
film_cost = (fp_w * fp_l / 10000) * 0.5

# 3. Labor
labor_pull = (200 / 500) * ( (H+2)/100 + (H+3)/100 ) # 0.14
labor_roll = 0.10
labor_assembly = 0.064
labor_label = 0.033
Packing_Wage = 0.03
fixed_share = 1400 / 20000 # 0.07

# 4. Others
disc_area = (D + 1) * (D + 1) * 2 / 10000
disc_cost = disc_area * Disc_Price_Sq
punching_cost = 0.05
carton_cost = 0.07
shipping_cost = 0.085

# Total
subtotal = outer_cost + inner_cost + glue_cost + paper_mat_cost + printing_cost + film_cost + labor_pull + labor_roll + labor_assembly + labor_label + Packing_Wage + fixed_share + disc_cost + punching_cost + carton_cost + shipping_cost
total_cost = subtotal * 1.05

print(f"Sets per 8-up: {sets_per_8up}")
print(f"Outer: {outer_cost:.4f}, Inner: {inner_cost:.4f}, Glue: {glue_cost:.4f}")
print(f"Paper: {paper_mat_cost:.4f}, Print: {printing_cost:.4f}, Film: {film_cost:.4f}")
print(f"Labor: {labor_pull+labor_roll+labor_assembly+labor_label+Packing_Wage:.4f}, Fixed: {fixed_share:.4f}")
print(f"Discs: {disc_cost:.4f}, Others: 0.205")
print(f"Subtotal: {subtotal:.4f}, Final (1.05 loss): {total_cost:.4f}")
