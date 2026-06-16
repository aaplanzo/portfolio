"""
Veteran Intake Form — Backend
------------------------------
A simple Flask server that receives form submissions
and appends them to a CSV file.
"""

from flask import Flask, request, jsonify, send_from_directory
import csv
import os
from datetime import datetime

app = Flask(__name__, static_folder=".")

CSV_FILE = "submissions.csv"
FIELDS = ["id", "name", "state", "branch", "years_served",
          "disability_rating", "employment_status", "housing_status",
          "benefits_enrolled", "mental_health_services", "date_enrolled"]


def init_csv():
    """Create CSV with headers if it doesn't exist."""
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()


def next_id():
    """Get next sequential ID."""
    if not os.path.exists(CSV_FILE):
        return 1
    with open(CSV_FILE, "r") as f:
        rows = list(csv.DictReader(f))
        return len(rows) + 1


@app.route("/")
def index():
    return send_from_directory(".", "form.html")


@app.route("/submit", methods=["POST"])
def submit():
    data = request.json
    row = {
        "id": next_id(),
        "name": data.get("name", "").strip(),
        "state": data.get("state", "").strip().upper(),
        "branch": data.get("branch", "").strip(),
        "years_served": data.get("years_served", ""),
        "disability_rating": data.get("disability_rating", 0),
        "employment_status": data.get("employment_status", ""),
        "housing_status": data.get("housing_status", ""),
        "benefits_enrolled": data.get("benefits_enrolled", "No"),
        "mental_health_services": data.get("mental_health_services", "No"),
        "date_enrolled": datetime.today().strftime("%Y-%m-%d"),
    }
    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writerow(row)

    return jsonify({"status": "success", "id": row["id"], "name": row["name"]})


@app.route("/submissions", methods=["GET"])
def submissions():
    if not os.path.exists(CSV_FILE):
        return jsonify([])
    with open(CSV_FILE, "r") as f:
        rows = list(csv.DictReader(f))
    return jsonify(rows)


if __name__ == "__main__":
    init_csv()
    print("Running at http://localhost:5000")
    app.run(debug=True)
