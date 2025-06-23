# Social Media Marketing Impact – From Scroll to Purchase

**"Do likes, platforms, and screen time really influence buying decisions? This project uncovers the behavioral science behind the scroll."**

This project explores how social media habits impact consumers' purchasing decisions using real survey data, Python-based modeling, and Excel output for BI dashboards. It demonstrates how data pipelines, machine learning, and statistical logic can power actionable marketing insights.

---

## Project Objective

To analyze how variables like **social media usage**, **platform type**, **demographics**, and **influence level** affect the likelihood of a consumer making a **purchase decision**.

**Key Research Questions:**
- Does social media usage time correlate with impulsive buying?
- Are some platforms more likely to trigger purchases?
- Do influence levels and mimetic behavior play a role in buyer psychology?
- Which **cities or regions** show higher predicted purchase probabilities?

---

## Project Structure

social-marketing-impact/
├── Socal.py ← Main pipeline & model file
├── Social_Media_Dataset.xlsx ← Raw survey dataset
├── Impulse_Radar_Output.xlsx ← Output Excel with predictions + summary
├── .venv/ ← Virtual environment (not pushed to GitHub)
└── README.md ← This file


## What Was Done

### 1. **Data Cleaning & Preparation**
- Removed duplicate rows
- Handled null values in the `Purchase Decision` column
- Split multi-platform users (e.g., “Instagram; TikTok”) into individual entries using `.explode()`

### 2. **Feature Engineering**
- Defined numerical (`Age`, `Income`, `Usage`) and categorical (`Gender`, `Education`, `Platforms`, `City`) columns
- Mapped target variable (`Purchase Decision`) from “Yes”/“No” → 1/0

### 3. **Model Pipeline**
- Built a `Pipeline` using:
  - `OneHotEncoder` for categorical columns
  - `LogisticRegression` for classification
- Used `ColumnTransformer` to apply appropriate preprocessing steps

### 4. **Prediction**
- Trained the model on the cleaned dataset
- Predicted **purchase probability** for each user
- Aggregated results at **city-level** to identify regional trends

### 5. **Output & Visualization Prep**
- Exported full predictions to `Row_Level` sheet
- Summarized purchase likelihoods by city in `City_Summary` sheet
- Ready for Power BI dashboard visualization

---

## Tools & Libraries

| Tool            | Purpose                         |
|-----------------|----------------------------------|
| **Python 3.12** | Core language                   |
| `pandas`        | Data cleaning & manipulation    |
| `scikit-learn`  | Pipeline + Logistic Regression  |
| `openpyxl`      | Excel read/write                |
| `xlsxwriter`    | Styled Excel output             |
| **Power BI**    | Data dashboard & storytelling   |

---

## Sample Dashboard Use Case

Once the `Impulse_Radar_Output.xlsx` is exported, it can be visualized using:
- KPI cards: Avg. probability of purchase
- Bar charts: Platform-wise or gender-wise impact
- Donut charts: Decision distribution by region
- Funnel: From exposure → trust → decision

---

## Why It Matters

In the age of TikTok trends and Instagram ads, marketing teams need more than intuition — they need **data-driven insight**. This project bridges **data science and marketing** by answering:

- *Where should we spend ad dollars?*
- *Which platforms drive action, not just awareness?*
- *Are certain demographics more susceptible to influence?*
