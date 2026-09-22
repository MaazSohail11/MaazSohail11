"""Build self-contained profile artwork. Run with Python 3; no dependencies."""

from html import escape
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "assets"
OUT.mkdir(exist_ok=True)
INK = "#101d25"
PANEL = "#172933"
LINE = "#30464f"
WHITE = "#f3f1e7"
MUTED = "#afc0c3"
MINT = "#bdf4cf"
ORANGE = "#ffb68c"
BLUE = "#a8cfff"


def text(x, y, value, size=20, color=WHITE, weight=400, extra=""):
    return f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" font-weight="{weight}" {extra}>{escape(value)}</text>'


def rect(x, y, w, h, fill=PANEL, stroke=LINE, radius=12, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" {extra}/>'


def path(d, stroke=MINT, fill="none", width=2, extra=""):
    return f'<path d="{d}" stroke="{stroke}" fill="{fill}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round" {extra}/>'


def circle(x, y, r, fill=MINT, stroke="none"):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}"/>'


def label(x, y, value, color=MINT, size=13):
    return text(x, y, value, size, color, 600, 'font-family="Consolas, monospace" letter-spacing="2"')


def save(name, w, h, title, content):
    header = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title>
<desc id="desc">Original vector illustration for Maaz Sohail's engineering portfolio. All elements are included in this file.</desc>
<defs>
  <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M 32 0 L 0 0 0 32" fill="none" stroke="#30464f" stroke-width="0.6" opacity="0.45"/></pattern>
  <linearGradient id="fade" x1="0" x2="1"><stop stop-color="#bdf4cf"/><stop offset="1" stop-color="#a8cfff"/></linearGradient>
