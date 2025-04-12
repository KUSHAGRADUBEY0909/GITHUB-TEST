import pandas as pd
import os

# ✅ Step 1: List all input files
files = [
    "mutual_funds_data.json",
    "mf_holdings_data.json",
    "stock_data.json"
]

dfs = []

# ✅ Step 2: Load each file (NDJSON)
for file in files:
    if os.path.exists(file):
        print(f"📥 Reading {file}...")
        df = pd.read_json(file, lines=True)
        dfs.append(df)
    else:
        print(f"⚠️ Skipping {file} (not found)")

# ✅ Step 3: Combine all dataframes
df_combined = pd.concat(dfs, ignore_index=True)

# ✅ Step 4: Drop duplicates based on schemeName
if "schemeName" in df_combined.columns:
    df_combined.drop_duplicates(subset="schemeName", inplace=True)
else:
    print("⚠️ 'schemeName' column not found. No deduplication applied.")

# ✅ Step 5: Save to a new combined JSON file
output_file = "all_funds_combined.json"
df_combined.to_json(output_file, orient="records", lines=True)

print(f"\n✅ Done! Combined data saved to {output_file}")
print(f"🔢 Total rows: {len(df_combined)}")
