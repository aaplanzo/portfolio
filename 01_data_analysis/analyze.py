"""
Veteran Services Data Analysis
-------------------------------
Cleans and analyzes a dataset of veterans enrolled in support services.
Outputs summary statistics and key insights.
"""

import pandas as pd


# ── 1. LOAD ──────────────────────────────────────────────────────────────────

df = pd.read_csv("veteran_services.csv")
print(f"Loaded {len(df)} records.\n")


# ── 2. CLEAN ─────────────────────────────────────────────────────────────────

# Standardize text columns
for col in ["state", "branch", "employment_status", "housing_status", "benefits_enrolled", "mental_health_services"]:
    df[col] = df[col].str.strip().str.title()

# Convert date
df["date_enrolled"] = pd.to_datetime(df["date_enrolled"])

# Fill missing income for unemployed (already 0, but make explicit)
df["annual_income"] = df["annual_income"].fillna(0)

# Flag records with high need (unemployed + unstable housing)
df["high_need"] = (
    (df["employment_status"] == "Unemployed") &
    (df["housing_status"] == "Unstable")
)

print("Data cleaned.\n")


# ── 3. ANALYZE ───────────────────────────────────────────────────────────────

print("=" * 50)
print("SUMMARY STATISTICS")
print("=" * 50)

# Employment breakdown
print("\nEmployment Status Breakdown:")
print(df["employment_status"].value_counts().to_string())

# Benefits enrollment rate
enrolled = df["benefits_enrolled"].value_counts(normalize=True) * 100
print(f"\nBenefits Enrollment Rate: {enrolled.get('Yes', 0):.1f}%")

# Mental health services
mh = df["mental_health_services"].value_counts(normalize=True) * 100
print(f"Mental Health Services Access: {mh.get('Yes', 0):.1f}%")

# Average disability rating by employment status
print("\nAvg Disability Rating by Employment Status:")
print(df.groupby("employment_status")["disability_rating"].mean().round(1).to_string())

# Average income by branch
print("\nAvg Annual Income by Branch:")
print(df.groupby("branch")["annual_income"].mean().round(0).astype(int).to_string())

# High need veterans
high_need_count = df["high_need"].sum()
print(f"\nHigh-Need Veterans (Unemployed + Unstable Housing): {high_need_count} ({high_need_count/len(df)*100:.1f}%)")

# Florida-specific (relevant to host org placement)
fl = df[df["state"] == "Fl"]
print(f"\nFlorida Veterans in Dataset: {len(fl)}")
print(f"  - High Need: {fl['high_need'].sum()}")
print(f"  - Benefits Enrolled: {fl['benefits_enrolled'].value_counts().get('Yes', 0)}")

print("\n" + "=" * 50)
print("Analysis complete.")
print("=" * 50)
