import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Number of bins
num_bins = 65

path = "C:\\Users\\Lenovo\\Desktop\\Data\\Helix\\Round_2\\heat\\data"

df = pd.read_csv(path + "\\temperature.csv")

# Create bins
df["building_density_bin"] = pd.cut(df["building_density"], bins=num_bins)

# Aggregate means per bin
binned = (
    df.groupby("building_density_bin")
    .agg(
        {
            "building_density": "mean",
            "avg_temp": "mean",
            "night_temp": "mean",
            "surface_temp": "mean",
        }
    )
    .dropna()
)

x = binned["building_density"].values

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

plt.xlabel("Building Density (Binned Mean)")
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

print(df[["building_density", "distance_from_center_km"]].corr())
print(df[["distance_from_center_km", "avg_temp"]].corr())

# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np

# path = "C:\\Users\\Lenovo\\Desktop\\Data\\Helix\\Round_2\\heat\\data"
# filename = "temperature.csv"
# df = pd.read_csv(path + "\\" + filename)


# df["building_density_pct"] = df["building_density"] * 100

# df["density_bin"] = pd.cut(df["building_density_pct"], bins=25)

# binned = (
#     df.groupby("density_bin")
#     .agg(
#         {
#             "building_density_pct": "mean",
#             "avg_temp": "mean",
#             "night_temp": "mean",
#             "surface_temp": "mean",
#         }
#     )
#     .dropna()
# )

# fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# axes[0].plot(binned["building_density_pct"], binned["avg_temp"])
# axes[0].set_title("Density (%) vs Avg Temp")

# axes[1].plot(binned["building_density_pct"], binned["night_temp"])
# axes[1].set_title("Density (%) vs Night Temp")

# axes[2].plot(binned["building_density_pct"], binned["surface_temp"])
# axes[2].set_title("Density (%) vs Surface Temp")

# plt.tight_layout()
# plt.show()
