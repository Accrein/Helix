import pandas as pd
import statsmodels.api as sm

path = "C:\\Users\\Lenovo\\Desktop\\Data\\Helix\\Round_2\\heat\\data"

temp_df = pd.read_csv(path + "\\temperature.csv")
surface_df = pd.read_csv(path + "\\urban_surface.csv")
air_df = pd.read_csv(path + "\\air_quality.csv")

# Temperature → average UHI per neighbourhood
temp_neighbour = temp_df.groupby("neighbourhood_id").agg({"urban_heat_index": "mean"})

# Urban surface (already structural, but aggregate to be safe)
surface_neighbour = surface_df.groupby("neighbourhood_id").agg(
    {
        "tree_cover_pct": "mean",
        "asphalt_pct": "mean",
        "building_density": "mean",
        "population_density": "mean",
    }
)

# Air quality → average AQI per neighbourhood
air_neighbour = air_df.groupby("neighbourhood_id").agg({"aqi": "mean"})

# Temperature → average UHI per neighbourhood
temp_neighbour = temp_df.groupby("neighbourhood_id").agg({"urban_heat_index": "mean"})

# Urban surface (already structural, but aggregate to be safe)
surface_neighbour = surface_df.groupby("neighbourhood_id").agg(
    {
        "tree_cover_pct": "mean",
        "asphalt_pct": "mean",
        "building_density": "mean",
        "population_density": "mean",
    }
)

# Air quality → average AQI per neighbourhood
air_neighbour = air_df.groupby("neighbourhood_id").agg({"aqi": "mean"})

neighbour_data = temp_neighbour.join(surface_neighbour, how="inner").join(
    air_neighbour, how="inner"
)

# print(neighbour_data.head())

# import matplotlib.pyplot as plt
# import seaborn as sns

# variables = [
#     "building_density",
#     "aqi",
#     "population_density",
#     "asphalt_pct",
#     "tree_cover_pct",
# ]

# plt.figure(figsize=(15, 8))

# for i, var in enumerate(variables, 1):
#     plt.subplot(2, 3, i)

#     sns.scatterplot(data=neighbour_data, x=var, y="urban_heat_index")

#     sns.regplot(
#         data=neighbour_data, x=var, y="urban_heat_index", scatter=False, color="red"
#     )

#     plt.title(f"UHI vs {var}")

# plt.tight_layout()
# plt.show()


import statsmodels.api as sm

# Define X (independent variables)
X = neighbour_data[
    ["building_density", "asphalt_pct", "tree_cover_pct", "population_density", "aqi"]
]

# Define Y (dependent variable)
y = neighbour_data["urban_heat_index"]

# Add constant (important)
X = sm.add_constant(X)

# Fit model
model = sm.OLS(y, X).fit()

# Show summary
print(model.summary())
