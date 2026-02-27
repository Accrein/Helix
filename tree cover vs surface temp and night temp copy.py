import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Number of bins
num_bins = 65

path = "C:\\Users\\Lenovo\\Desktop\\Data\\Helix\\Round_2\\heat\\data"

df = pd.read_csv(path + "\\temperature.csv")

# Create bins
df["tree_bin"] = pd.cut(df["tree_cover_pct"], bins=num_bins)

# Aggregate means per bin
binned = (
    df.groupby("tree_bin")
    .agg(
        {
            "tree_cover_pct": "mean",
            "avg_temp": "mean",
            "night_temp": "mean",
            "surface_temp": "mean",
        }
    )
    .dropna()
)

x = binned["tree_cover_pct"].values

# Fit linear regressions
coef_avg = np.polyfit(x, binned["avg_temp"], 1)
coef_night = np.polyfit(x, binned["night_temp"], 1)
coef_surface = np.polyfit(x, binned["surface_temp"], 1)

# # Predicted lines
# y_avg_pred = np.polyval(coef_avg, x)
# y_night_pred = np.polyval(coef_night, x)
# y_surface_pred = np.polyval(coef_surface, x)

# Plot actual binned lines
plt.figure()
plt.plot(x, binned["avg_temp"], label=f"Average Temperature ({coef_avg[0]:.4f})")
plt.plot(x, binned["night_temp"], label=f"Night Temperature ({coef_night[0]:.4f})")
plt.plot(
    x, binned["surface_temp"], label=f"Surface Temperature ({coef_surface[0]:.4f})"
)

# # Plot regression lines (dashed for distinction)
# plt.plot(x, y_avg_pred, linestyle="--")
# plt.plot(x, y_night_pred, linestyle="--")
# plt.plot(x, y_surface_pred, linestyle="--")

plt.xlabel("Tree Cover Percentage (Binned Mean)")
plt.ylabel("Temperature (°C)")
plt.title("Binned Relationship with Regression Lines")
plt.legend()
plt.show()

# Print regression coefficients
print("Regression Coefficients (Slope, Intercept):")
print(f"Average Temp:     slope = {coef_avg[0]:.4f}, intercept = {coef_avg[1]:.4f}")
print(f"Night Temp:       slope = {coef_night[0]:.4f}, intercept = {coef_night[1]:.4f}")
print(
    f"Surface Temp:     slope = {coef_surface[0]:.4f}, intercept = {coef_surface[1]:.4f}"
)
