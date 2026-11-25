"""Hand-drawn flat SVG illustrations, one per story. Original vector work, no photos."""

INK = "#22252b"
SKY = "#dfe8f0"
PAPER = "#f6f1e6"


def lead(kind, badge):
    """320x130 scene for a lead story."""
    body = LEAD_ART[kind]()
    return (f'<svg viewBox="0 8 320 106" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg"><g transform="translate(0,-6)">{body}</g>'
            f'{_badge(badge, 316, 12, 14, "end")}</svg>')


def panel(kind, badge):
    """240x60 scene for a smaller story."""
    body = PANEL_ART[kind]()
    return (f'<svg viewBox="0 6 240 48" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg">{body}'
            f'{_badge(badge, 236, 9, 10.5, "end")}</svg>')


def _badge(text, x, y, size, anchor):
    w = len(text) * size * 0.62 + size * 0.9
    bx = x - w if anchor == "end" else x
    h = size * 1.45
    return (f'<rect x="{bx:.1f}" y="{y}" width="{w:.1f}" height="{h:.1f}" rx="2" fill="#b3202a"/>'
            f'<text x="{bx + w / 2:.1f}" y="{y + h * 0.74:.1f}" text-anchor="middle" '
            f'font-family="Avenir Next Condensed, Helvetica Neue, Arial" font-weight="700" '
            f'font-size="{size}" fill="#fff" letter-spacing=".3">{text}</text>')


# ---------------------------------------------------------------- leads

def _court():
    s = f'<rect width="320" height="130" fill="#e9e4d8"/>'
    # courthouse
    s += f'<polygon points="30,48 125,18 220,48" fill="#c9c2b2" stroke="{INK}" stroke-width="2"/>'
    s += f'<rect x="38" y="48" width="174" height="8" fill="#bdb5a3" stroke="{INK}" stroke-width="2"/>'
    for i in range(6):
        x = 48 + i * 29
        s += f'<rect x="{x}" y="58" width="12" height="52" fill="#d8d2c4" stroke="{INK}" stroke-width="1.5"/>'
    s += f'<rect x="30" y="110" width="190" height="10" fill="#bdb5a3" stroke="{INK}" stroke-width="2"/>'
    s += f'<text x="125" y="44" text-anchor="middle" font-family="Georgia" font-size="7.5" font-weight="700" fill="{INK}">U.S. DISTRICT COURT · E.D.N.Y.</text>'
    # gavel
    s += f'<g transform="translate(252,78) rotate(-35)"><rect x="-26" y="-11" width="52" height="22" rx="3" fill="#7b4a26" stroke="{INK}" stroke-width="2"/>'
    s += f'<rect x="-30" y="-13" width="7" height="26" rx="2" fill="#5e3517" stroke="{INK}" stroke-width="1.5"/>'
    s += f'<rect x="23" y="-13" width="7" height="26" rx="2" fill="#5e3517" stroke="{INK}" stroke-width="1.5"/>'
    s += f'<rect x="-4" y="11" width="8" height="52" rx="3" fill="#8d5a32" stroke="{INK}" stroke-width="1.5"/></g>'
    s += f'<rect x="232" y="112" width="70" height="10" rx="3" fill="#5e3517" stroke="{INK}" stroke-width="1.5"/>'
    # chip with logo-free flower petals, labelled
    s += f'<rect x="246" y="44" width="34" height="26" rx="2" fill="#2d3340" stroke="{INK}" stroke-width="1.5"/>'
    for i in range(5):
        s += f'<line x1="{250 + i * 6.5}" y1="39" x2="{250 + i * 6.5}" y2="44" stroke="{INK}" stroke-width="1.5"/>'
        s += f'<line x1="{250 + i * 6.5}" y1="70" x2="{250 + i * 6.5}" y2="75" stroke="{INK}" stroke-width="1.5"/>'
    s += f'<text x="263" y="61" text-anchor="middle" font-family="Avenir Next Condensed, Arial" font-weight="700" font-size="9" fill="#fff">HUAWEI</text>'
    return s


