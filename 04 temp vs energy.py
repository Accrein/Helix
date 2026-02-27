import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Number of bins
num_bins = 65

path = "C:\\Users\\Lenovo\\Desktop\\Data\\Helix\\Round_2\\heat\\data"

df = pd.read_csv(path + "\\electricity.csv")

# Create bins
df["temp_bin"] = pd.cut(df["avg_temp"], bins=num_bins)

# Aggregate means per bin
binned = (
    df.groupby("temp_bin")
    .agg(
        {
            "avg_temp": "mean",
            "residential_kwh": "mean",
            "commercial_kwh": "mean",
            "peak_load_kw": "mean",
            "outage_minutes": "mean",
        }
    )
    .dropna()
)

x = binned["avg_temp"].values

# Fit linear regressions
coef_avg = np.polyfit(x, binned["residential_kwh"], 1)
coef_night = np.polyfit(x, binned["commercial_kwh"], 1)
coef_surface = np.polyfit(x, binned["peak_load_kw"], 1)

# # Predicted lines
# y_avg_pred = np.polyval(coef_avg, x)
# y_night_pred = np.polyval(coef_night, x)
# y_surface_pred = np.polyval(coef_surface, x)

# Plot actual binned lines
plt.figure()
fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.plot(x, binned["residential_kwh"], label=f"Residential kWh ({coef_avg[0]:.4f})")
ax1.plot(x, binned["commercial_kwh"], label=f"Commercial kWh ({coef_night[0]:.4f})")
ax1.plot(x, binned["peak_load_kw"], label=f"Peak Load (kW) ({coef_surface[0]:.4f})")

# # Plot regression lines (dashed for distinction)
# plt.plot(x, y_avg_pred, linestyle="--")
# plt.plot(x, y_night_pred, linestyle="--")
# plt.plot(x, y_surface_pred, linestyle="--")

ax1.set_xlabel("Average Temperature (Binned Mean)")
ax1.set_ylabel("Energy Consumption (kWh/kW)")

ax2 = ax1.twinx()
ax2.plot(
    x, binned["outage_minutes"], label="Outage Minutes", color="red", linestyle="--"
)
ax2.set_ylabel("Outage Minutes")
plt.title("Binned Relationship with Regression Lines")
plt.legend()
plt.show()

# Print regression coefficients
print("Regression Coefficients (Slope, Intercept):")
print(f"Residential kWh:     slope = {coef_avg[0]:.4f}, intercept = {coef_avg[1]:.4f}")
print(
    f"Commercial kWh:       slope = {coef_night[0]:.4f}, intercept = {coef_night[1]:.4f}"
)
print(
    f"Peak Load (kW):     slope = {coef_surface[0]:.4f}, intercept = {coef_surface[1]:.4f}"
)
