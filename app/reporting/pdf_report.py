from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, Image,
    PageBreak, ListFlowable, ListItem
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from datetime import datetime
from reportlab.platypus import Table
from reportlab.lib import colors
from reportlab.platypus import ListFlowable, ListItem
import re

def generate_pdf_report(filename, normalized, ratios, validation, insights, graph_paths, risk_score, risk_level):

    doc = SimpleDocTemplate(filename)
    elements = []
    styles = getSampleStyleSheet()


    elements.append(Paragraph("<b>AI Financial Intelligence Report</b>", styles["Title"]))
    elements.append(Spacer(1, 0.4 * inch))

    elements.append(Paragraph(f"Report Date: {datetime.now().strftime('%Y-%m-%d')}", styles["Normal"]))
    elements.append(Spacer(1, 0.3 * inch))

    elements.append(Paragraph("<b>Executive Summary</b>", styles["Heading1"]))
    elements.append(Spacer(1, 0.2 * inch))


    elements.append(Paragraph(f"<b>Financial Risk Score:</b> {risk_score}/100", styles["Normal"]))
    elements.append(Spacer(1, 0.2 * inch))


    if risk_level == "Low Risk":
        risk_color = colors.green
    elif risk_level == "Moderate Risk":
        risk_color = colors.orange
    else:
        risk_color = colors.red

    risk_table = Table([[f" {risk_level} "]], colWidths=3*inch)

    risk_table.setStyle([
        ('BACKGROUND', (0, 0), (-1, -1), risk_color),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTSIZE', (0, 0), (-1, -1), 14),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
    ])

    elements.append(risk_table)
    elements.append(Spacer(1, 0.4 * inch))
    elements.append(Spacer(1, 0.3 * inch))

    summary_points = [
        "Comprehensive AI-based financial analysis performed.",
        "Key profitability, leverage, and cash flow metrics evaluated.",
        "Validation checks conducted for accounting consistency.",
        "Risk indicators assessed using rule-based scoring."
    ]

    elements.append(ListFlowable(
        [ListItem(Paragraph(point, styles["Normal"])) for point in summary_points],
        bulletType='bullet'
    ))

    elements.append(Spacer(1, 0.5 * inch))

    elements.append(Paragraph("<b>AI Analytical Summary</b>", styles["Heading2"]))
    elements.append(Spacer(1, 0.2 * inch))


    cleaned_insights = insights.replace("**", "")

    points = re.split(r'\d+\.\s+', cleaned_insights)

    bullet_points = []

    for point in points:
        point = point.strip()
        if point:
            bullet_points.append(ListItem(Paragraph(point, styles["Normal"])))

    elements.append(ListFlowable(bullet_points, bulletType='bullet'))
    elements.append(Spacer(1, 0.4 * inch))


    elements.append(Paragraph("<b>Financial Summary</b>", styles["Heading1"]))
    elements.append(Spacer(1, 0.3 * inch))

    summary_data = [
        ["Revenue", normalized["income_statement"]["revenue"]],
        ["Net Income", normalized["income_statement"]["net_income"]],
        ["Total Assets", normalized["balance_sheet"]["total_assets"]],
        ["Total Liabilities", normalized["balance_sheet"]["total_liabilities"]],
        ["Equity", normalized["balance_sheet"]["equity"]],
        ["Operating Cash Flow", normalized["cash_flow"]["operating_cash_flow"]],
    ]

    table = Table(summary_data, hAlign='LEFT')
    elements.append(table)
    elements.append(Spacer(1, 0.5 * inch))

    # Ratios
    elements.append(Paragraph("<b>Financial Ratios</b>", styles["Heading1"]))
    elements.append(Spacer(1, 0.2 * inch))

    ratio_data = [[k, v] for k, v in ratios.items()]
    elements.append(Table(ratio_data))
    elements.append(Spacer(1, 0.5 * inch))

    # Validation
    elements.append(Paragraph("<b>Validation Findings</b>", styles["Heading1"]))
    elements.append(Spacer(1, 0.2 * inch))

    if validation:
        elements.append(ListFlowable(
            [ListItem(Paragraph(v, styles["Normal"])) for v in validation],
            bulletType='bullet'
        ))
    else:
        elements.append(Paragraph("No inconsistencies detected.", styles["Normal"]))

    elements.append(PageBreak())


    elements.append(Paragraph("<b>Financial Visualizations</b>", styles["Heading1"]))
    elements.append(Spacer(1, 0.3 * inch))

    for path in graph_paths.values():
        img = Image(path, width=5 * inch, height=3 * inch)
        elements.append(img)
        elements.append(Spacer(1, 0.4 * inch))

    doc.build(elements)