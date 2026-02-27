import pandas as pd
import numpy as np

# ---------------------------------------
# 1️⃣ Load Data
# ---------------------------------------


path = "C:\\Users\\Lenovo\\Desktop\\Data\\Helix\\Round_2\\heat\\data"
filename = "electricity.csv"
# df = pd.read_csv(path + "\\" + filename)


temperature_df = pd.read_csv(path + "\\temperature.csv")
electricity_df = pd.read_csv(path + "\\electricity.csv")
construction_df = pd.read_csv(path + "\\construction.csv")
budget_df = pd.read_csv(path + "\\city_budget.csv")

# ---------------------------------------
# 2️⃣ Add Year Columns
# ---------------------------------------

temperature_df["date"] = pd.to_datetime(temperature_df["date"])
temperature_df["year"] = temperature_df["date"].dt.year

electricity_df["date"] = pd.to_datetime(electricity_df["date"])
electricity_df["year"] = electricity_df["date"].dt.year

construction_df["date"] = pd.to_datetime(construction_df["date"])
construction_df["year"] = construction_df["date"].dt.year

# ---------------------------------------
# 3️⃣ Temperature Summary
# ---------------------------------------

temp_summary = temperature_df.groupby("year").agg(
    {
        "avg_temp": ["mean", "max", "std"],
        "night_temp": "mean",
        "surface_temp": "mean",
        "humidity": "mean",
        "wind_speed": "mean",
    }
)

temp_summary.columns = ["temp_" + "_".join(col) for col in temp_summary.columns]
temp_summary = temp_summary.reset_index()

# Extreme heat days
heat_threshold = 35
extreme_heat = (
    temperature_df.assign(extreme=temperature_df["avg_temp"] > heat_threshold)
    .groupby("year")["extreme"]
    .sum()
    .reset_index()
    .rename(columns={"extreme": "extreme_heat_days"})
)

# ---------------------------------------
# 4️⃣ Electricity Summary
# ---------------------------------------

elec_summary = (
    electricity_df.groupby("year")
    .agg(
        {
            "residential_kwh": "mean",
            "transformer_load_pct": "mean",
            "outage_minutes": "mean",
        }
    )
    .reset_index()
)

# Transformer stress days
electricity_df["high_stress"] = electricity_df["transformer_load_pct"] > 85

stress_days = (
    electricity_df.groupby("year")["high_stress"]
    .sum()
    .reset_index()
    .rename(columns={"high_stress": "high_stress_days"})
)

# Temperature → Outage slope
slope_results = []

for yr in sorted(electricity_df["year"].unique()):

    df_year = electricity_df[electricity_df["year"] == yr]

    coef = np.polyfit(df_year["avg_temp"], df_year["outage_minutes"], 1)

    slope_results.append({"year": yr, "temp_outage_slope": coef[0]})

slope_df = pd.DataFrame(slope_results)

# ---------------------------------------
# 5️⃣ Construction Summary
# ---------------------------------------

construction_summary = (
    construction_df.groupby("year")
    .agg(
        {
            "active_sites": "mean",
            "construction_area_sq_m": "mean",
            "dust_emission_index": "mean",
        }
    )
    .reset_index()
)

# ---------------------------------------
# 6️⃣ Budget Summary (Already Annual)
# ---------------------------------------

budget_summary = budget_df.copy()

# ---------------------------------------
# 7️⃣ Merge Everything
# ---------------------------------------

master = (
    temp_summary.merge(extreme_heat, on="year", how="left")
    .merge(elec_summary, on="year", how="left")
    .merge(stress_days, on="year", how="left")
    .merge(slope_df, on="year", how="left")
    .merge(construction_summary, on="year", how="left")
    .merge(budget_summary, on="year", how="left")
)

print("\n=== MASTER YEARLY DIAGNOSTIC TABLE ===")
pd.set_option("display.max_columns", None)
# print(master)

print(master.sort_values("year"))
