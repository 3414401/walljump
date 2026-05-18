import csv
import json
import urllib.request
from pathlib import Path

GOOGLE_SHEET_CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ28l5NOEwMHCOx3QZS-lZmbukWk___LC5P001mGQVsS5RIgNxprOWCnCg5xaZVX8Xew63Lk0a5lmAO/pub?output=csv"

output_path = Path("data/sheet-data.json")
output_path.parent.mkdir(parents=True, exist_ok=True)

with urllib.request.urlopen(GOOGLE_SHEET_CSV_URL) as response:
    csv_text = response.read().decode("utf-8-sig")

rows = list(csv.DictReader(csv_text.splitlines()))

with output_path.open("w", encoding="utf-8") as f:
    json.dump(rows, f, ensure_ascii=False, indent=2)

print(f"Saved {len(rows)} rows to {output_path}")
