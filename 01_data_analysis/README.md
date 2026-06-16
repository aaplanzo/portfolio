[README.md](https://github.com/user-attachments/files/29004011/README.md)
# Veteran Services Data Analysis

A Python script that cleans and analyzes a dataset of veterans enrolled in support services.

## What it does
- Loads and cleans raw CSV data (standardizes text, parses dates, fills missing values)
- Flags high-need veterans (unemployed + unstable housing)
- Outputs summary statistics: employment breakdown, benefits enrollment, disability ratings, income by branch, and state-level filters

## How to run

```bash
pip install pandas
python analyze.py
```

## Files
- `veteran_services.csv` — sample dataset (20 veterans)
- `analyze.py` — cleaning and analysis script

## Sample Output
```
Employment Status Breakdown:
Employed         11
Unemployed        6
Underemployed     3

Benefits Enrollment Rate: 75.0%
Mental Health Services Access: 60.0%
High-Need Veterans: 6 (30.0%)
```
