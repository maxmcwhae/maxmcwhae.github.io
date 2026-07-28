#!/usr/bin/env python3
"""Generate cv.pdf — one-page A4 CV for Max McWhae.
Edit the CONTENT structures below and re-run: python3 generate_cv.py
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_RIGHT
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, HRFlowable)
from reportlab.lib.styles import ParagraphStyle

INK = HexColor("#1a1a1a")
MUTE = HexColor("#555555")
RULE = HexColor("#bbbbbb")

S = {
    "name": ParagraphStyle("name", fontName="Times-Bold", fontSize=21,
                            leading=24, textColor=INK, spaceAfter=2),
    "contact": ParagraphStyle("contact", fontName="Times-Roman", fontSize=9,
                               leading=12, textColor=MUTE),
    "section": ParagraphStyle("section", fontName="Times-Bold", fontSize=10,
                               leading=12, textColor=INK, spaceBefore=10,
                               spaceAfter=2),
    "role": ParagraphStyle("role", fontName="Times-Bold", fontSize=10,
                            leading=12.5, textColor=INK),
    "date": ParagraphStyle("date", fontName="Times-Italic", fontSize=9,
                            leading=12.5, textColor=MUTE, alignment=TA_RIGHT),
    "body": ParagraphStyle("body", fontName="Times-Roman", fontSize=9.5,
                            leading=12.5, textColor=INK, spaceAfter=3),
    "profile": ParagraphStyle("profile", fontName="Times-Roman", fontSize=10,
                               leading=13.5, textColor=INK),
}

W = A4[0] - 2 * 1.7 * cm  # usable width


def rule():
    return HRFlowable(width="100%", thickness=0.6, color=RULE,
                      spaceBefore=1, spaceAfter=4)


def section(title):
    return [Paragraph(title.upper(), S["section"]), rule()]


def entry(role, date, desc=None):
    row = Table([[Paragraph(role, S["role"]), Paragraph(date, S["date"])]],
                colWidths=[W * 0.76, W * 0.24])
    row.setStyle(TableStyle([
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    out = [row]
    if desc:
        out.append(Paragraph(desc, S["body"]))
    else:
        out.append(Spacer(1, 3))
    return out


story = [
    Paragraph("Max McWhae", S["name"]),
    Paragraph("Perth, Western Australia &nbsp;·&nbsp; maxmcwhae.com &nbsp;·&nbsp; "
              "github.com/mcawezome &nbsp;·&nbsp; linkedin.com/in/max-mcwhae-1bb983102",
              S["contact"]),
    Spacer(1, 8),
    Paragraph("Technical AI safety researcher in training, focused on evaluation "
              "awareness and sandbagging in open-weight language models. Founder of "
              "the Perth AI Safety Meetup. Mathematics undergraduate at the University "
              "of Western Australia; writing code since 2002.", S["profile"]),
]

story += section("AI Safety & Research")
story += entry(
    "SANDGLASS — Independent research project", "2026 – present",
    "A pilot study of evaluation awareness and trained sandbagging in open-weight "
    "models: whether models internally represent \u201cI am being evaluated,\u201d and whether "
    "deliberate underperformance triggered by that recognition can be detected "
    "behaviourally or via linear activation probes. Developed through BlueDot "
    "Impact's Technical AI Safety project track; runs on consumer hardware; all "
    "outputs open, including negative results.")
story += entry("Founder & Organiser — Perth AI Safety Meetup", "2026 – present",
    "Founded Perth's first dedicated AI safety group. Piloted three sessions at UWA "
    "and Curtin in collaboration with EA UWA; relaunching as a monthly series at UWA.")
story += entry("Technical AI Safety course — BlueDot Impact", "2026",
    "Completed. Currently working through the ARENA curriculum (transformer "
    "internals and mechanistic interpretability).")
story += entry("Conferences", "2025 – 2026",
    "AJCAI 2025, Canberra (attended); AI Safety Forum 2026, Sydney (attended).")

story += section("Education")
story += entry("Bachelor of Mathematics — University of Western Australia",
               "2026 – present")
story += entry("Diploma of IT (Advanced Programming — Python) — North Metropolitan TAFE",
               "2025",
               "Including the AI Skill Set and Data Analysis Skill Set.")
story += entry("Certificate IV in IT (Advanced Programming) — North Metropolitan TAFE",
               "2022")
story += entry("BEng (Mining Engineering) — Curtin University", "2012 – 2016")

story += section("Experience")
story += entry("Professional Poker Player — Self-employed, Perth",
               "Jun 2025 – Mar 2026",
               "Supported myself through live cash-game play; cashed both Crown Perth "
               "monthly tournament entries (2nd and 4th).")
story += entry("Retail Assistant — ALDI, Busselton", "2023 – 2024")
story += entry("Pick & Packer / Delivery Driver — Galvin's Plumbing Supplies",
               "2019 – 2020")
story += entry("Sales & Warehouse All-rounder — YHI Power, Canning Vale", "2018")

story += section("Technical")
story.append(Paragraph(
    "Python (primary language) · PyTorch (in training via ARENA) · data analysis · "
    "Git/GitHub · local LLM tooling · Linux", S["body"]))

doc = SimpleDocTemplate("/home/claude/cv/cv.pdf", pagesize=A4,
                        leftMargin=1.7 * cm, rightMargin=1.7 * cm,
                        topMargin=1.5 * cm, bottomMargin=1.5 * cm,
                        title="Max McWhae — CV", author="Max McWhae")
doc.build(story)
print("cv.pdf written")
