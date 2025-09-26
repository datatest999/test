# Football Data – EPL Performance Extractor

This project fetches English Premier League (EPL) team performance data 
for the seasons **2020, 2021, 2022, 2023** using the 
[football-data.org API](https://www.football-data.org/).

The output includes:
- Games Played
- Won
- Draw
- Lost
- Goals For
- Goals Against

Results are saved in **CSV** and **Excel** format.

---

## 🚀 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/<your-username>/football.git
   cd football
   ```

2. Create & activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate    # Linux/Mac
   venv\Scripts\activate       # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the script:
   ```bash
   python scripts/fetch_epl_data.py
   ```

   ✅ Output will be in `output/epl_performance.csv` and `output/epl_performance.xlsx`.

---

## 🧪 Run Tests

```bash
pytest
```

---

## 📤 Submission

- Commit your changes:
  ```bash
  git add .
  git commit -m "EPL data extraction scripts and CSV output"
  git push origin main
  ```

- Open a **Pull Request** against the original repo.
