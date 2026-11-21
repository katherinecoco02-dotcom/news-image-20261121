"""Build entry.png for the 21 November 2026 news image.

Runs locally with Pillow only. The entry program (main.ts) just copies
the finished picture, so this script is the reproducible source of it.
Usage: python3 draw.py
"""
from PIL import Image, ImageDraw, ImageFont

PAGE_W, PAGE_H = 1024, 1024
BG = (247, 243, 232)
BLACK = (20, 20, 20)
CRIMSON = (178, 34, 34)
NAVY = (24, 68, 128)
LEAF = (34, 120, 70)
OCHRE = (176, 128, 20)
GREY = (70, 70, 70)
CARD_EDGE = (200, 190, 170)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
SANS_BOLD = FONT_DIR + "DejaVuSans-Bold.ttf"
SANS = FONT_DIR + "DejaVuSans.ttf"
SERIF_BOLD = FONT_DIR + "DejaVuSerif-Bold.ttf"


def load_font(name, size):
    return ImageFont.truetype(name, size)


def split_lines(canvas, txt, fnt, width):
    out, current = [], ""
    for word in txt.split():
        candidate = (current + " " + word).strip()
        if canvas.textlength(candidate, font=fnt) <= width:
            current = candidate
        else:
            out.append(current)
            current = word
    if current:
        out.append(current)
    return out


def draw_panel(canvas, left, top, width, height, kicker, headline, body, accent):
    canvas.rectangle([left, top, left + width, top + height],
                     fill=(255, 255, 255), outline=CARD_EDGE, width=2)
    canvas.rectangle([left, top, left + 10, top + height], fill=accent)
    canvas.text((left + 26, top + 16), kicker,
                font=load_font(SANS_BOLD, 19), fill=accent)
    head_lines = split_lines(canvas, headline, load_font(SANS_BOLD, 27), width - 52)
    cursor = top + 48
    for row in head_lines[:3]:
        canvas.text((left + 26, cursor), row, font=load_font(SANS_BOLD, 27), fill=BLACK)
        cursor += 34
    body_lines = split_lines(canvas, body, load_font(SANS, 20), width - 52)
    for row in body_lines[:2]:
        canvas.text((left + 26, cursor + 6), row, font=load_font(SANS, 20), fill=GREY)
        cursor += 26


def main():
    page = Image.new("RGB", (PAGE_W, PAGE_H), BG)
    canvas = ImageDraw.Draw(page)
    canvas.rectangle([0, 0, PAGE_W, 10], fill=BLACK)

    canvas.text((32, 28), "THE WORLD IN ONE DAY",
                font=load_font(SANS_BOLD, 26), fill=CRIMSON)
    canvas.text((32, 62), "SATURDAY 21 NOVEMBER 2026",
                font=load_font(SERIF_BOLD, 54), fill=BLACK)
    canvas.rectangle([32, 138, 992, 144], fill=CRIMSON)
    canvas.text((32, 156), "Tankers hit in Hormuz  •  Markets in correction",
                font=load_font(SANS_BOLD, 24), fill=BLACK)
    canvas.text((32, 188), "UK-EU reset  •  Cyberattacks  •  COP31 stalls",
                font=load_font(SANS_BOLD, 24), fill=BLACK)

    items = [
        dict(kicker="TANKERS HIT  •  STRAIT OF HORMUZ",
             headline="Two tankers hit by unknown projectiles near Oman",
             body="UK maritime agency reports strikes off Khasab; no casualties.",
             accent=CRIMSON),
        dict(kicker="MARKETS FALL  •  NEW YORK",
             headline="S&P 500 enters correction as AI sell-off spreads",
             body="Nasdaq falls 5.3%; Nikkei down 5.1%; Nvidia drops 14%.",
             accent=CRIMSON),
        dict(kicker="UK-EU RESET  •  BRUSSELS",
             headline="UK and EU sign three post-Brexit deals",
             body="Food trade, carbon markets, youth mobility for 100,000 a year.",
             accent=NAVY),
        dict(kicker="CYBERATTACKS  •  WASHINGTON",
             headline="FBI probes breach of national crime database",
             body="Hackers also hit the USDA system that pays farmers.",
             accent=BLACK),
        dict(kicker="COP31 STALLS  •  ANTALYA",
             headline="Climate talks run past deadline without a deal",
             body="Draft drops the promise to move away from fossil fuels.",
             accent=OCHRE),
        dict(kicker="CANCER HOPE  •  BARCELONA",
             headline="Pill makes pancreatic tumours vanish in 1 in 12",
             body="Daraxonrasib plus chemo shrank tumours in 60.7% of patients.",
             accent=LEAF),
    ]

    panel_w, panel_h, gap = 474, 240, 12
    for idx, item in enumerate(items):
        px = 32 + (idx % 2) * (panel_w + gap)
        py = 232 + (idx // 2) * (panel_h + gap)
        draw_panel(canvas, px, py, panel_w, panel_h,
                   item["kicker"], item["headline"], item["body"], item["accent"])

    canvas.rectangle([32, 976, 992, 980], fill=BLACK)
    canvas.text((32, 988), "21 NOVEMBER 2026  —  SIX STORIES, ONE DAY",
                font=load_font(SANS_BOLD, 20), fill=BLACK)
    page.save("entry.png", optimize=True)
    print("saved entry.png", page.size)


if __name__ == "__main__":
    main()
