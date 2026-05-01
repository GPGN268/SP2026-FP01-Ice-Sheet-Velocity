import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

DATA_FILE  = "Data/prefilter_summary.csv"
OUTPUT_DIR = "figures"
OUTPUT_FIG = os.path.join(OUTPUT_DIR, "figure1_position_quality.png")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MIN_EPOCHS = 1000

df = pd.read_csv(DATA_FILE)
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.to_period("M")

print(f"Loaded {len(df):,} station-days across {df['station'].nunique()} stations")
print(f"Columns: {df.columns.tolist()}")

pct_kept = 100 * (df["n_retained"] >= MIN_EPOCHS).sum() / len(df)
print(f"Station-days above {MIN_EPOCHS} epoch minimum: {pct_kept:.1f}%")

fig, axes = plt.subplots(
    1, 2, figsize=(16, 7), facecolor="#F7F9FC",
    gridspec_kw={"width_ratios": [1.6, 1], "wspace": 0.4},
)

fig.suptitle(
    "Figure 1  –  GPS Data Quality Assessment\n"
    "Whillans Ice Stream GPS Network  |  Epoch Retention",
    fontsize=13, fontweight="bold", color="#2C3E50", y=1.01,
)

# ── Panel A: heatmap of retained epochs per station per month ─────────────────
ax = axes[0]

pivot = df.pivot_table(
    index="station", columns="month", values="n_retained", aggfunc="sum"
)
pivot = pivot.sort_index()

months = [str(m) for m in pivot.columns]
stations = pivot.index.tolist()
data = pivot.values

im = ax.imshow(data, aspect="auto", cmap="YlGnBu", interpolation="nearest")

cbar = fig.colorbar(im, ax=ax, fraction=0.03, pad=0.02)
cbar.set_label("Retained epochs per month", fontsize=9, color="#444")
cbar.ax.tick_params(labelsize=7)

ax.set_yticks(range(len(stations)))
ax.set_yticklabels(stations, fontsize=6.5)

step = max(1, len(months) // 12)
ax.set_xticks(range(0, len(months), step))
ax.set_xticklabels([months[i] for i in range(0, len(months), step)],
                   rotation=45, ha="right", fontsize=7)

ax.set_xlabel("Month", fontsize=10, color="#444")
ax.set_ylabel("Station", fontsize=10, color="#444")
ax.set_title("(a)  Retained epochs per station per month",
             fontsize=10, color="#2C3E50", fontstyle="italic", pad=6)

# ── Panel B: histogram of epoch counts per station-day ───────────────────────
ax2 = axes[1]
ax2.set_facecolor("#FAFBFC")
for spine in ax2.spines.values():
    spine.set_edgecolor("#CCCCCC")

bins = np.linspace(0, df["n_total"].max() * 1.05, 50)

kept    = df[df["n_retained"] >= MIN_EPOCHS]["n_retained"]
dropped = df[df["n_retained"] <  MIN_EPOCHS]["n_retained"]

ax2.hist(kept, bins=bins, color="#4A90D9", alpha=0.85,
         edgecolor="white", linewidth=0.4, label=f"Kept  (≥{MIN_EPOCHS} epochs)")
if len(dropped) > 0:
    ax2.hist(dropped, bins=bins, color="#E84855", alpha=0.8,
             edgecolor="white", linewidth=0.4, label=f"Dropped  (<{MIN_EPOCHS} epochs)")

ax2.axvline(MIN_EPOCHS, color="#F5A623", linewidth=2.0,
            linestyle="--", label=f"{MIN_EPOCHS}-epoch minimum")

ymax = ax2.get_ylim()[1]
ax2.text(MIN_EPOCHS + 50, ymax * 0.85,
         f"{pct_kept:.1f}% of\nstation-days kept",
         fontsize=9, color="#2C3E50", fontweight="bold", va="top")

ax2.set_xlabel("Epochs per station-day", fontsize=10, color="#444")
ax2.set_ylabel("Number of station-days", fontsize=10, color="#444")
ax2.set_title("(b)  Epoch count distribution  |  1000-epoch minimum",
              fontsize=10, color="#2C3E50", fontstyle="italic", pad=6)
ax2.tick_params(labelsize=8, colors="#555")
ax2.yaxis.grid(True, color="#E0E0E0", linestyle="--", linewidth=0.6)
ax2.set_axisbelow(True)
ax2.legend(fontsize=8, framealpha=0.9, edgecolor="#CCCCCC")

plt.savefig(OUTPUT_FIG, dpi=200, bbox_inches="tight", facecolor=fig.get_facecolor())
print(f"\n✓  Figure saved → {OUTPUT_FIG}")
plt.close()