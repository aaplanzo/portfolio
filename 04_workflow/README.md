# Veteran Intake Form → CSV Pipeline

A web form that collects veteran service intake data and saves it to a CSV file via a Python Flask backend.

## What it does
- Front-end form collects name, branch, state, employment, housing, and services data
- Submits to a local Flask API endpoint
- Backend appends each submission as a new row in `submissions.csv`
- Live table on the page shows all submissions

## How to run

```bash
pip install flask
python app.py
```

Then open http://localhost:5000 in your browser.

## Files
- `app.py` — Flask backend with `/submit` and `/submissions` endpoints
- `form.html` — Front-end intake form
- `submissions.csv` — Auto-generated on first submission

## Tech
- Python / Flask
- HTML / CSS / JavaScript
- CSV (stdlib)