</defs>
<g font-family="Segoe UI, Arial, sans-serif">
'''
    base = rect(0.5, 0.5, w - 1, h - 1, INK, LINE, 20)
    (OUT / name).write_text(header + base + content + "</g></svg>\n", encoding="utf-8")


def stack(x, y, scale=1):
    """Exploded isometric software layers, joined by signal paths."""
    s = '<g transform="translate(%s %s) scale(%s)">' % (x, y, scale)
    s += '<ellipse cx="154" cy="282" rx="155" ry="46" fill="#09151c"/>'
    for offset, color in [(172, BLUE), (98, ORANGE), (24, MINT)]:
        s += path(f"M 0 {offset+67} L 152 {offset} L 305 {offset+67} L 152 {offset+136} Z", color, PANEL, 1.5)
        s += path(f"M 0 {offset+67} L 0 {offset+81} L 152 {offset+150} L 305 {offset+81} L 305 {offset+67}", LINE, INK, 1)
        s += path(f"M 152 {offset+136} V {offset+150}", color, width=1)
    s += path("M 38 130 V 272 M 268 130 V 272", MUTED, width=1, extra='stroke-dasharray="3 7"')
    s += path("M 76 94 L 152 60 L 230 94 L 152 130 Z", MINT, "#24443d")
    s += path("M 126 92 L 110 100 L 126 108 M 178 92 L 194 100 L 178 108 M 159 85 L 146 116", MINT, width=3)
    s += circle(38, 202, 4, ORANGE) + circle(268, 274, 4, BLUE)
    s += path("M 207 174 L 227 184 L 251 173", ORANGE)
    s += path("M 207 249 L 227 259 L 251 248", BLUE)
    s += '</g>'
    return s


hero = rect(614, 1, 385, 458, "url(#grid)", "none", 20)
hero += label(48, 46, "MAAZ SOHAIL / ENGINEERING & PRODUCT", size=16)
hero += circle(939, 40, 5) + circle(918, 40, 5, "#47645a") + circle(897, 40, 5, "#2c403d")
hero += text(46, 142, "Ideas into", 74, WHITE, 700, 'letter-spacing="-3"')
hero += text(46, 226, "working", 74, WHITE, 700, 'letter-spacing="-3"')
hero += text(46, 310, "systems.", 74, MINT, 700, 'letter-spacing="-3"')
hero += text(50, 354, "Useful interfaces. Thoughtful engineering.", 21, MUTED)
hero += stack(657, 87, 0.9)
hero += path("M 48 392 H 952", LINE, width=1)
hero += label(50, 427, "AI / FULL-STACK / CONNECTED HARDWARE", MINT, 13)
hero += text(950, 427, "From concept to implementation", 14, MUTED, extra='text-anchor="end"')
save("hero.svg", 1000, 460, "Maaz Sohail — Ideas into working systems", hero)

mobile = rect(1, 330, 598, 319, "url(#grid)", "none", 20)
mobile += label(32, 43, "MAAZ SOHAIL", MINT, 18)
mobile += text(30, 119, "Ideas into", 64, WHITE, 700, 'letter-spacing="-2"')
mobile += text(30, 193, "working systems.", 64, MINT, 700, 'letter-spacing="-2"')
mobile += text(32, 244, "Useful interfaces.", 25, MUTED)
mobile += text(32, 281, "Thoughtful engineering.", 25, MUTED)
mobile += stack(175, 301, 0.9)
mobile += label(32, 608, "AI / SOFTWARE / HARDWARE", MINT, 17)
save("hero-mobile.svg", 600, 650, "Maaz Sohail — Ideas into working systems", mobile)


def cover_base(kicker, title, subtitle, accent):
    s = rect(475, 1, 524, 278, "url(#grid)", "none", 20)
    s += label(36, 46, kicker, accent)
    s += text(34, 112, title, 46, WHITE, 650, 'letter-spacing="-1"')
    s += text(36, 155, subtitle, 20, MUTED)
    return s


pdf = cover_base("01 / DOCUMENT TOOLS", "PDF Free Editor", "Less friction. More getting things done.", MINT)
pdf += rect(36, 202, 94, 36, "#264037", "none", 18) + text(83, 226, "EDIT", 14, MINT, 600, 'text-anchor="middle"')
pdf += rect(140, 202, 94, 36, "#264037", "none", 18) + text(187, 226, "SIGN", 14, MINT, 600, 'text-anchor="middle"')
pdf += rect(244, 202, 110, 36, "#264037", "none", 18) + text(299, 226, "EXPORT", 14, MINT, 600, 'text-anchor="middle"')
pdf += rect(545, 29, 401, 222, "#14232b", LINE, 12)
pdf += path("M 545 61 H 946", LINE, width=1)
for cx in (562, 576, 590):
    pdf += circle(cx, 45, 3, MUTED)
pdf += rect(565, 81, 56, 149, INK, LINE, 6)
for y, letter in ((109, "T"), (151, "+"), (197, "/")):
    pdf += text(593, y, letter, 23, MINT, 600, 'text-anchor="middle"')
pdf += rect(647, 78, 174, 156, WHITE, "none", 4)
pdf += label(663, 107, "DOCUMENT", "#37594a", 10)
for y, w in ((122, 125), (134, 104), (146, 115)):
    pdf += rect(663, y, w, 4, "#b4c5bb", "none", 2)
pdf += rect(659, 166, 148, 42, "none", "#579776", 2)
pdf += path("M 668 196 Q 685 175 677 192 Q 674 203 697 185 Q 703 181 698 195 Q 708 183 712 194 Q 725 184 735 190 L 780 190", "#37594a", width=2)
pdf += rect(843, 112, 74, 74, MINT, "none", 18)
pdf += path("M 864 149 L 876 161 L 898 136", "#24443d", width=4)
save("pdf-editor.svg", 1000, 280, "PDF Free Editor — Edit, sign, export", pdf)

temp = cover_base("02 / FILE SHARING", "Tempload", "Share the file. Skip the sign-up.", BLUE)
temp += label(36, 228, "UPLOAD  /  SHARE  /  EXPIRE", BLUE, 15)
temp += path("M 648 140 H 749 M 823 140 H 919", BLUE, width=2, extra='stroke-dasharray="5 7"')
temp += rect(546, 71, 110, 142, "#213a4b", "#547c97", 12)
temp += path("M 577 99 H 611 L 626 114 V 175 H 577 Z M 611 99 V 114 H 626", BLUE)
temp += path("M 601 161 V 129 M 589 141 L 601 129 L 613 141", BLUE, width=3)
temp += circle(773, 140, 52, "#203b42", "#547c97")
temp += rect(749, 132, 48, 36, BLUE, "none", 8)
temp += path("M 758 132 V 117 Q 773 95 788 117 V 132", BLUE, width=4)
temp += circle(773, 146, 4, INK) + path("M 773 146 V 154", INK)
temp += circle(918, 140, 31, INK, BLUE)
temp += path("M 918 122 V 140 L 932 149", BLUE, width=3)
temp += label(738, 229, "PIN-GATED", BLUE, 11) + label(881, 199, "EXPIRY", BLUE, 10)
save("tempload.svg", 1000, 280, "Tempload — Temporary, PIN-gated file sharing", temp)


def node(x, title, sub, accent):
    s = rect(x, 96, 198, 130, PANEL, LINE, 10)
    s += circle(x + 27, 123, 5, accent)
    s += text(x + 20, 161, title, 20, WHITE, 600)
    s += text(x + 20, 191, sub, 16, MUTED)
    return s


med = label(32, 42, "SYSTEM STUDY / MEDIGUARD", MINT)
med += text(968, 42, "Evidence → reasoning → explanation", 17, MUTED, extra='text-anchor="end"')
med += path("M 230 161 H 275 M 475 161 H 521 M 721 161 H 768", MINT)
for x in (264, 510, 757):
    med += path(f"M {x} 156 L {x+7} 161 L {x} 166", MINT)
med += node(32, "Label evidence", "FDA drug-label data", MINT)
med += node(278, "Vector retrieval", "MiniLM + ChromaDB", MINT)
med += node(524, "Hybrid reasoning", "Rules + Random Forest", ORANGE)
med += node(770, "Explanation", "Source-linked output", BLUE)
save("mediguard.svg", 1000, 256, "MediGuard — Evidence, retrieval, reasoning, explanation", med)

drow = label(32, 42, "SYSTEM STUDY / DROWSINESS DETECTION", ORANGE)
drow += text(968, 42, "Pixels → decisions → physical output", 17, MUTED, extra='text-anchor="end"')
for x in (32, 278, 524, 770):
    drow += rect(x, 81, 198, 158)
drow += path("M 230 160 H 278 M 476 160 H 524 M 722 160 H 770", ORANGE, width=2, extra='stroke-dasharray="4 6"')
drow += rect(52, 100, 56, 38, "none", ORANGE, 8) + circle(80, 119, 10, "none", ORANGE)
drow += text(52, 180, "Capture", 24, WHITE, 600) + text(52, 211, "OpenCV frames", 17, MUTED)
drow += path("M 300 119 Q 330 85 360 119 Q 330 152 300 119", MINT) + circle(330, 119, 10, "none", MINT)
drow += text(298, 180, "Measure", 24, WHITE, 600) + text(298, 211, "MediaPipe landmarks", 16, MUTED)
drow += path("M 544 123 H 555 L 566 106 L 579 134 L 591 111 L 603 123 H 614", BLUE)
drow += text(544, 180, "Decide", 24, WHITE, 600) + text(544, 211, "Eye ratio + duration", 17, MUTED)
drow += rect(792, 99, 42, 42, "none", ORANGE, 4)
for x in range(798, 831, 10):
    drow += path(f"M {x} 93 V 99 M {x} 141 V 147", ORANGE)
drow += text(790, 180, "Act", 24, WHITE, 600) + text(790, 211, "ESP32 + notifications", 16, MUTED)
save("drowsiness.svg", 1000, 268, "Drowsiness Detection — Capture, measure, decide, act", drow)

for name, title, accent, content in (
    ("pdf-editor", "PDF Free Editor", MINT, pdf),
    ("tempload", "Tempload", BLUE, temp),
):
    # Recompose the original vector art; no raster screenshots or remote assets.
    compact = label(28, 37, "PRODUCT / " + title.upper(), accent, 15)
    compact += text(28, 95, title, 42, WHITE, 650)
    compact += '<svg x="24" y="123" width="552" height="280" viewBox="525 15 440 250">' + content + '</svg>'
    save(name + "-mobile.svg", 600, 430, title, compact)

for name, title, accent, steps in (
    ("mediguard", "MEDIGUARD", MINT, [
        ("Label evidence", "FDA drug-label data"),
        ("Vector retrieval", "MiniLM + ChromaDB"),
        ("Hybrid reasoning", "Rules + Random Forest"),
        ("Explanation", "Source-linked output"),
    ]),
    ("drowsiness", "DROWSINESS DETECTION", ORANGE, [
        ("Capture", "OpenCV camera frames"),
        ("Measure", "MediaPipe landmarks"),
        ("Decide", "Eye ratio + duration"),
        ("Act", "ESP32 + notifications"),
    ]),
):
    compact = label(28, 39, "SYSTEM / " + title, accent, 15)
    for index, (heading, sub) in enumerate(steps):
        y = 67 + index * 109
        compact += rect(28, y, 544, 91)
        compact += text(50, y + 55, f"0{index + 1}", 29, accent, 600)
        compact += text(114, y + 37, heading, 26, WHITE, 600)
        compact += text(114, y + 67, sub, 21, MUTED)
        if index < 3:
            compact += path(f"M 71 {y+91} V {y+109}", accent)
    save(name + "-mobile.svg", 600, 512, title, compact)

footer = text(32, 57, "Build thoughtfully. Make it useful.", 28, MINT, 600)
footer += label(966, 55, "MAAZ SOHAIL", MUTED, 13).replace('letter-spacing="2"', 'letter-spacing="2" text-anchor="end"')
save("footer.svg", 1000, 96, "Build thoughtfully. Make it useful. — Maaz Sohail", footer)
print(f"Built 11 SVG assets in {OUT}")
