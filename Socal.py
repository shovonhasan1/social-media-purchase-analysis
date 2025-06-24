# 1. Imports
import pandas as pd
from pathlib import Path
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LogisticRegression

# 2. File paths (✅ UPDATED)
DATA_FILE   = Path(r"C:\Users\user\PycharmProjects\social-marketing-impact\Social_Media_Dataset.xlsx")
OUTPUT_FILE = Path(r"C:\Users\user\PycharmProjects\social-marketing-impact\Impulse_Radar_Output.xlsx")

# 3. Column names
TARGET           = "Purchase Decision"      # Yes / No
LOCATION         = "City"

NUMERIC_COLS     = [
    "Age",
    "Income (USD)",
    "Social Media Usage (Hours/Day)",
]

CATEGORICAL_COLS = [
    "Gender",
    "Education Level",
    "Influence Level",
    "Social Media Platforms",
    LOCATION,
]

# 4. Load & basic cleanup
df = pd.read_excel(DATA_FILE).rename(columns=lambda c: c.strip())

# 4A. Deduplicate
df = df.drop_duplicates()

# 5. Drop rows without target label
df = df.dropna(subset=[TARGET])

# 6. Explode multi-platform users
df["Social Media Platforms"] = (
    df["Social Media Platforms"]
      .fillna("")
      .str.split(r"[;,]\s*")
)
df = df.explode("Social Media Platforms")

# 7. Feature / target split
X = df[NUMERIC_COLS + CATEGORICAL_COLS].copy()
y = df[TARGET].map({"Yes": 1, "No": 0})

# 8. OneHotEncoder
try:
    ohe = OneHotEncoder(handle_unknown="ignore", sparse_output=False)  # ≥1.2
except TypeError:
    ohe = OneHotEncoder(handle_unknown="ignore", sparse=False)         # <1.2

# 9. Preprocessing + model pipeline
pre = ColumnTransformer(
    transformers=[
        ("cat", ohe, CATEGORICAL_COLS),
        ("num", "passthrough", NUMERIC_COLS),
    ],
    remainder="drop",
)

model = Pipeline([
    ("prep", pre),
    ("clf",  LogisticRegression(max_iter=1000, n_jobs=-1)),
])

# 10. Fit model
model.fit(X, y)

# 11. Append probability column
df["purchase_prob"] = model.predict_proba(X)[:, 1]

# 12. City-level summary
city_summary = (
    df.groupby(LOCATION)
      .agg(
          Total_Users       = (TARGET, "size"),
          Avg_Purchase_Prob = ("purchase_prob", "mean"),
          Purchases_Yes     = (TARGET, lambda s: (s == "Yes").sum()),
      )
      .reset_index()
      .sort_values("Avg_Purchase_Prob", ascending=False)
)

# 13. Save to Excel
with pd.ExcelWriter(OUTPUT_FILE, engine="xlsxwriter") as writer:
    df.to_excel(writer, index=False, sheet_name="Row_Level")
    city_summary.to_excel(writer, index=False, sheet_name="City_Summary")

print("✅  Finished!  Deduplicated results saved to:", OUTPUT_FILE)
