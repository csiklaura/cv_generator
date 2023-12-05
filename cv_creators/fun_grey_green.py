from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_LEFT
import io
from .paragraph_styles import STYLES


def draw_background(canvas, doc):
    # Set the size of the rectangle
    width, height = A4
    canvas.setFillColor(colors.darkgrey)
    canvas.rect(0, height - 150, width, 150, stroke=False, fill=True)
    canvas.setFillColor(colors.green)
    canvas.rect(0, 0, width, 20, stroke=False, fill=True)

def create_cv(user_info):
    pdf_buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        pdf_buffer,
        pagesize=A4,
        rightMargin=16,
        leftMargin=16,
        topMargin=16,
        bottomMargin=32,
    )
    # Container for the 'Flowable' objects
    elements = []

    # Calculate the width for the columns
    left_col_width = doc.width / 3 + 2
    right_col_width = (doc.width / 3) * 2 - 2

    heading_columns = Table(
        [
            [
                [],
                [
                    Paragraph(user_info["name"], STYLES["NameStyleWhite"]),
                    Paragraph(user_info["title"], STYLES["JobTitleGreen"]),
                    Paragraph(user_info["profile_summary"], STYLES["SummaryGreen"]),
                ],
            ]
        ],
        spaceAfter=64,
        colWidths=[left_col_width, right_col_width],
    )
    heading_columns.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP")]))
    elements.append(heading_columns)

    # Change newline chars to <br/>
    user_info = change_newline_char_to_br(user_info)

    # Left column content
    left_content = [
        Paragraph("Contact", STYLES["LeftColBoldGreen"]),
        Paragraph(user_info["phone"], STYLES["LeftColBlack"]),
        Paragraph(user_info["email"], STYLES["LeftColBlack"]),
        Spacer(1, 12),
        Paragraph("Skills", STYLES["LeftColBoldGreen"]),
        Paragraph(user_info["skills"], STYLES["LeftColBlack"]),
        Spacer(1, 12),
        Paragraph("Languages", STYLES["LeftColBoldGreen"]),
        Paragraph(user_info["language"], STYLES["LeftColBlack"]),
        Spacer(1, 12),
        Paragraph("Expertise", STYLES["LeftColBoldGreen"]),
        Paragraph(user_info["expertise"], STYLES["LeftColBlack"]),
        Spacer(1, 12),
    ]

    # Right column content
    right_content = [
        Paragraph("Experience", STYLES["RightColBoldGreen"]),
        Paragraph(user_info["experience"], STYLES["RightCol"]),
        Spacer(1, 12),
        Paragraph("Education", STYLES["RightColBoldGreen"]),
        Paragraph(user_info["education"], STYLES["RightCol"]),
        Spacer(1, 12),
        Paragraph("Certifications", STYLES["RightColBoldGreen"]),
        Paragraph(user_info["certifications"], STYLES["RightCol"]),
        Spacer(1, 12),
    ]

    # Combine the two columns into a single flowable object using a Table
    columns = Table(
        [[left_content, right_content]], colWidths=[left_col_width, right_col_width]
    )
    columns.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP")]))
    elements.append(columns)

    # Build the document
    doc.build(elements, onFirstPage=draw_background, onLaterPages=draw_background)
    pdf_buffer.seek(0)
    return pdf_buffer


def change_newline_char_to_br(user_info: str) -> str:
    user_info = {key: value.replace("\n", "<br/>") for key, value in user_info.items()}
    return user_info
