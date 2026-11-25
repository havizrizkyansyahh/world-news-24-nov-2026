"""Builds entry.png: writes page.html, renders it in headless Chrome at 2x, downsamples to
1024x1024 and saves a PNG under 1 MiB.  Run: python3 src/build.py  (needs Chrome + Pillow)."""
import json
import os
import subprocess
import sys
from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import art  # noqa: E402
from stories import BRIEFS, LEADS, LEFT_OUT, NUMBERS, PANELS, REGIONS  # noqa: E402

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
RCOL = {k: c for k, _, c in REGIONS}
RNAME = {k: n for k, n, _ in REGIONS}
TAGS = {"C": ("CONFIRMED", "#2d7d46"), "O": ("OFFICIAL", "#1f4e8c"),
        "R": ("REPORTED", "#7a7a7a"), "CL": ("CLAIM", "#b5541b")}

# ------------------------------------------------------------------ map
MAP_W, MAP_H = 268, 150
LON0, LON1, LAT0, LAT1 = -170, 180, -48, 76


def proj(lon, lat):
    return ((lon - LON0) / (LON1 - LON0) * MAP_W, (LAT1 - lat) / (LAT1 - LAT0) * MAP_H)


def world_path():
    gj = json.loads((HERE / "ne_110m_land.geojson").read_text())
    d = []
    for f in gj["features"]:
        g = f["geometry"]
        polys = g["coordinates"] if g["type"] == "MultiPolygon" else [g["coordinates"]]
        for poly in polys:
            ring = poly[0]
            pts = [proj(x, y) for x, y in ring if y > LAT0 - 5]
            if len(pts) < 3:
                continue
            d.append("M" + "L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + "Z")
    return "".join(d)


def map_svg():
    s = f'<svg viewBox="0 0 {MAP_W} {MAP_H}" xmlns="http://www.w3.org/2000/svg">'
    s += f'<rect width="{MAP_W}" height="{MAP_H}" fill="#dce7ee"/>'
    s += f'<path d="{world_path()}" fill="#efe9dc" stroke="#b9b09c" stroke-width=".5"/>'
    for st in LEADS + PANELS:
        x, y = proj(st["lon"], st["lat"])
        r = 6.2 if st["n"] <= 3 else 5.2
        s += (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{RCOL[st["reg"]]}" stroke="#fff" stroke-width="1"/>'
              f'<text x="{x:.1f}" y="{y + 2.6:.1f}" text-anchor="middle" font-size="{7 if st["n"] < 10 else 6}" '
              f'font-weight="700" fill="#fff" font-family="Avenir Next Condensed, Arial">{st["n"]}</text>')
    return s + "</svg>"


# ------------------------------------------------------------------ html
def tag(t):
    name, col = TAGS[t]
    return f'<span class="tag" style="color:{col};border-color:{col}">{name}</span>'


def region_counts():
    counts = {k: 0 for k, _, _ in REGIONS}
    for st in LEADS + PANELS:
        counts[st["reg"]] += 1
    for b in BRIEFS:
        counts[b[0]] += 1
    return counts


def build_html():
    counts = region_counts()
    total = sum(counts.values())
    nregions = sum(1 for v in counts.values() if v)
    chips = "".join(f'<span class="chip" style="background:{RCOL[k]}">{RNAME[k]} {counts[k]}</span>'
                    for k, _, _ in REGIONS if counts[k])
    nums = "".join(f'<div class="num"><b>{a}</b><span>{b}</span></div>' for a, b in NUMBERS)

    leads = ""
    for st in LEADS:
        leads += f'''<div class="lead">
  <div class="art">{art.lead(st["art"], st["badge"])}<span class="pin" style="background:{RCOL[st["reg"]]}">{st["n"]}</span></div>
  <div class="kick"><span style="color:{RCOL[st["reg"]]}">{RNAME[st["reg"]].upper()}</span> · {st["place"]} · {st["field"]} {tag(st["tag"])}</div>
  <h2>{st["head"]}</h2>
  <p>{st["deck"]}</p>
  <div class="src">{st["src"]}</div>
</div>'''

    panels = ""
    for st in PANELS:
        panels += f'''<div class="panel">
  <div class="part">{art.panel(st["art"], st["badge"])}<span class="pin s" style="background:{RCOL[st["reg"]]}">{st["n"]}</span></div>
  <div class="kick"><span style="color:{RCOL[st["reg"]]}">{st["place"]}</span><span class="ksrc">{st["src"]}</span> {tag(st["tag"])}</div>
  <h3>{st["head"]}</h3>
  <p>{st["deck"]}</p>
</div>'''

    first = len(LEADS) + len(PANELS) + 1
    half = (len(BRIEFS) + 1) // 2
    cols = ["", ""]
    for i, (reg, place, text, src, t) in enumerate(BRIEFS):
        n = first + i
        cols[0 if i < half else 1] += (
            f'<li><span class="bn" style="background:{RCOL[reg]}">{n}</span>'
            f'<b>{place}:</b> {text} <i>{src}</i> <span class="st" style="color:{TAGS[t][1]}">{t}</span></li>')

    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1024px;height:1024px;overflow:hidden}}
