import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("seaborn-v0_8")
sns.set_palette("Set2")
# df = pd.read_csv("temperature.csv")


path = "C:\\Users\\Lenovo\\Desktop\\Data\\Helix\\Round_2\\heat\\data"

df = pd.read_csv(path + "\\temperature.csv")
# # print(df.columns)
# # plt.scatter(df["tree_cover_pct"], df["surface_temp"], alpha=0.02, s=10)
# # plt.xlabel("Tree Cover")
# # plt.ylabel("Surface Temperature")
# # plt.title("Title")
# # plt.show()
# plt.hexbin(df["tree_cover_pct"], df["surface_temp"], gridsize=40, cmap="magma")
# plt.colorbar(label="Count")


# # Linear regression (least squares)
# m, b = np.polyfit(df["tree_cover_pct"], df["surface_temp"], 1)

# # Correlation coefficient
# r = np.corrcoef(df["tree_cover_pct"], df["surface_temp"])[0, 1]

# plt.show()


x = df["tree_cover_pct"]
y = df["surface_temp"]

# Fit regression
m, b = np.polyfit(x, y, 1)
r = np.corrcoef(x, y)[0, 1]

plt.figure(figsize=(8, 6))

# Hexbin
plt.hexbin(x, y, gridsize=60, bins="log", cmap="viridis")
plt.colorbar(label="log10(Count)")

# Regression line
x_line = np.linspace(x.min(), x.max(), 100)
y_line = m * x_line + b
plt.plot(x_line, y_line, color="red", linewidth=2)

# Labels
plt.xlabel("Tree Cover (%)")
plt.ylabel("Surface Temperature (°C)")
plt.title("Tree Cover vs Surface Temperature")

# Add correlation text
plt.text(
    0.05,
    0.95,
    f"r = {r:.3f}",
    transform=plt.gca().transAxes,
    verticalalignment="top",
    fontsize=12,
    bbox=dict(facecolor="white", alpha=0.7),
)

plt.show()
