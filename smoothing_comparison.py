

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy.ndimage import uniform_filter1d, gaussian_filter1d

df = pd.read_csv("Data/whillans_velocity_slip_merged_wide.csv")
df["start_time"] = pd.to_datetime(df["start_time"])
df = df.sort_values("start_time").reset_index(drop=True)

STATION = "WB08_v_myr"
series = df[STATION].dropna()
times  = df.loc[series.index, "start_time"]
x      = np.arange(len(series))
y      = series.values

WINDOW = 30

def rolling_mean(y, w):
    return pd.Series(y).rolling(w, center=True, min_periods=1).mean().values

def rolling_median(y, w):
    return pd.Series(y).rolling(w, center=True, min_periods=1).median().values

def uniform_box(y, w):
    return uniform_filter1d(y.astype(float), size=w)

def gaussian(y, w):
    sigma = w / 6
    return gaussian_filter1d(y.astype(float), sigma=sigma)

def ewm(y, w):
    return pd.Series(y).ewm(span=w, adjust=False).mean().values

smoothers = {
    "Rolling Mean":   rolling_mean(y, WINDOW),
    "Rolling Median": rolling_median(y, WINDOW),
    "Box (Uniform)":  uniform_box(y, WINDOW),
    "Gaussian":       gaussian(y, WINDOW),
    "Exp. Weighted":  ewm(y, WINDOW),
}

COLORS = ["#E63946", "#2A9D8F", "#E9C46A", "#457B9D", "#A8DADC"]

fig = plt.figure(figsize=(16, 14), facecolor="#0d1117")
fig.suptitle(
    f"Smoothing Technique Comparison  ·  Station {STATION.replace('_v_myr','')}\n"
    "Whillans Ice Stream Background Velocity",
    color="white", fontsize=14, fontweight="bold", y=0.98
)

n = len(smoothers)
gs = gridspec.GridSpec(n + 1, 1, figure=fig, hspace=0.55,
                       top=0.93, bottom=0.06, left=0.08, right=0.97)

ax_overlay = fig.add_subplot(gs[0])
ax_overlay.plot(x, y, color="white", lw=0.5, alpha=0.25, label="Raw")
for (name, sm), col in zip(smoothers.items(), COLORS):
    ax_overlay.plot(x, sm, color=col, lw=1.8, label=name)
ax_overlay.set_title("All Smoothers Overlaid", color="white", fontsize=10, pad=4)
ax_overlay.legend(loc="upper right", fontsize=7.5, ncol=3,
                  framealpha=0.3, labelcolor="white")
ax_overlay.set_facecolor("#161b22")
ax_overlay.tick_params(colors="white", labelsize=8)
for sp in ax_overlay.spines.values():
    sp.set_edgecolor("#30363d")
ax_overlay.set_ylabel("Velocity (m/yr)", color="#8b949e", fontsize=8)

for i, ((name, sm), col) in enumerate(zip(smoothers.items(), COLORS)):
    ax = fig.add_subplot(gs[i + 1])
    residual = y - sm
    ax.fill_between(x, y, sm, where=(residual >= 0),
                    color=col, alpha=0.15, interpolate=True)
    ax.fill_between(x, y, sm, where=(residual < 0),
                    color=col, alpha=0.08, interpolate=True)
    ax.plot(x, y,  color="white", lw=0.5, alpha=0.3, label="Raw")
    ax.plot(x, sm, color=col,     lw=1.6, label=name)
    rmse = np.sqrt(np.mean(residual**2))
    ax.text(0.99, 0.88, f"RMSE vs raw: {rmse:.2f} m/yr",
            transform=ax.transAxes, ha="right", va="top",
            color="white", fontsize=7.5,
            bbox=dict(boxstyle="round,pad=0.3", fc="#21262d", ec=col, lw=0.8))
    ax.set_title(name, color=col, fontsize=9, pad=3, fontweight="bold")
    ax.set_facecolor("#161b22")
    ax.tick_params(colors="white", labelsize=7.5)
    for sp in ax.spines.values():
        sp.set_edgecolor("#30363d")
    ax.set_ylabel("m/yr", color="#8b949e", fontsize=7.5)
    if i == n - 1:
        ax.set_xlabel("Slip-event index", color="#8b949e", fontsize=8)

fig.savefig("smoothing_comparison.png", dpi=150, bbox_inches="tight",
            facecolor=fig.get_facecolor())
plt.close()
print("Saved → smoothing_comparison.png")
