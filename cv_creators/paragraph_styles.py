from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT

STYLES = getSampleStyleSheet()
STYLES.add(
    ParagraphStyle(
        name="LeftColWhite",
        fontName="Helvetica",
        alignment=TA_LEFT,
        textColor=colors.white,
        fontSize=12,
        leading=12,
    )
)
STYLES.add(
    ParagraphStyle(
        name="LeftColBoldWhite",
        fontName="Helvetica-Bold",
        alignment=TA_LEFT,
        textColor=colors.white,
        fontSize=16,
        leading=12,
        spaceAfter=8,
    )
)
STYLES.add(
    ParagraphStyle(
        name="LeftColBlack",
        fontName="Helvetica",
        alignment=TA_LEFT,
        textColor=colors.black,
        fontSize=12,
        leading=12,
    )
)
STYLES.add(
    ParagraphStyle(
        name="LeftColBoldGreen",
        fontName="Helvetica-Bold",
        alignment=TA_LEFT,
        textColor=colors.green,
        fontSize=16,
        leading=12,
        spaceAfter=8,
        backColor=colors.darkgrey,
        borderPadding=(2.8,5,8.5)
    )
)
STYLES.add(
    ParagraphStyle(
        name="RightCol",
        fontName="Helvetica",
        alignment=TA_LEFT,
        textColor=colors.black,
        fontSize=12,
        leading=12,
    )
)
STYLES.add(
    ParagraphStyle(
        name="RightColBold",
        fontName="Helvetica-Bold",
        alignment=TA_LEFT,
        textColor=colors.black,
        fontSize=16,
        leading=12,
        spaceAfter=8,
    )
)
STYLES.add(
    ParagraphStyle(
        name="RightColBoldGreen",
        fontName="Helvetica-Bold",
        alignment=TA_LEFT,
        textColor=colors.green,
        fontSize=16,
        leading=12,
        spaceAfter=8,
        backColor=colors.darkgrey,
        borderPadding=(2.8,5,8.5)
    )
)
STYLES.add(
    ParagraphStyle(
        name="NameStyleDarkGrey",
        fontName="Helvetica",
        fontSize=32,
        alignment=TA_LEFT,  # Left align text
        textColor=colors.black,
        spaceAfter=16,
    )
)

STYLES.add(
    ParagraphStyle(
        name="JobTitleDarkGrey",
        fontName="Helvetica",
        fontSize=24,
        alignment=TA_LEFT,  # Left align text
        textColor=colors.darkgrey,
        spaceAfter=14,
    )
)

STYLES.add(
    ParagraphStyle(
        name="SummaryDarkGrey",
        fontName="Helvetica",
        fontSize=14,
        alignment=TA_LEFT,  # Left align text
        textColor=colors.darkgrey,
        spaceAfter=48,
    )
)
STYLES.add(
    ParagraphStyle(
        name="NameStyleWhite",
        fontName="Helvetica",
        fontSize=32,
        alignment=TA_LEFT,  # Left align text
        textColor=colors.white,
        spaceAfter=16,
    )
)

STYLES.add(
    ParagraphStyle(
        name="JobTitleGreen",
        fontName="Helvetica",
        fontSize=24,
        alignment=TA_LEFT,  # Left align text
        textColor=colors.green,
        spaceAfter=14,
    )
)

STYLES.add(
    ParagraphStyle(
        name="SummaryGreen",
        fontName="Helvetica",
        fontSize=14,
        alignment=TA_LEFT,  # Left align text
        textColor=colors.green,
        spaceAfter=48,
    )
)