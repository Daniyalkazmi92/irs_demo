# IRS Demo - EIN XML Data Extractor

This Python script extracts officer and preparer information from IRS XML filings based on EIN input.

## 📁 Files Included
- `demo_noapi.py`: Main script that reads EINs and parses officer data from IRS XMLs.
- `sample_input.csv`: Sample CSV input with EINs.
- `demo_output.csv`: Generated output CSV with extracted data.
- `requirements.txt`: Python dependencies.

## ▶️ How to Run

1. Install dependencies:
pip install -r requirements.txt

markdown
Copy
Edit

2. Run the script:
python demo_noapi.py

css
Copy
Edit

3. Output saved to:
demo_output.csv

perl
Copy
Edit

## 🧪 Sample Input Format (sample_input.csv)
```csv
EIN
123456789
987654321
✅ Output Format (demo_output.csv)
Includes: officer name, title, preparer name, firm, filing URL, etc.

🔐 Note
This version does not use the ProPublica API, and works directly with XML links.

✨ Built for a real Upwork demo.
