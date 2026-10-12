
import pandas as pd
from pathlib import Path

project_dir = Path(__file__).resolve().parent.parent
input_file = project_dir / "data" / "raw" / "flight_operations_january_2025.csv"
output_dir = project_dir / "data" / "processed"
output_file = output_dir / "flight_operations_january_2025_clean.csv"

output_dir.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(input_file)

df["FL_DATE"] = pd.to_datetime(df["FL_DATE"], errors="coerce")

df = df.drop_duplicates()

df["CANCELLED"] = df["CANCELLED"].fillna(0).astype(int)
df["DIVERTED"] = df["DIVERTED"].fillna(0).astype(int)

df["IS_CANCELLED"] = df["CANCELLED"]
df["IS_DIVERTED"] = df["DIVERTED"]

df["IS_DEPARTURE_DELAYED"] = (
    df["DEP_DELAY_NEW"].notna() & (df["DEP_DELAY_NEW"] > 0)
).astype(int)

df["IS_ARRIVAL_DELAYED"] = (
    df["ARR_DELAY_NEW"].notna() & (df["ARR_DELAY_NEW"] > 0)
).astype(int)

df["TOTAL_RECORDED_DELAY_CAUSE_MINUTES"] = (
    df[
        [
            "CARRIER_DELAY",
            "WEATHER_DELAY",
            "NAS_DELAY",
            "SECURITY_DELAY",
            "LATE_AIRCRAFT_DELAY",
        ]
    ]
    .fillna(0)
    .sum(axis=1)
)

df.to_csv(output_file, index=False, date_format="%Y-%m-%d")

print("Data cleaning completed.")
print("Records:", len(df))
print("Columns:", len(df.columns))
print("Duplicate rows:", df.duplicated().sum())
print("Processed file:", output_file)
