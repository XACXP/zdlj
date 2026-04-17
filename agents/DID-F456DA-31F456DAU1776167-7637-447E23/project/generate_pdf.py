
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import os

def create_quote_pdf(output_path):
    # Register Chinese font (Microsoft YaHei)
    # Using raw path and checking for .ttc
    font_path = r'C:\Windows\Fonts\msyh.ttc'
    if not os.path.exists(font_path):
        font_path = r'C:\Windows\Fonts\msyh.ttf'
        
    try:
        # Standard TTFont initialization
        # subfontIndex is used for .ttc files
        pdfmetrics.registerFont(TTFont('YaHei', font_path, subfontIndex=0))
    except Exception as e:
        print(f"Primary font registration failed: {e}")
        # Try a simpler registration if it's a .ttf
        try:
            pdfmetrics.registerFont(TTFont('YaHei', font_path))
        except Exception as e2:
            print(f"Secondary font registration failed: {e2}")
            # If all fails, the PDF will likely have missing characters for Chinese
            # but we'll try to use a standard font to at least produce a file
            pass

    doc = SimpleDocTemplate(output_path, pagesize=A4)
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Title'],
        fontName='YaHei',
        fontSize=18,
        spaceAfter=20
    )
    
    normal_style = ParagraphStyle(
        'NormalStyle',
        parent=styles['Normal'],
        fontName='YaHei',
        fontSize=10,
        leading=14
    )
    
    header_style = ParagraphStyle(
        'HeaderStyle',
        parent=styles['Heading2'],
        fontName='YaHei',
        fontSize=14,
        spaceBefore=10,
        spaceAfter=10
    )
    
    story = []
    
    # Title
    story.append(Paragraph("东嘉纸罐 (Dongjia Paper Tube Factory) - 报价单", title_style))
    
    # Quote info
    info_data = [
        ["报价单号：", "DJ-20260415-005"],
        ["报价日期：", "2026年04月15日"],
        ["有效期至：", "2026年05月15日"]
    ]
    t_info = Table(info_data, colWidths=[100, 300])
    t_info.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), 'YaHei'),
        ('FONTSIZE', (0,0), (-1,-1), 10),
        ('ALIGN', (0,0), (0,-1), 'LEFT'),
    ]))
    story.append(t_info)
    story.append(Spacer(1, 20))
    
    # Product Specifications
    story.append(Paragraph("一、 产品规格描述", header_style))
    spec_data = [
        ["项目", "详细参数"],
        ["产品名称", "定制圆筒纸罐"],
        ["产品规格", "直径 9.0cm × 高度 8.0cm"],
        ["材质要求", "纯白材质（内外均为高档口杯纸）"],
        ["表面工艺", "表面覆哑膜（防潮耐磨，触感细腻）"],
        ["特殊工艺", "烫金工艺 (Logo/图案尺寸：15mm × 15mm)"]
    ]
    t_spec = Table(spec_data, colWidths=[120, 300])
    t_spec.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), 'YaHei'),
        ('FONTSIZE', (0,0), (-1,-1), 10),
        ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ALIGN', (0,0), (-1,0), 'CENTER'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_spec)
    story.append(Spacer(1, 20))
    
    # Pricing
    story.append(Paragraph("二、 价格明细", header_style))
    price_data = [
        ["规格项目", "订购数量 (个)", "含税单价 (元/个)", "合计总价 (元)"],
        ["90/80 规格纸罐", "10,000", "1.65", "16,500.00"]
    ]
    t_price = Table(price_data, colWidths=[150, 100, 100, 100])
    t_price.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), 'YaHei'),
        ('FONTSIZE', (0,0), (-1,-1), 10),
        ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_price)
    story.append(Paragraph("<br/>价格计算说明：已包含 25% 利润加成及 10% 税收加成。总价为人民币：壹万陆仟伍佰元整。", normal_style))
    story.append(Spacer(1, 20))
    
    # Business Terms
    story.append(Paragraph("三、 商务条款", header_style))
    terms = [
        "1. 交货方式：EXW 离厂价（不含运费）。",
        "2. 交货周期：自确认样稿及收到订金之日起，预估 12-15 天发货。",
        "3. 付款方式：预付总额的 30% 作为定金；生产完成发货前支付剩余 70% 尾款。",
        "4. 品质说明：所有产品均严格按照核准的材质与工艺标准生产。"
    ]
    for term in terms:
        story.append(Paragraph(term, normal_style))
    
    story.append(Spacer(1, 40))
    story.append(Paragraph("报价单位：东嘉纸罐 (Dongjia Paper Tube Factory)", normal_style))
    story.append(Paragraph("联系地址：浙江省温州市龙港市...", normal_style))
    
    doc.build(story)
    print(f"PDF successfully created at: {output_path}")

if __name__ == "__main__":
    output_path = r'C:\Users\Admin\.accio\accounts\1747493724\agents\DID-F456DA-2B0D4C\project\东嘉纸罐报价单_90x80.pdf'
    create_quote_pdf(output_path)
