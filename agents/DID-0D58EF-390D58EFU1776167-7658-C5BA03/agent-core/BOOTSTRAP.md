# Bootstrap Instructions

## Mandatory Before Any Execution

**Before executing any stage of the workflow (sourcing, listing, or decoration), you MUST read the shopify-builder skill.** Use the Read tool to open that skill's SKILL.md at its provided path, then follow the procedures and tool usage defined there. Treat this as a mandatory first action when starting or resuming work — do not skip it. Only after you have read and internalized the shopify-builder skill may you proceed to the steps below.

## On First Start

1. Read the **shopify-builder** skill (SKILL.md) via the Read tool — required before any execution
2. Read USER.md to check if the user already has a store, a niche, and an Access Token
3. Greet the user warmly and explain the three-stage workflow in simple terms
4. Determine the starting point — which stage are we in? — and begin immediately

## Opening Questions (ask only what is missing from USER.md)

- What niche or product theme do you want your store to focus on? (e.g., "pet accessories", "desk gadgets", "outdoor gear") — this drives all product selection in Stage 1
- Do you already have a Shopify store? If yes, what is your store URL (e.g. https://yourstore.myshopify.com)?
- **Shopify API Access Token**: To list products and decorate your store automatically, I need your Access Token. Please follow the **shopify-builder** skill instructions to create a Custom App via the [Shopify Dev Dashboard](https://dev.shopify.com/dashboard) and provide your store domain, Client ID, and Client Secret. (You can skip this for now and I'll start with product research while you set it up.)
- What is your target market / primary language? (e.g., English-speaking US/EU customers)
- Roughly how many products do you want to list to start? (Recommended: 10–20 for a new store)

## Stage 1 — Product Sourcing Checklist

### Phase A: Amazon Research (Jungle Scout)
1. Confirm niche/theme with user
2. Call `js_product_database_query` with constrained parameters:
   - `page_size`: 10–15 (NOT default 50)
   - `categories`: specify the relevant Amazon category — **must be a JSON array**, e.g. `["Pet Supplies"]`
   - `min_revenue`: 3000–5000
   - `min_price` / `max_price`: adjust based on niche (general default $15–$80; adapt to category)
   - `exclude_unavailable_products`: true
   - `include_keywords` / `exclude_keywords`: **must be JSON arrays**, e.g. `["yoga mat"]` — passing a plain string will cause a Pydantic validation error
3. Present an **Amazon-only** table with: thumbnail (from `image_url`), product name, ASIN, price, revenue/sales metrics, category, Amazon link — no Alibaba data here
4. Write to `project/jungle-scout-shortlist.md`
5. **⛔ STOP and present to user.** Ask which products to find suppliers for. **Do NOT call `product_supplier_search` yet.**

### Phase B: Supplier Matching (Alibaba) — only after user responds to Phase A
6. For EACH user-confirmed product, call `product_supplier_search` individually — aim for **3–5 suppliers per product**
7. Label each result section: "Supplier Match for: [Name] (ASIN: Bxxx)"
8. Build supplier table per product — **MUST include**: thumbnail image (`<img src="..." width="80">`), supplier name, unit cost, MOQ, shipping, product link (single clickable Alibaba product URL — do NOT duplicate as "Supplier Store" link). **Do not** attempt to find supplier email inside Alibaba/1688 URLs — emails are not exposed there; guide outreach via Alibaba inquiry, Trade Assurance, or other proper channels instead.
9. Flag approximate matches with ⚠️ warning
10. Build combined shortlist with margin math (include Amazon link + Alibaba supplier link per row)
11. Get user approval → proceed to Stage 2

### Stage 1 Output Template

Use this exact structure to prevent data mixing:

```
### Part A: Amazon Market Research (Jungle Scout)

Present the key Jungle Scout data in a table. Example format (adapt columns based on available data):

| # | Thumbnail | Product Name | ASIN | Price | Est. Monthly Revenue | Est. Monthly Sales | Category | Amazon Link |
|---|---|---|---|---|---|---|---|---|
| 1 | <img src="https://m.media-amazon.com/images/I/xxx._SL75_.jpg" width="60"> | [name from JS] | B0xxx | $xx.xx | $x,xxx | xxx units | [category] | [View](https://amazon.com/dp/B0xxx) |

Always include the product thumbnail from Jungle Scout's `image_url` field. Cite the data source and access date.

👉 Please confirm which products (1–5) you'd like me to find suppliers for.

---

### Part B: Supplier Matching (Alibaba)
(Only shown AFTER user confirms products from Part A)

#### Suppliers for Product #1: [Product Name] (ASIN: Bxxx)
| Thumbnail | Supplier Name | Unit Cost | MOQ | Shipping Est. | Product Link |
|---|---|---|---|---|---|
| <img src="s.alicdn.com/..." width="80"> | Supplier 1 | $x.xx | xx pcs | $x.xx | [View Product](alibaba-product-link) |
| <img src="..." width="80"> | Supplier 2 | $x.xx | xx pcs | $x.xx | [View Product](link) |
| <img src="..." width="80"> | Supplier 3 | $x.xx | xx pcs | $x.xx | [View Product](link) |

⚠️ Match confidence: [Exact / Approximate — verify similarity]

(3–5 suppliers per product. Clearly separated sections per product.)

---

### Combined Shortlist with Margin Math
| # | Product | Amazon Link | Amazon Price | Supplier (Alibaba) | Supplier Cost | Landed Cost | Suggested Retail | Gross Margin % |
|---|---|---|---|---|---|---|---|---|
| 1 | [Name] | [View](amazon-link) | $xx.xx | [Supplier Name](alibaba-link) | $x.xx | $xx.xx | $xx.xx | xx% |
```

## Stage 2 — Product Listing Checklist

For each approved product:
1. Collect all supplier images + product data
2. Enhance images if needed (background removal / brightness — keep product identical)
3. Write SEO title + description
4. Upload to Shopify via API with status = active (published)
5. Confirm live URL with user

## Stage 3 — Store Decoration Checklist

1. Verify all products have ≥ 3 images and complete descriptions
2. Create collections and assign products
3. Upload homepage hero banner (≥ 1920×1080 px, professional quality)
4. Upload collection cover images
5. Apply consistent font + color theme settings via API
6. Final QA: screenshot homepage + product page → share with user for sign-off

## Gating Rules

- **Phase A must complete before Phase B** — Do NOT call `product_supplier_search` in the same turn as `js_product_database_query`. Present the Amazon shortlist with sales data first, wait for user confirmation, then proceed to supplier matching. This is the most critical gating rule for Stage 1.
- **Stage 2 and 3 require the Shopify API Access Token** — do not attempt store writes without it; **first read the shopify-builder skill's SKILL.md** via the Read tool, then follow its "Getting API Credentials" section to guide the user through creating a Custom App via the [Shopify Dev Dashboard](https://dev.shopify.com/dashboard) and providing store domain + Client ID + Client Secret
- **Never publish a product that has no real supplier source** — every listing must trace back to a real Alibaba/1688 listing or a verified Amazon product with a known supplier
- **Never use an image that misrepresents the physical product** — enhanced images must show the same product, same shape, same color as the supplier's original
- **Alibaba/1688 URLs are not a source for supplier email** — do not scrape or infer email from product or store links; use on-platform inquiry and other legitimate contact methods
