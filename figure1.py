import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.lines import Line2D

# ── paths ─────────────────────────────────────────────────────────────────────
DATA_FILE  = "Data/ppp_velocity_timeseries.csv"
OUTPUT_DIR = "figures"
OUTPUT_FIG = os.path.join(OUTPUT_DIR, "figure1_position_quality.png")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── constants ─────────────────────────────────────────────────────────────────
RMSP_CUTOFF = 0.05   # metres

# ── load data ─────────────────────────────────────────────────────────────────
print("Loading data …")
df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])
df = df.dropna(subset=["east", "north", "rmsp"])
print(f"  Loaded {len(df):,} epochs across {df['station'].nunique()} stations")

# ── filter statistics ─────────────────────────────────────────────────────────
n_total     = len(df)
n_dropped   = (df["rmsp"] > RMSP_CUTOFF).sum()
pct_dropped = 100 * n_dropped / n_total
print(f"  Dropped (rmsp > {RMSP_CUTOFF} m): {n_dropped:,}  ({pct_dropped:.1f}%)")

kept    = df[df["rmsp"] <= RMSP_CUTOFF]
dropped = df[df["rmsp"] >  RMSP_CUTOFF]

# ── colour map ────────────────────────────────────────────────────────────────
CMAP = plt.cm.viridis
NORM = mcolors.Normalize(vmin=0.0, vmax=RMSP_CUTOFF, clip=True)

# ── figure ────────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(
    1, 2, figsize=(14, 6), facecolor="#F7F9FC",
    gridspec_kw={"width_ratios": [1.4, 1], "wspace": 0.35},
)

fig.suptitle(
    "Figure 1  –  GPS Position Quality Assessment\n"
    "Justification for the RMSP ≤ 0.05 m epoch filter",
    fontsize=13, fontweight="bold", color="#2C3E50", y=1.01,
)

# ── Panel A: scatter coloured by rmsp ────────────────────────────────────────
ax = axes[0]
ax.set_facecolor("#FAFBFC")
for spine in ax.spines.values():
    spine.set_edgecolor("#CCCCCC")

ax.scatter(
    dropped["east"] / 1e3, dropped["north"] / 1e3,
    s=0.5, alpha=0.2, color="#BBBBBB", linewidths=0,
    rasterized=True, label="Dropped",
)
sc = ax.scatter(
    kept["east"] / 1e3, kept["north"] / 1e3,
    c=kept["rmsp"], cmap=CMAP, norm=NORM,
    s=0.8, alpha=0.6, linewidths=0,
    rasterized=True, label="Kept",
)

cbar = fig.colorbar(sc, ax=ax, fraction=0.035, pad=0.02)
cbar.set_label("RMSP  (m)", fontsize=9, color="#444")
cbar.ax.tick_params(labelsize=8)

ax.set_xlabel("Polar-stereographic easting  (km)", fontsize=10, color="#444")
ax.set_ylabel("Polar-stereographic northing  (km)", fontsize=10, color="#444")
ax.set_title("(a)  Raw epoch positions coloured by RMSP",
             fontsize=10, color="#2C3E50", fontstyle="italic", pad=6)
ax.tick_params(labelsize=8, colors="#555")

legend_handles = [
    Line2D([0],[0], marker="o", color="w", markerfacecolor="#999",
           markersize=6, label=f"Dropped  ({pct_dropped:.1f}% of epochs)"),
    Line2D([0],[0], marker="o", color="w", markerfacecolor=CMAP(0.3),
           markersize=6, label="Kept  (rmsp ≤ 0.05 m)"),
]
ax.legend(handles=legend_handles, fontsize=8, loc="upper right",
          framealpha=0.9, edgecolor="#CCCCCC")

# ── Panel B: histogram ────────────────────────────────────────────────────────
ax2 = axes[1]
ax2.set_facecolor("#FAFBFC")
for spine in ax2.spines.values():
    spine.set_edgecolor("#CCCCCC")

clip_max = min(df["rmsp"].quantile(0.995) * 1.05, 0.5)
bins = np.linspace(0, clip_max, 80)

ax2.hist(kept["rmsp"], bins=bins, color="#4A90D9", alpha=0.8,
         edgecolor="white", linewidth=0.4, label="Kept")
ax2.hist(dropped["rmsp"].clip(upper=clip_max), bins=bins,
         color="#E84855", alpha=0.7, edgecolor="white", linewidth=0.4,
         label="Dropped")

ax2.axvline(RMSP_CUTOFF, color="#F5A623", linewidth=2.0,
            linestyle="--", label=f"Cutoff  {RMSP_CUTOFF} m")

ymax = ax2.get_ylim()[1]
ax2.text(RMSP_CUTOFF + 0.001, ymax * 0.85,
         f"{pct_dropped:.1f}% of epochs\ndropped",
         fontsize=9, color="#E84855", fontweight="bold", va="top")

ax2.set_xlabel("RMSP  (m)", fontsize=10, color="#444")
ax2.set_ylabel("Number of epochs", fontsize=10, color="#444")
ax2.set_title("(b)  RMSP distribution  |  0.05 m cutoff",
              fontsize=10, color="#2C3E50", fontstyle="italic", pad=6)
ax2.tick_params(labelsize=8, colors="#555")
ax2.yaxis.grid(True, color="#E0E0E0", linestyle="--", linewidth=0.6)
ax2.set_axisbelow(True)
ax2.legend(fontsize=8, framealpha=0.9, edgecolor="#CCCCCC")

# ── save ──────────────────────────────────────────────────────────────────────
plt.savefig(OUTPUT_FIG, dpi=200, bbox_inches="tight",
            facecolor=fig.get_facecolor())
print(f"\n✓  Figure saved → {OUTPUT_FIG}")
plt.close()


import pandas as pd
df = pd.read_csv('Data/ppp_velocity_timeseries.csv')
print(df['rmsp'].describe())
print('unique rmsp values sample:', df['rmsp'].unique()[:20])
