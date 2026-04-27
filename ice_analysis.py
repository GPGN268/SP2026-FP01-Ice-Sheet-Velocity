import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.lines import Line2D

DATA_PATH  = "Data/whillans_velocity_slip_merged_wide.csv"
OUTPUT_DIR = "figures"
OUTPUT_FIG = os.path.join(OUTPUT_DIR, "position_outliers.png")

IQR_MULTIPLIER = 1.5
STATIONS = ["WB07","WB08","WB09","WB10","WB11","WB12","WB13","WB14","ENB","SLW"]

COLOR_NORMAL  = "#4A90D9"
COLOR_OUTLIER = "#E84855"
COLOR_MEDIAN  = "#F5A623"
COLOR_BOX     = "#2C3E50"

os.makedirs(OUTPUT_DIR, exist_ok=True)

print("Loading data …")
df = pd.read_csv(DATA_PATH, parse_dates=["start_time"])
df = df.sort_values("start_time").reset_index(drop=True)

def iqr_outlier_mask(series):
    q1  = series.quantile(0.25)
    q3  = series.quantile(0.75)
    iqr = q3 - q1
    lo  = q1 - IQR_MULTIPLIER * iqr
    hi  = q3 + IQR_MULTIPLIER * iqr
    return (series < lo) | (series > hi)

station_data = {}
for stn in STATIONS:
    col  = f"{stn}_v_myr"
    vals = df[["start_time", col]].dropna(subset=[col]).copy()
    vals["is_outlier"] = iqr_outlier_mask(vals[col])
    station_data[stn] = vals

outlier_pct = {
    stn: 100 * d["is_outlier"].mean()
    for stn, d in station_data.items()
}

fig = plt.figure(figsize=(20, 18), facecolor="#F7F9FC")
fig.suptitle(
    "GPS Position-Derived Velocity: Outlier / Noise Analysis\n"
    "Whillans Ice Stream GPS Stations  |  15-second epoch sampling",
    fontsize=16, fontweight="bold", color=COLOR_BOX, y=0.98
)

outer = gridspec.GridSpec(3, 1, figure=fig,
                          hspace=0.45,
                          top=0.94, bottom=0.05,
                          left=0.07, right=0.97)

n_col = 5
n_row = int(np.ceil(len(STATIONS) / n_col))
ts_gs = gridspec.GridSpecFromSubplotSpec(
    n_row, n_col, subplot_spec=outer[0], hspace=0.65, wspace=0.38
)

