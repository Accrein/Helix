import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

path = "C:\\Users\\Lenovo\\Desktop\\Data\\Helix\\Round_2\\heat\\data"

surface_df = pd.read_csv(path + "\\temperature.csv")
budget_df = pd.read_csv(path + "\\city_budget.csv")

surface_df["date"] = pd.to_datetime(surface_df["date"], format="mixed")
surface_df["year"] = surface_df["date"].dt.year

tree_cover_year = surface_df.groupby("year")["tree_cover_pct"].mean().reset_index()

tree_budget_year = budget_df[["year", "tree_plantation_budget"]]

tree_analysis = tree_cover_year.merge(tree_budget_year, on="year", how="inner")

print(tree_analysis)

fig, ax1 = plt.subplots(figsize=(8, 5))

# Tree cover (left axis)
ax1.plot(tree_analysis["year"], tree_analysis["tree_cover_pct"], marker="o")
ax1.set_xlabel("Year")
ax1.set_ylabel("Average Tree Cover (%)")

# Budget (right axis)
ax2 = ax1.twinx()
ax2.plot(tree_analysis["year"], tree_analysis["tree_plantation_budget"], marker="s")
ax2.set_ylabel("Tree Plantation Budget")

plt.title("Tree Cover vs Tree Plantation Budget Over Time")
plt.show()
