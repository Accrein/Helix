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

import numpy as np

median_income_value = ac_analysis["median_income"].median()

ac_analysis["income_group"] = np.where(
    ac_analysis["median_income"] >= median_income_value, "High Income", "Low Income"
)

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))

sns.scatterplot(
    data=ac_analysis, x="surface_temp", y="ac_sales_units", hue="income_group"
)

sns.regplot(
    data=ac_analysis[ac_analysis["income_group"] == "Low Income"],
    x="surface_temp",
    y="ac_sales_units",
    scatter=False,
    label="Low Income",
)

sns.regplot(
    data=ac_analysis[ac_analysis["income_group"] == "High Income"],
    x="surface_temp",
    y="ac_sales_units",
    scatter=False,
    label="High Income",
)

plt.title("AC Sales vs Temperature by Income Group")
plt.xlabel("Surface Temperature")
plt.ylabel("AC Sales Units")
plt.show()
