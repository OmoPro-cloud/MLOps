import pandas as pd, matplotlib.pyplot as plt, seaborn as sns

# --- Load & prepare ---
df = pd.read_csv("global_temps_extended.csv")

# Ensure lowercase column names
df.columns = [c.strip().lower() for c in df.columns]

# Melt wide format (regions as columns) into long format
df_long = df.melt(id_vars="year", var_name="region", value_name="temp_anomaly")

# Compute rolling 10-year mean per region
df_long["roll_10y"] = (
    df_long.groupby("region")["temp_anomaly"]
    .transform(lambda s: s.rolling(10, min_periods=1).mean())
)

sns.set_theme(style="whitegrid", context="talk")
fig, axes = plt.subplots(2, 2, figsize=(14, 9), constrained_layout=True)
(ax1, ax2), (ax3, ax4) = axes

# (A) Global trend (with rolling mean)
global_df = df_long[df_long["region"] == "global"]
sns.lineplot(data=global_df, x="year", y="temp_anomaly", ax=ax1,
             linewidth=2, label="Annual")
sns.lineplot(data=global_df, x="year", y="roll_10y", ax=ax1,
             linestyle="--", label="10y mean")
ax1.set_title("A) Global Temperature Anomaly Over Time")
ax1.set_xlabel("Year"); ax1.set_ylabel("Δ°C vs baseline")
ax1.grid(True, alpha=0.3); ax1.legend()

# (B) Heatmap of regions × year
pivot = df_long.pivot(index="year", columns="region", values="temp_anomaly")
sns.heatmap(pivot.T, cmap="RdBu_r", center=0, linewidths=.2, ax=ax2)
ax2.set_title("B) Regional Heatmap by Year")
ax2.set_xlabel("Year"); ax2.set_ylabel("Region")

# (C) Decadal distribution (global only)
global_df["decade"] = (global_df["year"] // 10) * 10
sns.boxplot(data=global_df, x="decade", y="temp_anomaly", ax=ax3)
ax3.set_title("C) Decadal Distribution (Global)")
ax3.set_xlabel("Decade"); ax3.set_ylabel("Δ°C")
for label in ax3.get_xticklabels(): label.set_rotation(30)

# (D) Regional trends
sns.lineplot(data=df_long, x="year", y="temp_anomaly", hue="region", ax=ax4)
ax4.set_title("D) Regional Temperature Trends")
ax4.set_xlabel("Year"); ax4.set_ylabel("Δ°C")
ax4.legend(title="Region")

for ax in (ax3, ax4): ax.grid(True, alpha=0.3)

fig.suptitle("Global Temperature Trends Dashboard (Seaborn)", y=1.03, fontsize=18)
plt.savefig("dashboard.png", dpi=200, bbox_inches="tight")
plt.show()