def _shanghai():
    s = '<rect width="320" height="130" fill="#f0e3df"/>'
    s += '<rect y="104" width="320" height="26" fill="#9fb6c8"/>'
    # skyline
    bl = [(10, 70, 26), (40, 58, 22), (66, 80, 18), (150, 64, 24), (180, 50, 20), (206, 74, 22), (232, 60, 18)]
    for x, y, w in bl:
        s += f'<rect x="{x}" y="{y}" width="{w}" height="{104 - y}" fill="#b9b0b8" stroke="{INK}" stroke-width="1.5"/>'
    # Oriental Pearl style tower
    s += f'<line x1="118" y1="8" x2="118" y2="104" stroke="{INK}" stroke-width="3"/>'
    s += f'<circle cx="118" cy="40" r="11" fill="#c8434a" stroke="{INK}" stroke-width="2"/>'
    s += f'<circle cx="118" cy="80" r="15" fill="#c8434a" stroke="{INK}" stroke-width="2"/>'
    s += f'<polygon points="104,104 112,86 124,86 132,104" fill="#b9b0b8" stroke="{INK}" stroke-width="1.5"/>'
    # tapered tower (Shanghai Tower)
    s += f'<path d="M86 104 L90 22 Q96 14 102 22 L104 104 Z" fill="#a9b8c6" stroke="{INK}" stroke-width="1.5"/>'
    # dossier + magnifier
    s += f'<rect x="186" y="40" width="96" height="58" rx="3" fill="#fbf7ef" stroke="{INK}" stroke-width="2" transform="rotate(-6 236 66)"/>'
    s += f'<g transform="rotate(-6 236 66)"><text x="234" y="60" text-anchor="middle" font-family="Georgia" font-weight="700" font-size="12" fill="{INK}">CHEN JINING</text>'
    s += f'<text x="234" y="73" text-anchor="middle" font-family="Avenir Next Condensed, Arial" font-size="8.5" fill="{INK}">POLITBURO · SHANGHAI</text>'
    s += '<rect x="203" y="79" width="62" height="13" fill="none" stroke="#b3202a" stroke-width="1.8"/>'
    s += '<text x="234" y="89" text-anchor="middle" font-family="Avenir Next Condensed, Arial" font-weight="700" font-size="8" fill="#b3202a">UNDER PROBE</text></g>'
    s += f'<circle cx="290" cy="92" r="15" fill="#ffffff66" stroke="{INK}" stroke-width="4"/>'
    s += f'<line x1="300" y1="103" x2="314" y2="118" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>'
    return s


def _riyadh():
    s = '<rect width="320" height="130" fill="#f3e6cf"/>'
    s += '<rect y="108" width="320" height="22" fill="#d9c49d"/>'
    for x, h, w in [(14, 40, 30), (50, 56, 26), (196, 46, 28), (230, 34, 34), (270, 52, 30)]:
        s += f'<rect x="{x}" y="{108 - h}" width="{w}" height="{h}" fill="#d8cbb2" stroke="{INK}" stroke-width="1.5"/>'
    # PIF tower: tall tapering glass tower
    s += f'<path d="M110 108 L118 14 L140 8 L150 108 Z" fill="#7d93a8" stroke="{INK}" stroke-width="2"/>'
    for y in range(22, 104, 9):
        s += f'<line x1="{118 - (y - 14) * 0.085:.1f}" y1="{y}" x2="{140 + (y - 8) * 0.1:.1f}" y2="{y}" stroke="#5c7186" stroke-width="1"/>'
    # impact + smoke
    s += '<circle cx="138" cy="46" r="9" fill="#f2a33a"/><circle cx="138" cy="46" r="5" fill="#fbe27a"/>'
    s += '<path d="M140 40 C150 30 160 34 168 22 C176 14 190 18 196 8" stroke="#6b6b6b" stroke-width="9" fill="none" stroke-linecap="round" opacity=".55"/>'
    # drone
    s += f'<g transform="translate(226,62) rotate(-18)"><path d="M-26 0 L18 -4 L26 0 L18 4 Z" fill="#555c66" stroke="{INK}" stroke-width="1.5"/>'
    s += f'<path d="M-4 -2 L-14 -16 L-6 -16 L6 -2 Z M-4 2 L-14 16 L-6 16 L6 2 Z" fill="#555c66" stroke="{INK}" stroke-width="1.2"/></g>'
    s += '<path d="M200 70 L150 46" stroke="#8a8a8a" stroke-width="1.5" stroke-dasharray="4 3"/>'
    s += f'<text x="130" y="116" text-anchor="middle" font-family="Avenir Next Condensed, Arial" font-weight="700" font-size="9" fill="{INK}">PIF TOWER · KAFD</text>'
    return s


LEAD_ART = {"court": _court, "shanghai": _shanghai, "riyadh": _riyadh}


# ---------------------------------------------------------------- panels

def _bg(c):
    return f'<rect width="240" height="60" fill="{c}"/>'


