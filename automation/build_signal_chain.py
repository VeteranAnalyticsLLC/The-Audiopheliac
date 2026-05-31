"""
The Audiopheliac — Office Studio Signal Chain
Visual philosophy: Signal Cartography
Output: high-resolution PNG + vector PDF
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle
import matplotlib.lines as mlines
from matplotlib import font_manager
import numpy as np

# ---------------- BRAND PALETTE (Full Spectrum, per CLAUDE.md) ----------------
INK         = '#0A0A0B'
PAPER       = '#F5F5F7'
HAIRLINE    = '#FFFFFF'
DIM         = '#22232A'
MID         = '#4A4D58'

YELLOW      = '#F8E91F'   # Analog audio
LIGHT_GREEN = '#99E257'   # Phono / pre-stage
GREEN       = '#41D99A'   # Digital audio (USB)
TEAL        = '#0ABED3'   # USB-C data spine
BLUE        = '#0F82DF'   # Video (DP / HDMI)
VIOLET      = '#5E54D4'   # USB-A peripherals
POWER       = '#6A6A6E'   # AC / DC power

# ---------------- CANVAS ----------------
W, H = 120, 68   # logical units, 16:9-ish ratio
fig, ax = plt.subplots(figsize=(24, 13.6), facecolor=INK)
ax.set_facecolor(INK)
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.set_aspect('equal')
ax.axis('off')

# ---------------- HELPERS ----------------
def device(x, y, w, h, label, sub='', accent=PAPER, sub_color=None):
    """Device node: rounded rectangle with color accent stripe + labels."""
    # Outer box
    box = FancyBboxPatch((x, y), w, h,
                         boxstyle="round,pad=0.0,rounding_size=0.35",
                         linewidth=0.9, edgecolor=accent, facecolor=INK)
    ax.add_patch(box)
    # Top color stripe
    stripe = FancyBboxPatch((x, y + h - 0.55), w, 0.55,
                            boxstyle="round,pad=0.0,rounding_size=0.0",
                            linewidth=0, facecolor=accent)
    ax.add_patch(stripe)
    # Main label
    ax.text(x + w/2, y + h*0.62, label,
            color=PAPER, fontsize=10.5, ha='center', va='center',
            family='sans-serif', weight='semibold')
    # Sub label
    if sub:
        sub_col = sub_color or '#A5A6AB'
        ax.text(x + w/2, y + h*0.30, sub,
                color=sub_col, fontsize=7, ha='center', va='center',
                family='monospace', alpha=0.95)
    return (x, y, w, h)

def port(cx, cy, color):
    """A small connection-point dot."""
    ax.add_patch(Circle((cx, cy), 0.30, facecolor=color, edgecolor=INK, linewidth=0.4, zorder=5))

def line(p1, p2, color, label='', label_pos='mid', label_side='above', dash=False, lw=1.4):
    """Orthogonal signal line (right-angles only), optional label."""
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2 or y1 == y2:
        xs, ys = [x1, x2], [y1, y2]
    else:
        # Choose bend orientation based on relative position
        # Default: go horizontal first, then vertical
        mid = (x1 + x2) / 2
        xs = [x1, mid, mid, x2]
        ys = [y1, y1, y2, y2]
    ls = (0, (3, 2)) if dash else '-'
    ax.plot(xs, ys, color=color, linewidth=lw, linestyle=ls,
            solid_capstyle='round', solid_joinstyle='round', zorder=3)
    port(x1, y1, color)
    port(x2, y2, color)
    if label:
        if label_pos == 'mid':
            lx, ly = (x1 + x2) / 2, (y1 + y2) / 2
        elif label_pos == 'start':
            lx, ly = x1 + (x2-x1)*0.25, y1 + (y2-y1)*0.25
        else:
            lx, ly = x1 + (x2-x1)*0.75, y1 + (y2-y1)*0.75
        dy = 0.95 if label_side == 'above' else -0.95
        ax.text(lx, ly + dy, label, color=color, fontsize=6.4,
                ha='center', va='center', family='monospace', alpha=0.95)

def vline(x, y1, y2, color, dash=False, lw=1.4):
    ls = (0, (3, 2)) if dash else '-'
    ax.plot([x, x], [y1, y2], color=color, linewidth=lw, linestyle=ls,
            solid_capstyle='round', zorder=3)

def hline(y, x1, x2, color, dash=False, lw=1.4):
    ls = (0, (3, 2)) if dash else '-'
    ax.plot([x1, x2], [y, y], color=color, linewidth=lw, linestyle=ls,
            solid_capstyle='round', zorder=3)

def path(points, color, dash=False, lw=1.4, label='', label_idx=None, label_side='above'):
    """Draw a multi-segment orthogonal path through a sequence of points."""
    ls = (0, (3, 2)) if dash else '-'
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    ax.plot(xs, ys, color=color, linewidth=lw, linestyle=ls,
            solid_capstyle='round', solid_joinstyle='round', zorder=3)
    port(points[0][0], points[0][1], color)
    port(points[-1][0], points[-1][1], color)
    if label and label_idx is not None and 0 <= label_idx < len(points)-1:
        p1 = points[label_idx]
        p2 = points[label_idx+1]
        lx, ly = (p1[0]+p2[0])/2, (p1[1]+p2[1])/2
        dy = 0.95 if label_side == 'above' else -0.95
        ax.text(lx, ly + dy, label, color=color, fontsize=6.4,
                ha='center', va='center', family='monospace', alpha=0.95)

# ---------------- TITLE BAR ----------------
ax.text(4, 64.2, "T H E   A U D I O P H E L I A C",
        color=PAPER, fontsize=20, weight='bold',
        family='sans-serif', ha='left', va='center')
ax.text(4, 61.0, "O F F I C E   S T U D I O   ·   S I G N A L   C H A I N",
        color='#B8BABE', fontsize=9, family='sans-serif',
        ha='left', va='center')
ax.text(W-4, 64.2, "2026.05",
        color=PAPER, fontsize=11, family='monospace',
        ha='right', va='center')
ax.text(W-4, 61.0, "GDMARCHE  ·  Office Studio",
        color='#B8BABE', fontsize=8, family='monospace',
        ha='right', va='center', alpha=0.85)
hline(58.6, 4, W-4, color='#2A2C33', lw=0.8)

# ---------------- DEVICE NODES ----------------

# === CAPTURE PATH (top row) — yellow / light green ===
device(2.5,   48.5,  10.5, 6,  "AT-LP120XUSB", "Turntable · RCA out\nUSB cable: UNPLUGGED",
       accent=YELLOW)
device(16.0,  48.5,  10.5, 6,  "Schiit Mani II", "Phono preamp · MM",
       accent=LIGHT_GREEN)

# === MOTU — central audio I/O hub ===
device(30.0,  39.5,  14.0, 15, "MOTU M4", "USB-C audio interface\n24-bit · 192 kHz",
       accent=GREEN)
# Sub-label for I/O sections
ax.text(37.0, 50.5, "INPUTS 3 / 4 · TRS line", color=YELLOW, fontsize=6.4,
        ha='center', family='monospace', alpha=0.95)
ax.text(37.0, 41.8, "OUTPUTS 1 / 2 · TRS main", color=BLUE, fontsize=6.4,
        ha='center', family='monospace', alpha=0.95)
hline(46.5, 30.5, 43.5, color=MID, lw=0.5)

# === WORKSTATION — Precision 7540 (visual center of gravity) ===
device(50.0,  36.0,  18.0, 18, "Precision 7540", "GDMARCHE · Xeon E-2286M\nWin 11 · Ableton 12 · Audacity",
       accent=TEAL)

# === Dell 240W barrel charger ===
device(52.0,  21.5,  14.0, 5.5, "Dell 240W Barrel", "Primary AC power · independent of dock",
       accent=POWER)

# === HEADPHONES — alt monitor path for capture ===
device(30.0,  29.5,  14.0, 5.0, "ATH-M50x", "M4 front headphone jack\nUse during vinyl capture",
       accent=YELLOW)

# === DOCK — WD19DCS, port multiplier ===
device(72.0,  36.0,  14.0, 18, "WD19DCS", "Dell Performance Dock\nSingle-cable mode · 1 of 2 USB-C used",
       accent=VIOLET)
ax.text(79.0, 47.5, "DP1 · DP2 · HDMI", color=BLUE, fontsize=6.4,
        ha='center', family='monospace', alpha=0.95)
ax.text(79.0, 41.5, "USB-A × 4  ·  Ethernet", color=VIOLET, fontsize=6.4,
        ha='center', family='monospace', alpha=0.95)
ax.text(79.0, 38.4, "Front USB-C: EMPTY", color='#E26666', fontsize=6.0,
        ha='center', family='monospace', weight='bold', alpha=0.95)
hline(43.5, 72.5, 85.5, color=MID, lw=0.5)
hline(39.7, 72.5, 85.5, color=MID, lw=0.5)

# === DISPLAYS ===
device(91.0,  50.5,  14.0, 4.0, "Sansui Monitor 1", "HDMI · 27\"",
       accent=BLUE)
device(91.0,  45.0,  14.0, 4.0, "Sansui Monitor 2", "DP → HDMI passive",
       accent=BLUE)
device(91.0,  39.5,  14.0, 4.0, "Dell Monitor",     "DP → DP · shared with GFE",
       accent=BLUE)

# === PERIPHERALS — USB-A on dock ===
device(91.0,  33.0,  14.0, 4.0, "Casio Privia",     "USB-B → USB-A · MIDI over USB",
       accent=VIOLET)
device(91.0,  27.5,  14.0, 4.0, "WD Smartware",     "Nightly backup · external HDD",
       accent=VIOLET)
device(91.0,  22.0,  14.0, 4.0, "Spark 40 amp",     "USB MIDI / control",
       accent=VIOLET)
device(91.0,  16.5,  14.0, 4.0, "Ethernet",         "Spectrum SAX2V1R · wired LAN",
       accent=VIOLET)

# === MONITORING / MIX BUS (bottom) ===
device(50.0,  10.5,  18.0, 7.0, "Rolls MX28 Mini-Mix VI", "Level 3: MOTU stereo  ·  Master = daily volume",
       accent=BLUE)
device(28.0,   1.0,   8.0, 6.5, "Yamaha HS7 L",     "Studio monitor",
       accent=BLUE)
device(38.0,   1.0,   8.0, 6.5, "JBL LSR310S",      "Subwoofer · crossover",
       accent=BLUE)
device(48.0,   1.0,   8.0, 6.5, "Yamaha HS7 R",     "Studio monitor",
       accent=BLUE)

# ---------------- CONNECTIONS ----------------

# --- CAPTURE (yellow → green) ---
line((13.0, 51.5), (16.0, 51.5), YELLOW, label='RCA · L+R')
line((26.5, 51.5), (30.0, 51.5), YELLOW, label='RCA · L+R')

# --- MOTU → PC (USB-C, audio + data) ---
line((44.0, 47.0), (50.0, 47.0), GREEN, label='USB-C · class-compliant audio')

# --- PC USB-C #1 → WD19DCS (dock spine) ---
line((68.0, 47.0), (72.0, 47.0), TEAL, label='USB-C #1 · dock primary cable')

# --- Dell barrel charger → PC ---
line((59.0, 27.0), (59.0, 36.0), POWER, label='240W barrel · independent of dock', label_side='below')

# --- ATH-M50x ← MOTU front headphone (alternate, from MOTU bottom-LEFT) ---
line((33.0, 39.5), (33.0, 34.5), YELLOW, dash=True, lw=1.0, label='Front HP jack', label_side='below')

# --- WD19DCS → Displays (video, blue) ---
line((86.0, 52.5), (91.0, 52.5), BLUE, label='HDMI')
line((86.0, 47.0), (91.0, 47.0), BLUE, label='DP→HDMI')
line((86.0, 41.5), (91.0, 41.5), BLUE, label='DP→DP')

# --- WD19DCS → Peripherals (violet) ---
line((86.0, 35.0), (91.0, 35.0), VIOLET, label='USB-A · USB-B')
line((86.0, 29.5), (91.0, 29.5), VIOLET, label='USB-A · USB-A')
line((86.0, 24.0), (91.0, 24.0), VIOLET, label='USB-A · USB-B')
line((86.0, 18.5), (91.0, 18.5), VIOLET, label='RJ-45')

# --- MOTU outputs → MX28 (analog audio, yellow) — routes via the M4/PC gap ---
path([(44.0, 41.0), (47.0, 41.0), (47.0, 17.5), (50.0, 17.5)], YELLOW,
     label='TRS · L+R to Level 3', label_idx=1, label_side='above')

# --- MX28 main out → HS7 L / JBL Sub / HS7 R (analog, blue accent for monitoring) ---
path([(56.0, 10.5), (56.0, 8.5), (32.0, 8.5), (32.0, 7.5)], BLUE,
     label='Main out · L', label_idx=1, label_side='below')
path([(59.0, 10.5), (59.0, 9.0), (42.0, 9.0), (42.0, 7.5)], BLUE,
     label='Sub feed', label_idx=1, label_side='below')
path([(62.0, 10.5), (62.0, 9.5), (52.0, 9.5), (52.0, 7.5)], BLUE,
     label='Main out · R', label_idx=1, label_side='below')

# ---------------- LEGEND ----------------
LEG_X = 4.0
LEG_Y = 13.0
LEG_W = 22.0
LEG_H = 22.0

# Legend frame
legend_box = FancyBboxPatch((LEG_X, LEG_Y), LEG_W, LEG_H,
                            boxstyle="round,pad=0.0,rounding_size=0.4",
                            linewidth=0.7, edgecolor=MID, facecolor=INK)
ax.add_patch(legend_box)
ax.text(LEG_X + 1.2, LEG_Y + LEG_H - 1.6, "SIGNAL VOCABULARY",
        color=PAPER, fontsize=9, family='sans-serif',
        weight='bold')
hline(LEG_Y + LEG_H - 2.4, LEG_X + 1.2, LEG_X + LEG_W - 1.2, color=MID, lw=0.4)

legend_items = [
    (YELLOW,      "ANALOG AUDIO",     "RCA · TRS · phono"),
    (LIGHT_GREEN, "PHONO STAGE",      "Preamp output"),
    (GREEN,       "DIGITAL AUDIO",    "USB class-compliant"),
    (TEAL,        "USB-C DATA",       "Dock spine · workstation"),
    (BLUE,        "VIDEO",            "DisplayPort · HDMI"),
    (VIOLET,      "USB-A PERIPHERAL", "MIDI · storage · ethernet"),
    (POWER,       "POWER",            "AC · DC barrel"),
]
y_cursor = LEG_Y + LEG_H - 4.5
for color, label, hint in legend_items:
    # swatch line
    ax.plot([LEG_X + 1.5, LEG_X + 4.5], [y_cursor, y_cursor],
            color=color, linewidth=2.0, solid_capstyle='round')
    ax.text(LEG_X + 5.2, y_cursor + 0.05, label,
            color=PAPER, fontsize=7.5, family='sans-serif',
            weight='semibold', va='center')
    ax.text(LEG_X + 5.2, y_cursor - 0.9, hint,
            color='#A5A6AB', fontsize=6.4, family='monospace',
            va='center', alpha=0.9)
    y_cursor -= 2.4

# ---------------- FOOTER ----------------
hline(1.0, 4, W-4, color='#2A2C33', lw=0.6)
ax.text(4, 0.4, "Every cable, waveform, and decibel earns its keep.",
        color='#7A7C82', fontsize=7.5, family='sans-serif',
        ha='left', va='center', style='italic', alpha=0.9)
ax.text(W-4, 0.4, "theaudiopheliac.com",
        color='#7A7C82', fontsize=7.5, family='monospace',
        ha='right', va='center', alpha=0.9)

# ---------------- ZONE LABELS (subtle, top of each region) ----------------
ax.text(15.0, 56.0, "CAPTURE PATH",
        color='#888A90', fontsize=7, family='sans-serif',
        ha='left', alpha=0.85)
ax.text(50.0, 56.0, "WORKSTATION",
        color='#888A90', fontsize=7, family='sans-serif',
        ha='left', alpha=0.85)
ax.text(72.0, 56.0, "EXPANSION  ·  DISPLAYS  ·  PERIPHERALS",
        color='#888A90', fontsize=7, family='sans-serif',
        ha='left', alpha=0.85)
ax.text(50.0, 19.0, "MONITORING PATH",
        color='#888A90', fontsize=7, family='sans-serif',
        ha='left', alpha=0.85)

# ---------------- SAVE ----------------
out_dir = "/sessions/pensive-zealous-curie/mnt/outputs"
import os
png_path = os.path.join(out_dir, "Audiopheliac_Signal_Chain.png")
pdf_path = os.path.join(out_dir, "Audiopheliac_Signal_Chain.pdf")
plt.savefig(png_path, dpi=240, facecolor=INK, bbox_inches='tight', pad_inches=0.25)
plt.savefig(pdf_path,            facecolor=INK, bbox_inches='tight', pad_inches=0.25)
print("Saved:", png_path)
print("Saved:", pdf_path)
