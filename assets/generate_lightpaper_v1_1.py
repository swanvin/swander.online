from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

c = canvas.Canvas("SWANDER_Lightpaper_v1.1.pdf", pagesize=letter)
width, height = letter

# --- Background ---
c.setFillColor(HexColor("#0c0c0f"))
c.rect(0, 0, width, height, stroke=0, fill=1)

# --- Title ---
c.setFont("Helvetica-Bold", 26)
c.setFillColor(HexColor("#bfa8ff"))
c.drawCentredString(width/2, height - 1.2*inch, "SWANDER LIGHTPAPER v1.1")
c.setFont("Helvetica", 14)
c.setFillColor(HexColor("#cccccc"))
c.drawCentredString(width/2, height - 1.6*inch, "Federation Edition")

# --- Body text helper ---
def textblock(y, title, body):
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(HexColor("#bfa8ff"))
    c.drawString(1*inch, y, title)
    c.setFont("Helvetica", 11)
    c.setFillColor(HexColor("#dddddd"))
    text = c.beginText(1*inch, y - 0.25*inch)
    text.setLeading(15)
    text.textLines(body)
    c.drawText(text)
    return y - (0.25 + 0.18*len(body.splitlines()))*inch

# --- Sections ---
y = height - 2.3*inch

y = textblock(y, "Overview",
"""SWANDER ($SWND) is the meme-federation of humor, motion, and unity built on Solana.
It represents a collective of creators and dreamers who believe that laughter can fuel
innovation and that motion is the purest form of progress.""")

y = textblock(y, "Origin & Philosophy",
"""Born from the Swan Labs movement, SWANDER emerged as a flight toward decentralized joy.
It carries the grace of a swan and the boldness of a meme, celebrating creativity in motion.""")

y = textblock(y, "Tokenomics ($SWND)",
"""• 50%  – Community & Rewards
• 25%  – Liquidity & Treasury
• 15%  – Development & Federation Growth
• 10%  – Initial Burn & Fair Launch

$SWND serves as both a symbol and a currency for federation governance and creativity.""")

y = textblock(y, "Federation Vision & Governance",
"""The SWANDER Federation unites holders as citizens of a decentralized culture.
Its governance encourages transparency, humor, and collective intelligence,
ensuring decisions are made with both heart and motion.""")

y = textblock(y, "Flightpath 2025 → 2026",
"""Phase 1 – Meme to Motion (Community Ignition)
Phase 2 – Liquidity & Lightpaper Launch
Phase 3 – Federation Tools & DAO Integration
Phase 4 – Global Collaborations & Creative Expansions
Phase 5 – Cross-Chain Flight (Interoperability Deployment)""")

y = textblock(y, "Contact",
"""Website: https://swander.online
Email: contact@swander.online""")

# --- Footer ---
c.setFont("Helvetica", 9)
c.setFillColor(HexColor("#777777"))
c.drawCentredString(width/2, 0.6*inch, "© 2025 SWANDER – All Rights Reserved")

c.showPage()
c.save()
print("SWANDER_Lightpaper_v1.1.pdf created successfully.")
