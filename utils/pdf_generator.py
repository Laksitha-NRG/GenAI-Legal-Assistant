from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os


def generate_pdf(pdf_path, contract_name, overall_risk, clause_details, language):
    doc = SimpleDocTemplate(pdf_path, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    # Register Unicode font for Hindi
    font_path = "fonts/NotoSansDevanagari-Regular.ttf"
    pdfmetrics.registerFont(TTFont("NotoHindi", font_path))

    if language == "Hindi":
        styles["Normal"].fontName = "NotoHindi"
        styles["Heading1"].fontName = "NotoHindi"

    # Title
    elements.append(Paragraph("<b>Contract Risk Analysis Report</b>", styles["Heading1"]))
    elements.append(Paragraph(f"Contract: {contract_name}", styles["Normal"]))
    elements.append(Paragraph(f"Overall Risk: {overall_risk}", styles["Normal"]))
    elements.append(Paragraph("<br/>", styles["Normal"]))

    # Clauses
    for i, clause in enumerate(clause_details, 1):
        elements.append(
            Paragraph(f"<b>Clause {i} | Risk: {clause['risk']}</b>", styles["Normal"])
        )
        elements.append(Paragraph(clause["text"], styles["Normal"]))
        elements.append(Paragraph(clause["explanation"], styles["Normal"]))
        elements.append(Paragraph("<br/>", styles["Normal"]))

    doc.build(elements)
