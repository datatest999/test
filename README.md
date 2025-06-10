# EPL Team Performance Summary – 2023

Hey there!

This is a quick data engineering project where I pull English Premier League match data from the [football-data.org](https://www.football-data.org/) API, crunch the numbers, and generate a team performance summary for the 2023 season.

The goal was to calculate how each team did — wins, draws, losses, goals scored, goals conceded — and output all of that to a clean CSV that can be used for visualizations or analysis.

---

##  What this project does

- Connects to the Football Data API
- Fetches all matches from the 2023 EPL season
- Calculates team-level stats:
  - ✅ Wins
  - 🤝 Draws
  - ❌ Losses
  - ⚽ Goals For
  - 🚫 Goals Against
- Saves the data as a `CSV` for BI/analytics use

---

##  Quick note on data

Originally, I was asked to work with **seasons 2020 to 2023**, but the API limits free access to past seasons. I was only able to fetch **2023 match data**, which I used to complete the assignment. The logic is still built to handle multiple seasons if access is expanded.

---

##  Output file

The script creates:
epl_2020_2023_summary.csv

This file has per-team stats for the season. Here's a quick sample:

Team	            Wins	Draws	Losses	Goals For	Goals Against
Arsenal FC	        28	    5	       5	   91	        29
Manchester City FC	28	    7	       3	   96	        34



##  How to run this
1. Clone this repo
-git clone https://github.com/charapy99/test.git
-cd test

2. Create a virtual environment
-python -m venv venv
-venv\Scripts\activate  #for Windows

3. Install dependencies
-pip install -r requirements.txt

4. Run the script
-python fetch_epl_data.py


## Unit testing
This project includes unit tests to verify the correctness of the data transformation logic inside process_matches().

The tests are written using Python's built-in unittest framework and are located in test_processor.py.

Tests included:
1. Basic match logic
Checks that wins, draws, goals for/against are correctly calculated using a couple of matches involving Arsenal.

2. Unfinished matches are skipped
Ensures that matches with status like SCHEDULED or POSTPONED are not included in the stats.

3. Draw match handling
Verifies that both teams are awarded a draw and goals are recorded properly when the match ends in a tie.

4. Cumulative goal tally
Confirms that goals and wins stack up across multiple matches — not overwritten.

5. Teams with no wins
Tests that teams who only lose or draw still appear in the final stats with accurate values.

## Other notes
The API token and auth info are already handled in the script
Everything is modular so you could easily adapt this to other competitions or seasons if you have access

Author
Charan P
📧 charanpy99@gmail.com


# test
football
API:

API initial Url: https://api.football-data.org/

API account name: testing.data999@gmail.com

API token information:

Please modify your client to use a HTTP header named "X-Auth-Token" with the underneath personal token as value. Your token: 12abfbaacdab48bc8948ed6061925e1f
