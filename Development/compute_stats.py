import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

df = pd.read_csv('Data/Whillians-GPS-Data-and-Features.csv')

df['rolling_mean'] = df['slip_size'].rolling(window=30).mean()
df['rolling_std'] = df['slip_size'].rolling(window=30).std()
df['prior_30_mean'] = df['slip_size'].shift(1).rolling(window=30).mean()

plt.figure(figsize=(12, 10))
numeric_df = df.select_dtypes(include=['number']).dropna()
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.savefig('heatmap.png')

print("--- Pairwise Correlations & P-values ---")
target = 'slip_size'
features = ['tide_height', 'tide_h', 'time_since']

for f in features:
    data = df[[target, f]].dropna()
    r, p = pearsonr(data[target], data[f])
    print(f"{f} vs {target}: r={r:.3f}, p={p:.5e}")

print("Success! Checklist items complete.")
