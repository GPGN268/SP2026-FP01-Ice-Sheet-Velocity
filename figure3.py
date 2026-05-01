import pandas as pd
df = pd.read_csv('Data/ppp_velocity_timeseries.csv', parse_dates=['timestamp'])
print(df.columns.tolist())
print(df.head(3))
print(df['station'].unique())
import pandas as pd
df = pd.read_csv('Data/ppp_velocity_timeseries.csv', parse_dates=['timestamp'])
print(df.columns.tolist())
print(df.head(3).to_string())
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE  = "Data/ppp_velocity_timeseries.csv"
OUTPUT_DIR = "figures"
OUTPUT_FIG = os.path.join(OUTPUT_DIR, "figure3_velocity_smoothing.png")
os.makedirs(OUTPUT_DIR, exist_ok=True)

STATION = "gz01"

df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])
df = df[df["station"] == STATION].dropna(subset=["v"]).sort_values("timestamp").reset_index(drop=True)

daily_median = df["v"]
rolling_30d  = df["v_30d"]
timestamps   = df["timestamp"]

noise_daily   = daily_median.std()
noise_30d     = rolling_30d.std()

fig, axes = plt.subplots(3, 1, figsize=(14, 12), facecolor="#F7F9FC", sharex=True)
fig.suptitle(
    f"Figure 3  –  Velocity Smoothing Comparison  |  Station {STATION.upper()}\n"
    "Inter-epoch velocity  →  Daily median  →  30-day rolling median",
    fontsize=13, fontweight="bold", color="#2C3E50", y=1.01,
)

plt.subplots_adjust(hspace=0.35)

ax1 = axes[0]
ax1.set_facecolor("#FAFBFC")
for spine in ax1.spines.values():
    spine.set_edgecolor("#CCCCCC")
ax1.scatter(timestamps, daily_median, s=3, alpha=0.8, color="#1a1a2e",
            linewidths=0, rasterized=True)
ax1.set_ylabel("Velocity  (m yr⁻¹)", fontsize=10, color="#444")
ax1.set_title("(a)  Daily velocity estimates", fontsize=10,
              color="#2C3E50", fontstyle="italic", pad=6)
ax1.tick_params(labelsize=8, colors="#555")
ax1.yaxis.grid(True, color="#E0E0E0", linestyle="--", linewidth=0.6)
ax1.set_axisbelow(True)
ax1.text(0.01, 0.97, f"σ = {noise_daily:.2f} m yr⁻¹",
         transform=ax1.transAxes, fontsize=9, va="top",
         color="#E84855", fontweight="bold")

ax2 = axes[1]
ax2.set_facecolor("#FAFBFC")
for spine in ax2.spines.values():
    spine.set_edgecolor("#CCCCCC")
ax2.plot(timestamps, daily_median, color="#4A90D9", lw=1.0, alpha=0.5, label="Daily")
ax2.plot(timestamps, daily_median.rolling(7, center=True).median(),
         color="#F5A623", lw=1.8, label="7-day rolling median")
ax2.set_ylabel("Velocity  (m yr⁻¹)", fontsize=10, color="#444")
ax2.set_title("(b)  Daily median velocity", fontsize=10,
              color="#2C3E50", fontstyle="italic", pad=6)
ax2.tick_params(labelsize=8, colors="#555")
ax2.yaxis.grid(True, color="#E0E0E0", linestyle="--", linewidth=0.6)
ax2.set_axisbelow(True)
ax2.legend(fontsize=8, framealpha=0.9, edgecolor="#CCCCCC")
ax2.text(0.01, 0.97, f"σ = {daily_median.rolling(7, center=True).median().std():.2f} m yr⁻¹",
         transform=ax2.transAxes, fontsize=9, va="top",
         color="#E84855", fontweight="bold")

ax3 = axes[2]
ax3.set_facecolor("#FAFBFC")
for spine in ax3.spines.values():
    spine.set_edgecolor("#CCCCCC")
ax3.plot(timestamps, rolling_30d, color="#2ECC71", lw=2.0, label="30-day rolling median")
ax3.set_ylabel("Velocity  (m yr⁻¹)", fontsize=10, color="#444")
ax3.set_xlabel("Date", fontsize=10, color="#444")
ax3.set_title("(c)  30-day rolling median velocity", fontsize=10,
              color="#2C3E50", fontstyle="italic", pad=6)
ax3.tick_params(labelsize=8, colors="#555")
ax3.tick_params(axis="x", rotation=30)
ax3.yaxis.grid(True, color="#E0E0E0", linestyle="--", linewidth=0.6)
ax3.set_axisbelow(True)
ax3.legend(fontsize=8, framealpha=0.9, edgecolor="#CCCCCC")
ax3.text(0.01, 0.97, f"σ = {noise_30d:.2f} m yr⁻¹",
         transform=ax3.transAxes, fontsize=9, va="top",
         color="#E84855", fontweight="bold")

plt.savefig(OUTPUT_FIG, dpi=200, bbox_inches="tight", facecolor=fig.get_facecolor())
print(f"✓  Figure saved → {OUTPUT_FIG}")
plt.close()