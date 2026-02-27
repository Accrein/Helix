import pandas as pd
import matplotlib.pyplot as plt

# Number of bins
num_bins = 25


path = "C:\\Users\\Lenovo\\Desktop\\Data\\Helix\\Round_2\\heat\\data"

df = pd.read_csv(path + "\\temperature.csv")


# Create distance bins
df["distance_bin"] = pd.cut(df["distance_from_center_km"], bins=num_bins)

# Aggregate means per bin
binned = (
    df.groupby("distance_bin")
    .agg(
        {
            "distance_from_center_km": "mean",
            "avg_temp": "mean",
            "night_temp": "mean",
            "surface_temp": "mean",
        }
    )
    .dropna()
)

# Create panels
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Avg Temp
axes[0].plot(binned["distance_from_center_km"], binned["avg_temp"])
axes[0].set_title("Distance vs Avg Temp")
axes[0].set_xlabel("Distance from Center (km)")
axes[0].set_ylabel("Average Temp (°C)")

# Night Temp
axes[1].plot(binned["distance_from_center_km"], binned["night_temp"])
axes[1].set_title("Distance vs Night Temp")
axes[1].set_xlabel("Distance from Center (km)")
axes[1].set_ylabel("Night Temp (°C)")

# Surface Temp
axes[2].plot(binned["distance_from_center_km"], binned["surface_temp"])
axes[2].set_title("Distance vs Surface Temp")
axes[2].set_xlabel("Distance from Center (km)")
axes[2].set_ylabel("Surface Temp (°C)")

plt.tight_layout()
plt.show()