for idx, stn in enumerate(STATIONS):
    ax  = fig.add_subplot(ts_gs[idx // n_col, idx % n_col])
    d   = station_data[stn]
    col = f"{stn}_v_myr"

    normal  = d[~d["is_outlier"]]
    outlier = d[d["is_outlier"]]

    ax.scatter(normal["start_time"],  normal[col],
               s=2, alpha=0.35, color=COLOR_NORMAL,  linewidths=0, rasterized=True)
    ax.scatter(outlier["start_time"], outlier[col],
               s=6, alpha=0.7,  color=COLOR_OUTLIER, linewidths=0, rasterized=True,
               zorder=3)

    med = d[col].median()
    ax.axhline(med, color=COLOR_MEDIAN, lw=1.2, ls="--", alpha=0.85)

    ax.set_title(stn, fontsize=9, fontweight="bold", color=COLOR_BOX, pad=3)
    ax.set_ylabel("v (m yr⁻¹)", fontsize=7, color="#555")
    ax.tick_params(axis="both", labelsize=6, colors="#555")
    ax.xaxis.set_tick_params(rotation=30)
    ax.set_facecolor("#FAFBFC")
    for spine in ax.spines.values():
        spine.set_edgecolor("#CCCCCC")

    ax.text(0.97, 0.96,
            f"{outlier_pct[stn]:.1f}% outliers",
            transform=ax.transAxes, ha="right", va="top",
            fontsize=6.5, color=COLOR_OUTLIER, fontweight="bold")

fig.text(0.5, outer[0].get_position(fig).y1 + 0.005,
         "Panel 1 — Velocity Time Series (red = IQR outliers, dashed = median)",
         ha="center", fontsize=10, color=COLOR_BOX, fontstyle="italic")

ax2 = fig.add_subplot(outer[1])

box_data = [station_data[s][f"{s}_v_myr"].values for s in STATIONS]
ax2.boxplot(
    box_data,
    tick_labels=STATIONS,
    patch_artist=True,
    showfliers=True,
    flierprops=dict(marker="o", markersize=3, alpha=0.4,
                    markerfacecolor=COLOR_OUTLIER,
                    markeredgecolor=COLOR_OUTLIER),
    medianprops=dict(color=COLOR_MEDIAN, linewidth=2),
    boxprops=dict(facecolor="#D6E8F7", edgecolor=COLOR_BOX, linewidth=1.2),
    whiskerprops=dict(color=COLOR_BOX, linewidth=1, linestyle="--"),
    capprops=dict(color=COLOR_BOX, linewidth=1.5),
)

ax2.set_xlabel("GPS Station", fontsize=10, color=COLOR_BOX)
ax2.set_ylabel("Ice velocity  (m yr⁻¹)", fontsize=10, color=COLOR_BOX)
ax2.set_title("Panel 2 — Box Plots: Velocity Spread & Outliers per Station",
              fontsize=10, color=COLOR_BOX, fontstyle="italic", pad=6)
ax2.tick_params(labelsize=9, colors="#444")
ax2.set_facecolor("#FAFBFC")
ax2.yaxis.grid(True, color="#E0E0E0", linestyle="--", linewidth=0.7)
ax2.set_axisbelow(True)
for spine in ax2.spines.values():
    spine.set_edgecolor("#CCCCCC")

ax3 = fig.add_subplot(outer[2])

pcts   = [outlier_pct[s] for s in STATIONS]
colors = [COLOR_OUTLIER if p > 15 else COLOR_NORMAL for p in pcts]
bars   = ax3.bar(STATIONS, pcts, color=colors, edgecolor="white",
                 linewidth=0.8, width=0.6)

for bar, pct in zip(bars, pcts):
    ax3.text(bar.get_x() + bar.get_width() / 2,
             bar.get_height() + 0.4,
             f"{pct:.1f}%",
             ha="center", va="bottom", fontsize=8,
             color=COLOR_BOX, fontweight="bold")

ax3.axhline(15, color="#888", lw=1.2, ls=":", label="15 % threshold")
ax3.set_xlabel("GPS Station", fontsize=10, color=COLOR_BOX)
ax3.set_ylabel("Outlier fraction (%)", fontsize=10, color=COLOR_BOX)
ax3.set_title("Panel 3 — Outlier Fraction per Station  (red bars > 15 %)",
              fontsize=10, color=COLOR_BOX, fontstyle="italic", pad=6)
ax3.tick_params(labelsize=9, colors="#444")
ax3.set_facecolor("#FAFBFC")
ax3.yaxis.grid(True, color="#E0E0E0", linestyle="--", linewidth=0.7)
ax3.set_axisbelow(True)
ax3.legend(fontsize=8)
for spine in ax3.spines.values():
    spine.set_edgecolor("#CCCCCC")

legend_elements = [
    Line2D([0],[0], marker="o", color="w", markerfacecolor=COLOR_NORMAL,  markersize=7, label="Normal epoch"),
    Line2D([0],[0], marker="o", color="w", markerfacecolor=COLOR_OUTLIER, markersize=7, label="IQR outlier"),
    Line2D([0],[0], color=COLOR_MEDIAN, lw=2, ls="--", label="Station median"),
]
fig.legend(handles=legend_elements, loc="upper right",
           bbox_to_anchor=(0.97, 0.97), fontsize=9,
           framealpha=0.9, edgecolor="#CCCCCC")

plt.savefig(OUTPUT_FIG, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
print(f"\n✓  Figure saved → {OUTPUT_FIG}")
plt.close()