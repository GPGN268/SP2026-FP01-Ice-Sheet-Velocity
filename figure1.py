import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.lines import Line2D

DATA_FILE  = "Data/ppp_velocity_timeseries.csv"
OUTPUT_DIR = "figures"
OUTPUT_FIG = os.path.join(OUTPUT_DIR, "figure1_position_quality.png")
os.makedirs(OUTPUT_DIR, exist_ok=True)

RMSP_CUTOFF = 0.05

df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])
df = df.dropna(subset=["east", "north", "rmsp"])
df = df[
    (df["east"].between(-8e5, 0)) &
    (df["north"].between(-7e5, -4e5))
]
print(f"Loaded {len(df):,} epochs across {df['station'].nunique()} stations")

n_total     = len(df)
n_dropped   = (df["rmsp"] > RMSP_CUTOFF).sum()
pct_dropped = 100 * n_dropped / n_total
print(f"rmsp range: {df['rmsp'].min():.4f} – {df['rmsp'].max():.4f} m")
print(f"Dropped: {n_dropped} ({pct_dropped:.1f}%)")

kept    = df[df["rmsp"] <= RMSP_CUTOFF]
dropped = df[df["rmsp"] >  RMSP_CUTOFF]

CMAP = plt.cm.viridis
NORM = mcolors.Normalize(vmin=df["rmsp"].min(), vmax=df["rmsp"].max())

fig, axes = plt.subplots(
    1, 2, figsize=(14, 6), facecolor="#F7F9FC",
    gridspec_kw={"width_ratios": [1.4, 1], "wspace": 0.35},
)

fig.suptitle(
    "Figure 1  –  GPS Position Quality Assessment\n"
    "Raw epoch positions and RMSP distribution  |  Whillans Ice Stream GPS Network",
    fontsize=13, fontweight="bold", color="#2C3E50", y=1.01,
)

ax = axes[0]
ax.set_facecolor("#FAFBFC")
for spine in ax.spines.values():
    spine.set_edgecolor("#CCCCCC")

sc = ax.scatter(
    df["east"] / 1e3, df["north"] / 1e3,
    c=df["rmsp"], cmap=CMAP, norm=NORM,
    s=1.5, alpha=0.6, linewidths=0, rasterized=True,
)

cbar = fig.colorbar(sc, ax=ax, fraction=0.035, pad=0.02)
cbar.set_label("RMSP  (m)", fontsize=9, color="#444")
cbar.ax.tick_params(labelsize=8)

ax.set_xlabel("Polar-stereographic easting  (km)", fontsize=10, color="#444")
ax.set_ylabel("Polar-stereographic northing  (km)", fontsize=10, color="#444")
ax.set_title("(a)  Raw epoch positions coloured by RMSP",
             fontsize=10, color="#2C3E50", fontstyle="italic", pad=6)
ax.tick_params(labelsize=8, colors="#555")

for stn, grp in df.groupby("station"):
    cx = grp["east"].median() / 1e3
    cy = grp["north"].median() / 1e3
    ax.text(cx, cy, stn, fontsize=5.5, ha="center", va="center",
            color="#2C3E50", fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.15", fc="white", alpha=0.5, ec="none"))

ax2 = axes[1]
ax2.set_facecolor("#FAFBFC")
for spine in ax2.spines.values():
    spine.set_edgecolor("#CCCCCC")

bins = np.linspace(df["rmsp"].min(), df["rmsp"].max() * 1.05, 60)

ax2.hist(kept["rmsp"], bins=bins, color="#4A90D9", alpha=0.85,
         edgecolor="white", linewidth=0.4, label="Kept")

if len(dropped) > 0:
    ax2.hist(dropped["rmsp"].clip(upper=bins[-1]), bins=bins,
             color="#E84855", alpha=0.7, edgecolor="white", linewidth=0.4,
             label="Dropped")

ax2.axvline(RMSP_CUTOFF, color="#E84855", linewidth=2.0,
            linestyle="--", label=f"Cutoff  {RMSP_CUTOFF} m")

ymax = ax2.get_ylim()[1]
label = f"{pct_dropped:.1f}% of epochs dropped" if n_dropped > 0 else "100% of epochs\npassed filter"
ax2.text(RMSP_CUTOFF * 0.95, ymax * 0.85, label,
         fontsize=9, color="#2C3E50", fontweight="bold", va="top", ha="right")

ax2.set_xlabel("RMSP  (m)", fontsize=10, color="#444")
ax2.set_ylabel("Number of epochs", fontsize=10, color="#444")
ax2.set_title("(b)  RMSP distribution  |  0.05 m cutoff",
              fontsize=10, color="#2C3E50", fontstyle="italic", pad=6)
ax2.tick_params(labelsize=8, colors="#555")
ax2.yaxis.grid(True, color="#E0E0E0", linestyle="--", linewidth=0.6)
ax2.set_axisbelow(True)
ax2.legend(fontsize=8, framealpha=0.9, edgecolor="#CCCCCC")

plt.savefig(OUTPUT_FIG, dpi=200, bbox_inches="tight", facecolor=fig.get_facecolor())
print(f"\n✓  Figure saved → {OUTPUT_FIG}")
plt.close()