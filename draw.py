"""Draw the 21 November 2026 news image with Pillow (local build tool only).

The submitted program is main.ts, which only copies entry.png.
This script is how entry.png was made, so the picture is reproducible
from the same six verified stories. Run: python3 draw.py
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 232)
INK = (20, 20, 20)
RED = (178, 34, 34)
BLUE = (24, 68, 128)
GREEN = (34, 120, 70)
GOLD = (176, 128, 20)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)
d.rectangle([0, 0, W, 10], fill=INK)

# Header
d.text((32, 28), "THE WORLD IN ONE DAY", font=font(BOLD, 26), fill=RED)
d.text((32, 62), "SATURDAY 21 NOVEMBER 2026", font=font(SERIF, 54), fill=INK)
d.rectangle([32, 138, 992, 144], fill=RED)
d.text(
    (32, 156),
    "Tankers hit in Hormuz  •  Markets in correction",
    font=font(BOLD, 24),
    fill=INK,
)
d.text(
    (32, 188),
    "UK-EU reset  •  Cyberattacks  •  COP31 stalls",
    font=font(BOLD, 24),
    fill=INK,
)

stories = [
    ("TANKERS HIT  •  STRAIT OF HORMUZ", "Two tankers hit by unknown projectiles near Oman",
     "UK maritime agency reports strikes off Khasab; no casualties.", RED),
    ("MARKETS FALL  •  NEW YORK", "S&P 500 enters correction as AI sell-off spreads",
     "Nasdaq falls 5.3%; Nikkei down 5.1%; Nvidia drops 14%.", RED),
    ("UK-EU RESET  •  BRUSSELS", "UK and EU sign three post-Brexit deals",
     "Food trade, carbon markets, youth mobility for 100,000 a year.", BLUE),
    ("CYBERATTACKS  •  WASHINGTON", "FBI probes breach of national crime database",
     "Hackers also hit the USDA system that pays farmers.", INK),
    ("COP31 STALLS  •  ANTALYA", "Climate talks run past deadline without a deal",
     "Draft drops the promise to move away from fossil fuels.", GOLD),
    ("CANCER HOPE  •  BARCELONA", "Pill makes pancreatic tumours vanish in 1 in 12",
     "Daraxonrasib plus chemo shrank tumours in 60.7% of patients.", GREEN),
]

# Six panels: 2 columns x 3 rows
x0, y0, pw, ph, gap = 32, 232, 474, 240, 12
for i, (kicker, head, body, colour) in enumerate(stories):
    x = x0 + (i % 2) * (pw + gap)
    y = y0 + (i // 2) * (ph + gap)
    d.rectangle([x, y, x + pw, y + ph], fill=(255, 255, 255),
                outline=(200, 190, 170), width=2)
    d.rectangle([x, y, x + 10, y + ph], fill=colour)
    d.text((x + 26, y + 16), kicker, font=font(BOLD, 19), fill=colour)
    lines = wrap(d, head, font(BOLD, 27), pw - 52)
    yy = y + 48
    for line in lines[:3]:
        d.text((x + 26, yy), line, font=font(BOLD, 27), fill=INK)
        yy += 34
    blines = wrap(d, body, font(REG, 20), pw - 52)
    for line in blines[:2]:
        d.text((x + 26, yy + 6), line, font=font(REG, 20), fill=(70, 70, 70))
        yy += 26

# Footer
d.rectangle([32, 976, 992, 980], fill=INK)
d.text((32, 988), "21 NOVEMBER 2026  —  SIX STORIES, ONE DAY",
       font=font(BOLD, 20), fill=INK)

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