def _zap():
    s = _bg("#2b3550")
    s += '<circle cx="30" cy="16" r="6" fill="#e9e2b8"/>'
    s += f'<rect x="80" y="14" width="80" height="46" fill="#8f96a3" stroke="{INK}" stroke-width="1.5"/>'
    for r in range(4):
        for c in range(6):
            col = "#f2c46b" if (r + c) % 4 == 0 else "#3a4256"
            s += f'<rect x="{86 + c * 12.5}" y="{19 + r * 10}" width="7" height="6" fill="{col}"/>'
    s += '<polygon points="130,14 160,14 160,40 150,30 142,36 136,22" fill="#2b3550"/>'
    s += '<path d="M146 14 C150 4 160 6 166 0" stroke="#9aa0a8" stroke-width="6" fill="none" opacity=".7"/>'
    s += '<path d="M140 18 l6 -8 l4 6 l5 -9 l3 11 z" fill="#f08a2a"/>'
    s += '<rect x="20" y="40" width="40" height="20" fill="#6d7482"/><rect x="176" y="34" width="44" height="26" fill="#6d7482"/>'
    return s


def _gaza():
    s = _bg("#e9dcc4")
    s += '<rect y="48" width="240" height="12" fill="#c4ae86"/>'
    # damaged multi-storey block
    s += f'<path d="M60 48 V18 H104 V26 L112 30 L106 38 L114 48 Z" fill="#cdbfa3" stroke="{INK}" stroke-width="1.3"/>'
    for r in range(3):
        for c in range(4):
            s += f'<rect x="{66 + c * 9}" y="{22 + r * 8}" width="5" height="5" fill="#5b5346"/>'
    s += '<path d="M106 44 l8 4 h-20 z M116 48 l10 -6 l6 6 z" fill="#a8977a"/>'
    # strike flash and smoke column
    s += '<circle cx="104" cy="26" r="6" fill="#f2a33a"/><circle cx="104" cy="26" r="3" fill="#fbe27a"/>'
    s += '<path d="M106 22 C114 12 108 6 120 -2" stroke="#6f6f6f" stroke-width="10" fill="none" opacity=".5" stroke-linecap="round"/>'
    # jet overhead
    s += '<g transform="translate(176,18)"><path d="M-14 0 L12 -2 L16 0 L12 2 Z" fill="#59606b"/><path d="M-2 -1 L-8 -9 L-3 -9 L4 -1 Z M-2 1 L-8 9 L-3 9 L4 1 Z" fill="#59606b"/></g>'
    s += '<rect x="150" y="32" width="40" height="16" fill="#d6c9ae" stroke="#22252b" stroke-width="1.1"/>'
    return s


def _tanker():
    s = _bg("#cfe0ea")
    s += '<rect y="40" width="240" height="20" fill="#3f6f8f"/>'
    s += f'<path d="M30 40 L44 52 L150 52 L160 40 Z" fill="#8a2f2a" stroke="{INK}" stroke-width="1.5"/>'
    s += f'<rect x="40" y="32" width="110" height="8" fill="#3a3f47" stroke="{INK}" stroke-width="1.2"/>'
    s += f'<rect x="130" y="20" width="16" height="12" fill="#eee" stroke="{INK}" stroke-width="1.2"/>'
    s += '<path d="M70 32 q6 -14 12 -4 q4 -12 10 0 q4 -8 8 2 z" fill="#f08a2a"/>'
    s += '<path d="M84 22 C90 10 100 14 108 2" stroke="#555" stroke-width="7" fill="none" opacity=".55"/>'
    s += f'<circle cx="190" cy="50" r="6" fill="#2a2d33"/>'
    for a in range(0, 360, 45):
        import math
        x, y = 190 + 9 * math.cos(math.radians(a)), 50 + 9 * math.sin(math.radians(a))
        s += f'<line x1="190" y1="50" x2="{x:.1f}" y2="{y:.1f}" stroke="#2a2d33" stroke-width="1.5"/>'
    return s


def _pill():
    s = _bg("#ece6f4")
    s += f'<g transform="translate(70,32) rotate(-25)"><rect x="-38" y="-12" width="76" height="24" rx="12" fill="#ffffff" stroke="{INK}" stroke-width="1.6"/>'
    s += f'<path d="M0 -12 H26 A12 12 0 0 1 26 12 H0 Z" fill="#6c4ab0" stroke="{INK}" stroke-width="1.6"/></g>'
    s += f'<path d="M140 50 L148 18 H164 L172 50 Z" fill="#cfe6f2" stroke="{INK}" stroke-width="1.5"/>'
    s += '<path d="M143 40 H169 L172 50 H140 Z" fill="#7fb7d6"/>'
    s += f'<rect x="146" y="12" width="20" height="6" fill="#ddd" stroke="{INK}" stroke-width="1.2"/>'
    return s


