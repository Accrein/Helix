import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ----------------------------
# 1️⃣ Load Data
# ----------------------------

path = "C:\\Users\\Lenovo\\Desktop\\Data\\Helix\\Round_2\\heat\\data"

main_df = pd.read_csv(path + "\\urban_surface.csv")
air_df = pd.read_csv(path + "\\air_quality.csv")
temp_df = pd.read_csv(path + "\\temperature.csv")
construction_df = pd.read_csv(path + "\\construction.csv")

# ----------------------------
# 2️⃣ Aggregate Structural Data
# ----------------------------

structural = main_df.groupby("neighbourhood_id").agg(
    {
        "building_density": "mean",
        "population_density": "mean",
        "asphalt_pct": "mean",
        "tree_cover_pct": "mean",  # add if available
        "heat_retention_factor": "mean",  # add if available
    }
)

temp = temp_df.groupby("neighbourhood_id").agg(
    {
        "avg_temp": "mean",
        "night_temp": "mean",
        "surface_temp": "mean",
        "urban_heat_index": "mean",
    }
)


# ----------------------------
# 3️⃣ Aggregate Air Quality Data
# ----------------------------

air = air_df.groupby("neighbourhood_id").agg(
    {"aqi": "mean", "pm10": "mean", "pm25": "mean"}
)

# ----------------------------
# 4️⃣ Aggregate Construction Data
# ----------------------------

construction = construction_df.groupby("neighbourhood_id").agg(
    {"dust_emission_index": "mean", "construction_area_sq_m": "sum"}
)

# ----------------------------
# 5️⃣ Merge All Neighbourhood Data
# ----------------------------

neighbour_data = (
    structural.join(air, how="inner")
    .join(construction, how="inner")
    .join(temp, how="inner")
)

# ----------------------------
# 6️⃣ Correlation Matrix
# ----------------------------

plt.figure(figsize=(10, 8))

corr = neighbour_data.corr()

sns.heatmap(corr, annot=True, cmap="coolwarm", center=0, fmt=".2f")

plt.title("Neighbourhood Structural & Environmental Correlation Matrix")
plt.tight_layout()
plt.show()
