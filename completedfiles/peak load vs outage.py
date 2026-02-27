import matplotlib.pyplot as plt
import pandas as pd


path = "C:\\Users\\Lenovo\\Desktop\\Data\\Helix\\Round_2\\heat\\data"
filename = "electricity.csv"
df = pd.read_csv(path + "\\" + filename)


num_bins = 25

df["load_bin"] = pd.cut(df["peak_load_kw"], bins=num_bins)

binned = (
    df.groupby("load_bin")
    .agg({"peak_load_kw": "mean", "outage_minutes": "mean"})
    .dropna()
)

plt.figure(figsize=(8, 6))
plt.plot(binned["peak_load_kw"], binned["outage_minutes"])

plt.xlabel("Peak Load (kW)")
plt.ylabel("Outage Minutes")
plt.title("Peak Load vs Outage Minutes (Binned)")

plt.show()