def _trophy():
    s = _bg("#eef3e6")
    # Senegal flag
    s += f'<rect x="20" y="14" width="22" height="34" fill="#2e8b3c"/><rect x="42" y="14" width="22" height="34" fill="#f5d33b"/><rect x="64" y="14" width="22" height="34" fill="#d1312e"/>'
    s += '<polygon points="53,25 55.5,31 62,31 57,35 59,41 53,37 47,41 49,35 44,31 50.5,31" fill="#2e8b3c"/>'
    s += f'<rect x="20" y="14" width="66" height="34" fill="none" stroke="{INK}" stroke-width="1.2"/>'
    # trophy
    s += f'<path d="M110 10 H140 V22 Q140 36 125 38 Q110 36 110 22 Z" fill="#e0b030" stroke="{INK}" stroke-width="1.5"/>'
    s += f'<path d="M110 14 Q100 14 102 22 Q104 28 111 28 M140 14 Q150 14 148 22 Q146 28 139 28" fill="none" stroke="{INK}" stroke-width="1.5"/>'
    s += f'<rect x="121" y="38" width="8" height="8" fill="#e0b030" stroke="{INK}" stroke-width="1.2"/>'
    s += f'<rect x="112" y="46" width="26" height="8" fill="#7b4a26" stroke="{INK}" stroke-width="1.2"/>'
    s += f'<text x="160" y="46" font-family="Georgia" font-weight="700" font-size="15" fill="{INK}">1–0</text>'
    return s


def _rally():
    s = _bg("#e8f1ea")
    pts = "14,50 40,46 60,48 84,40 104,42 128,30 150,28 176,14"
    s += f'<polyline points="{pts}" fill="none" stroke="#1d8a4a" stroke-width="3"/>'
    s += '<polygon points="176,14 168,13 173,21" fill="#1d8a4a"/>'
    s += f'<rect x="190" y="30" width="34" height="24" rx="2" fill="#2d3340" stroke="{INK}" stroke-width="1.2"/>'
    for i in range(4):
        s += f'<line x1="{195 + i * 8}" y1="26" x2="{195 + i * 8}" y2="30" stroke="{INK}" stroke-width="1.2"/>'
    return s


def _dow():
    s = _bg("#1f2733")
    s += '<line x1="10" y1="30" x2="230" y2="30" stroke="#596579" stroke-dasharray="3 3"/>'
    s += '<polyline points="10,44 40,40 70,36 100,34 130,30 160,26" fill="none" stroke="#45c47a" stroke-width="3"/>'
    s += '<polyline points="10,22 50,24 90,30 130,40 160,48" fill="none" stroke="#e2574c" stroke-width="2.4"/>'
    s += '<text x="150" y="40" font-family="Avenir Next Condensed, Arial" font-weight="700" font-size="9" fill="#45c47a">DOW ▲</text>'
    s += '<text x="166" y="50" font-family="Avenir Next Condensed, Arial" font-weight="700" font-size="9" fill="#e2574c">NASDAQ −1.5%</text>'
    return s


def _jets():
    s = _bg("#d9e6f2")
    s += '<rect y="44" width="240" height="16" fill="#5d8fb8"/>'
    s += '<ellipse cx="170" cy="46" rx="26" ry="6" fill="#6b8f58" stroke="#22252b" stroke-width="1"/>'
    for (x, y) in [(40, 22), (78, 32), (60, 12)]:
        s += f'<g transform="translate({x},{y})"><path d="M-14 0 L12 -2 L16 0 L12 2 Z" fill="#59606b"/><path d="M-2 -1 L-8 -9 L-3 -9 L4 -1 Z M-2 1 L-8 9 L-3 9 L4 1 Z" fill="#59606b"/><path d="M-14 0 L-18 -5 L-15 -5 L-11 -1 Z" fill="#59606b"/></g>'
    s += '<path d="M150 30 q20 -14 40 0" fill="none" stroke="#b3202a" stroke-width="1.6"/><path d="M144 24 q26 -20 52 0" fill="none" stroke="#b3202a" stroke-width="1.6"/>'
    return s


