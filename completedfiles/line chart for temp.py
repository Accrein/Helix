import pandas as pd
import matplotlib.pyplot as plt


path = "C:\\Users\\Lenovo\\Desktop\\Data\\Helix\\Round_2\\heat\\data"
filename = "temperature.csv"
df = pd.read_csv(path + "\\" + filename)


# Ensure date column is datetime
df["date"] = pd.to_datetime(df["date"])

# Sort by date (very important for time series)
df = df.sort_values("date")

df_monthly = df.set_index("date").resample("M").mean().reset_index()

plt.figure(figsize=(12, 6))

# plt.plot(df["date"], df["avg_temp"], label="Average Temp")
plt.plot(df["date"], df["night_temp"], label="Night Temp")
# plt.plot(df["date"], df["surface_temp"], label="Surface Temp")

plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Monthly Temperature Trends (Smoothed)")
plt.legend()
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()