body{{background:#f7f3ea;color:#1c1f24;font-family:"Helvetica Neue",Arial,sans-serif;padding:8px 14px 0}}
.top{{display:flex;justify-content:space-between;font:700 10.5px "Avenir Next Condensed","Helvetica Neue";letter-spacing:.6px}}
.top .l{{color:#b3202a}}
h1{{font:700 60px/1 Georgia,"Times New Roman",serif;text-align:center;letter-spacing:-.5px;margin:1px 0 0}}
.deck{{text-align:center;font:italic 15.5px Georgia,serif;color:#8a1c22;margin:3px 0 4px;border-bottom:2px solid #1c1f24;padding-bottom:4px}}
.deck b{{font-style:normal;color:#1c1f24;margin:0 6px}}
.row{{display:flex;align-items:center;gap:5px;margin:4px 0 4px}}
.chip{{color:#fff;font:700 10.5px "Avenir Next Condensed","Helvetica Neue";padding:2px 7px;border-radius:2px;letter-spacing:.3px}}
.row .lab{{font:700 10.5px "Avenir Next Condensed";margin-left:auto;color:#444}}
.nums{{display:flex;border-top:1px solid #bbb;border-bottom:1px solid #bbb;margin-bottom:5px}}
.num{{flex:1;text-align:center;padding:2px 2px 3px;border-left:1px solid #d6d0c2}}
.num:first-child{{border-left:0}}
.num b{{display:block;font:700 19px/1.1 Georgia,serif;color:#8a1c22}}
.num span{{font:10px "Helvetica Neue";color:#333}}
.leads{{display:flex;gap:10px}}
.lead{{flex:1;background:#fffdf8;border:1px solid #d3cbb8;padding:0 0 4px}}
.art,.part{{position:relative;line-height:0}}
.art svg{{width:100%;height:104px;display:block}}
.pin{{position:absolute;left:5px;top:5px;width:20px;height:20px;border-radius:50%;color:#fff;font:700 12px/20px "Avenir Next Condensed";text-align:center;border:1.5px solid #fff}}
.pin.s{{width:16px;height:16px;font-size:10px;line-height:15px;left:3px;top:3px}}
.kick{{font:700 9.5px "Avenir Next Condensed","Helvetica Neue";letter-spacing:.4px;color:#555;padding:4px 7px 0;display:flex;align-items:center;gap:4px}}
.tag{{font:700 8.5px "Avenir Next Condensed";border:1px solid;border-radius:2px;padding:0 3px;margin-left:auto;letter-spacing:.3px;line-height:12px}}
h2{{font:700 21px/1.08 Georgia,serif;padding:2px 7px 0;letter-spacing:-.2px}}
.lead p{{font:11.2px/1.28 "Helvetica Neue";padding:3px 7px 0;color:#2b2e33}}
.src{{font:italic 10px Georgia;color:#666;padding:2px 7px 0}}
.grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:6px 8px;margin-top:6px}}
.panel{{background:#fffdf8;border:1px solid #d3cbb8;padding-bottom:3px}}
.part svg{{width:100%;height:42px;display:block}}
.panel .kick{{padding:3px 5px 0;font-size:9px}}
h3{{font:700 14px/1.1 Georgia,serif;padding:1px 5px 0}}
.panel p{{font:10px/1.25 "Helvetica Neue";padding:1px 5px 0;color:#2b2e33;white-space:nowrap;overflow:hidden}}
.ksrc{{font:italic 9px Georgia;color:#777;letter-spacing:0;font-weight:400}}
.panel p i{{color:#777;font-family:Georgia}}
.bottom{{display:flex;gap:12px;margin-top:7px;border-top:2px solid #1c1f24;padding-top:4px}}
.mapbox{{width:268px;flex:none}}
.mapbox svg{{width:268px;height:150px;display:block;border:1px solid #c9c1ae}}
.hd{{font:700 10.5px "Avenir Next Condensed";letter-spacing:.5px;margin-bottom:3px;display:flex;justify-content:space-between}}
.legend{{font:9px "Helvetica Neue";color:#444;margin-top:3px;line-height:1.35}}
.legend span{{display:inline-block;width:8px;height:8px;border-radius:50%;margin:0 2px 0 5px;vertical-align:-1px}}
.briefs{{flex:1;display:flex;gap:12px}}
.briefs ul{{list-style:none;flex:1}}
.briefs li{{font:10.3px/1.47 "Helvetica Neue";white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.briefs li i{{color:#777;font:italic 9.5px Georgia}}
.bn{{display:inline-block;width:17px;text-align:center;color:#fff;font:700 9px/13px "Avenir Next Condensed";border-radius:2px;margin-right:4px}}
.st{{font:700 8px "Avenir Next Condensed"}}
.dc{{margin-top:5px;white-space:nowrap;overflow:hidden;border:1.5px solid #b3202a;background:#fbecea;padding:3px 7px;font:10px/1.35 "Helvetica Neue";color:#333}}
.dc .k{{background:#b3202a;color:#fff;font:700 9.5px "Avenir Next Condensed";padding:1px 5px;margin-right:6px;border-radius:2px}}
.foot{{display:flex;justify-content:space-between;font:9.5px "Helvetica Neue";color:#555;margin-top:4px}}
.foot .k{{font:700 8.5px "Avenir Next Condensed";border:1px solid;border-radius:2px;padding:0 3px;margin:0 2px 0 6px}}
</style></head><body>
<div class="top"><span class="l">THE WORLD IN ONE DAY</span><span>{total} STORIES · {nregions} REGIONS · EVERY ONE FROM TUESDAY 24 NOVEMBER 2026</span></div>
<h1>Tuesday 24 November 2026</h1>
<div class="deck">US jury convicts Huawei<b>◆</b>China probes Shanghai’s party chief<b>◆</b>Houthi drone hits Riyadh tower, 11 hurt</div>
<div class="row">{chips}<span class="lab">= {total} stories</span></div>
<div class="nums">{nums}</div>
<div class="leads">{leads}</div>
<div class="grid">{panels}</div>
<div class="bottom">
  <div class="mapbox"><div class="hd"><span>WHERE IT HAPPENED</span><span>PINS = STORIES 1–{len(LEADS) + len(PANELS)}</span></div>{map_svg()}
</div>
  <div style="flex:1;min-width:0"><div class="hd"><span>ALSO ON TUESDAY 24 NOVEMBER · {len(BRIEFS)} MORE STORIES</span><span>C confirmed · O official · R reported</span></div>
  <div class="briefs"><ul>{cols[0]}</ul><ul>{cols[1]}</ul></div></div>
</div>
<div class="dc"><span class="k">DATE CHECK</span>Left out as other days’ news: {LEFT_OUT}</div>
<div class="foot"><span>Every story happened, or was first reported, on Tuesday 24 November 2026 (any time zone) · sources named beside each item</span><span>Original drawings, no photos</span></div>
</body></html>'''


def main():
    out_dir = ROOT / "build"
    out_dir.mkdir(exist_ok=True)
    page = out_dir / "page.html"
    page.write_text(build_html(), encoding="utf-8")
    shot = out_dir / "shot2x.png"
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                    "--force-device-scale-factor=2", "--window-size=1024,1024",
                    "--default-background-color=00000000", f"--screenshot={shot}",
                    page.as_uri()], check=True, capture_output=True)
    img = Image.open(shot).convert("RGB")
    img = img.resize((1024, 1024), Image.LANCZOS)
    img.save(out_dir / "full.png", optimize=True)
    # Reduce to a 256-colour palette only if needed to stay under 1 MiB.
    target = ROOT / "entry.png"
    img.save(target, optimize=True)
    if os.path.getsize(target) > 1_000_000:
        q = img.quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
        q.save(target, optimize=True)
    print("entry.png", os.path.getsize(target), "bytes")


if __name__ == "__main__":
    main()
