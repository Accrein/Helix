import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

path = "C:\\Users\\Lenovo\\Desktop\\Data\\Helix\\Round_2\\heat\\data"

electricity_df = pd.read_csv(path + "\\electricity.csv")
temp_df = pd.read_csv(path + "\\temperature.csv")


# AC sales per neighbourhood
ac_neighbour = electricity_df.groupby("neighbourhood_id")["ac_sales_units"].mean()

# Temperature per neighbourhood
temp_neighbour = temp_df.groupby("neighbourhood_id")["surface_temp"].mean()

# Income (already static)
income_neighbour = temp_df.groupby("neighbourhood_id")["median_income"].mean()

# Merge
ac_analysis = ac_neighbour.to_frame().join(temp_neighbour).join(income_neighbour)
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(9, 6))

# Smaller size scaling
size = ac_analysis["median_income"] / ac_analysis["median_income"].max() * 300

# Generate unique colors using colormap
colors = np.arange(len(ac_analysis))

scatter = plt.scatter(
    ac_analysis["surface_temp"],
    ac_analysis["ac_sales_units"],
    s=size,
    c=colors,
    cmap="tab20",  # good for categorical colors
    alpha=0.7,
)

plt.xlabel("Surface Temperature")
plt.ylabel("AC Sales Units")
plt.title("AC Sales vs Surface Temperature\n(Size = Median Income)")

plt.show()
