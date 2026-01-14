# ------------------------------------------------------------
# Temperature Analysis Program  for  Australian Weather Stations
# ( It is adapted for wide-format monthly mean maximum temperature files)
# ------------------------------------------------------------
import os
import pandas as pd
import numpy as np

# ------------------------------------------------------------
# Folder which contains CSV files
# ------------------------------------------------------------
FOLDER_PATH = r"C:\Users\bijen\Downloads\temperatures"

if not os.path.exists(FOLDER_PATH):
    raise FileNotFoundError("Temperatures folder not found!")

# ------------------------------------------------------------
# Australian seasons  for (Southern Hemisphere)
# ------------------------------------------------------------
SEASONS = {
    "Summer": [12, 1, 2],   # Dec, Jan, Feb
    "Autumn": [3, 4, 5],
    "Winter": [6, 7, 8],
    "Spring": [9, 10, 11]
}

# Month name which will be used for number mapping
MONTH_MAP = {
    'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
    'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12
}

seasonal_data = {season: [] for season in SEASONS}
station_temps = {}          # station → list of monthly temperatures
station_names = {}          # station_id → name (for nicer output)

# ------------------------------------------------------------
# Processing  all CSV files in the folder
# ------------------------------------------------------------
for filename in os.listdir(FOLDER_PATH):
    if filename.lower().endswith(".csv"):
        file_path = os.path.join(FOLDER_PATH, filename)
        df = pd.read_csv(file_path)

        # Columns which is expected
        required = ['STN_ID', 'STATION_NAME']
        month_cols = [c for c in df.columns if c in MONTH_MAP]
        if not all(r in df.columns for r in required) or not month_cols:
            print(f"Skipping {filename} - missing STN_ID / STATION_NAME or month columns")
            continue

        # Keeping  only relevant columns
        df = df[['STN_ID', 'STATION_NAME'] + month_cols].copy()

        # Melt wide  which is done for long format
        df_long = pd.melt(
            df,
            id_vars=['STN_ID', 'STATION_NAME'],
            value_vars=month_cols,
            var_name='month_name',
            value_name='temp'
        )

        # Adding  numeric month
        df_long['month'] = df_long['month_name'].map(MONTH_MAP)

        # Droping  any rows which is  missing temperature
        df_long = df_long.dropna(subset=['temp'])

        # Store station name which is take first occurrence
        for st_id, name in df_long[['STN_ID', 'STATION_NAME']].drop_duplicates().itertuples(index=False):
            station_names[st_id] = name

        # Collecting  all temperatures per season  which is for grand mean approach
        for season, months in SEASONS.items():
            season_rows = df_long[df_long['month'].isin(months)]
            seasonal_data[season].extend(season_rows['temp'].tolist())

        # Collecting temperatures per station
        for st_id, group in df_long.groupby('STN_ID'):
            if st_id not in station_temps:
                station_temps[st_id] = []
            station_temps[st_id].extend(group['temp'].tolist())

# ------------------------------------------------------------
# Stats which is for Summary
# ------------------------------------------------------------
total_stations = len(station_temps)
total_values = sum(len(temps) for temps in station_temps.values())
print(f"Processed {total_stations} stations with {total_values:,} monthly values.")

if total_stations == 0:
    print("No valid data found.")
    exit()

# ------------------------------------------------------------
# 1. grand mean across all stations/months (Seasonal Average Output) 
# ------------------------------------------------------------
with open("average_temp.txt", "w", encoding="utf-8") as f:
    f.write("Average monthly mean maximum temperature (°C) - all stations combined\n")
    f.write("---------------------------------------------------------------\n")
    for season, temps in seasonal_data.items():
        if temps:
            mean_temp = np.mean(temps)
            count = len(temps)
            f.write(f"{season}: {mean_temp:.1f}°C  (based on {count} monthly values)\n")
        else:
            f.write(f"{season}: no data\n")

# ------------------------------------------------------------
# 2. Across all monthly means of a station(Largest Temperature Range) 
# ------------------------------------------------------------
ranges = {}
for st_id, temps in station_temps.items():
    if len(temps) < 2:
        continue
    max_t = max(temps)
    min_t = min(temps)
    rng = max_t - min_t
    ranges[st_id] = (rng, max_t, min_t, len(temps))

if ranges:
    largest_range = max(r[0] for r in ranges.values())

    with open("largest_temp_range_station.txt", "w", encoding="utf-8") as f:
        f.write("Station(s) with largest range in monthly mean maximum temperatures\n")
        f.write("-------------------------------------------------------------------\n")
        for st_id, (rng, max_t, min_t, count) in ranges.items():
            if rng == largest_range:
                name = station_names.get(st_id, str(st_id))
                f.write(f"Station {st_id} ({name}): Range {rng:.1f}°C  "
                        f"(Max: {max_t:.1f}°C, Min: {min_t:.1f}°C, {count} months)\n")

# ------------------------------------------------------------
# 3. Standard deviation of monthly means(Temperature Stability)
# ------------------------------------------------------------
std_devs = {}
for st_id, temps in station_temps.items():
    if len(temps) >= 2:
        std_devs[st_id] = np.std(temps, ddof=1)   # sample std dev

if std_devs:
    min_std = min(std_devs.values())
    max_std = max(std_devs.values())

    with open("temperature_stability_stations.txt", "w", encoding="utf-8") as f:
        f.write("Temperature stability - monthly mean maximum temperatures\n")
        f.write("----------------------------------------------------------\n")
        for st_id, std in std_devs.items():
            name = station_names.get(st_id, str(st_id))
            if std == min_std:
                f.write(f"Most stable: Station {st_id} ({name}) → StdDev {std:.1f}°C\n")
        for st_id, std in std_devs.items():
            if std == max_std:
                name = station_names.get(st_id, str(st_id))
                f.write(f"Most variable: Station {st_id} ({name}) → StdDev {std:.1f}°C\n")