def _heat():
    s = _bg("#fbeee0")
    s += '<circle cx="190" cy="34" r="12" fill="#f4b23a"/>'
    for i in range(8):
        import math
        a = math.radians(i * 45)
        s += f'<line x1="{190 + 16 * math.cos(a):.1f}" y1="{34 + 16 * math.sin(a):.1f}" x2="{190 + 22 * math.cos(a):.1f}" y2="{34 + 22 * math.sin(a):.1f}" stroke="#f4b23a" stroke-width="2.4"/>'
    s += f'<rect x="56" y="8" width="12" height="38" rx="6" fill="#fff" stroke="{INK}" stroke-width="1.5"/>'
    s += '<rect x="59" y="14" width="6" height="34" fill="#d1312e"/>'
    s += f'<circle cx="62" cy="50" r="8" fill="#d1312e" stroke="{INK}" stroke-width="1.5"/>'
    s += '<text x="84" y="40" font-family="Avenir Next Condensed, Arial" font-weight="700" font-size="9" fill="#22252b">SUMMER 2026</text>'
    return s


def _bomb():
    s = _bg("#efe4d6")
    s += '<rect y="50" width="240" height="10" fill="#9a8f80"/>'
    s += f'<path d="M150 50 V26 L162 12 L174 26 V50 Z" fill="#d6cbb6" stroke="{INK}" stroke-width="1.3"/>'
    s += f'<rect x="176" y="30" width="30" height="20" fill="#d6cbb6" stroke="{INK}" stroke-width="1.3"/>'
    s += '<line x1="162" y1="4" x2="162" y2="12" stroke="#22252b" stroke-width="1.5"/><line x1="158" y1="7" x2="166" y2="7" stroke="#22252b" stroke-width="1.5"/>'
    s += '<path d="M70 50 l-14 -16 l10 2 l-4 -16 l12 12 l4 -14 l6 14 l12 -10 l-4 16 l12 -2 l-14 14 z" fill="#f08a2a"/>'
    s += '<path d="M80 26 C86 14 96 16 104 4" stroke="#6b6b6b" stroke-width="8" fill="none" opacity=".5"/>'
    return s


def _flags():
    s = _bg("#eef0f4")
    s += '<rect x="22" y="12" width="54" height="12" fill="#cd2a3e"/><rect x="22" y="24" width="54" height="12" fill="#ffffff"/><rect x="22" y="36" width="54" height="12" fill="#436f4d"/>'
    s += '<rect x="22" y="12" width="54" height="36" fill="none" stroke="#22252b" stroke-width="1.2"/>'
    s += '<rect x="164" y="12" width="54" height="18" fill="#2f63b5"/><rect x="164" y="30" width="54" height="18" fill="#f5d33b"/>'
    s += '<rect x="164" y="12" width="54" height="36" fill="none" stroke="#22252b" stroke-width="1.2"/>'
    # handshake: two sleeves and clasped hands
    s += '<path d="M82 40 L104 30 L110 36 L90 48 Z" fill="#cd2a3e" stroke="#22252b" stroke-width="1.1"/>'
    s += '<path d="M158 40 L136 30 L130 36 L150 48 Z" fill="#2f63b5" stroke="#22252b" stroke-width="1.1"/>'
    s += '<path d="M104 30 Q120 20 136 30 L130 38 Q120 44 110 36 Z" fill="#e8b88f" stroke="#22252b" stroke-width="1.1"/>'
    s += '<path d="M112 31 l6 6 M118 28 l6 6 M124 28 l5 5" stroke="#22252b" stroke-width=".9"/>'
    return s


def _fire():
    s = _bg("#3a2a24")
    s += f'<rect x="60" y="24" width="120" height="36" fill="#6e625a" stroke="#1b1b1b" stroke-width="1.3"/>'
    s += '<polygon points="60,24 90,12 120,24 150,12 180,24" fill="#5a4f48" stroke="#1b1b1b" stroke-width="1.2"/>'
    for i in range(5):
        s += f'<rect x="{70 + i * 22}" y="34" width="10" height="10" fill="#f2a33a"/>'
    s += '<path d="M120 24 q8 -18 14 -6 q6 -14 12 0 q4 -8 8 4 z" fill="#f08a2a"/>'
    s += '<path d="M132 10 C138 2 150 4 158 -4" stroke="#999" stroke-width="7" fill="none" opacity=".5"/>'
    return s


PANEL_ART = {"zap": _zap, "gaza": _gaza, "tanker": _tanker, "pill": _pill, "trophy": _trophy,
             "rally": _rally, "dow": _dow, "jets": _jets, "heat": _heat, "bomb": _bomb,
             "flags": _flags, "fire": _fire}
