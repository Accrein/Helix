import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("seaborn-v0_8")
sns.set_palette("Set2")


path = "C:\\Users\\Lenovo\\Desktop\\Data\\Helix\\Round_2\\heat\\data"

df = pd.read_csv(path + "\\temperature.csv")

x = df["building_density"]
y = df["night_temp"]

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
plt.xlabel("Building Density (%)")
plt.ylabel("Night Temperature (°C)")
plt.title("Building Density vs Night Temperature")

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
