import requests
import pandas as pd

def main():
    API_TOKEN = "12abfbaacdab48bc8948ed6061925e1f"
    HEADERS = {"X-Auth-Token": API_TOKEN}
    BASE_URL = "https://api.football-data.org/v4/competitions/PL/matches"
    seasons = [2020, 2021, 2022, 2023]  # Only 2023 available in free tier

    all_matches = []

    for season in seasons:
        print(f"👉 Fetching EPL matches for season {season}...")
        try:
            response = requests.get(BASE_URL, headers=HEADERS, params={"season": season})
            if response.status_code == 200:
                data = response.json()
                matches = data.get("matches", [])
                print(f"✅ {len(matches)} matches fetched for {season}")
                all_matches.extend(matches)
            else:
                print(f"⚠️ Could not fetch season {season}: {response.status_code}")
        except Exception as e:
            print(f"❌ Error fetching season {season}: {e}")

    if not all_matches:
        print("🚫 No match data fetched. Exiting.")
        return

    print("🛠️ Processing match data...")

    team_stats = process_matches(all_matches)

    # Export
    df = pd.DataFrame.from_dict(team_stats, orient='index').reset_index().rename(columns={'index': 'Team'})
    try:
        df.to_csv("epl_2020_2023_summary.csv", index=False)
        print("📁 Saved summary to 'epl_2023_summary.csv'")
    except PermissionError:
        print("🚫 Could not save CSV — please close the file if it's open and try again.")


def process_matches(matches):
    stats = {}
    for match in matches:
        if match['status'] != "FINISHED":
            continue

        home = match['homeTeam']['name']
        away = match['awayTeam']['name']
        h_goals = match['score']['fullTime']['home']
        a_goals = match['score']['fullTime']['away']
        winner = match['score']['winner']

        for team in [home, away]:
            if team not in stats:
                stats[team] = {'Wins': 0, 'Draws': 0, 'Losses': 0, 'Goals For': 0, 'Goals Against': 0}

        stats[home]['Goals For'] += h_goals
        stats[home]['Goals Against'] += a_goals
        stats[away]['Goals For'] += a_goals
        stats[away]['Goals Against'] += h_goals

        if winner == "HOME_TEAM":
            stats[home]['Wins'] += 1
            stats[away]['Losses'] += 1
        elif winner == "AWAY_TEAM":
            stats[away]['Wins'] += 1
            stats[home]['Losses'] += 1
        else:
            stats[home]['Draws'] += 1
            stats[away]['Draws'] += 1

    return stats

if __name__ == "__main__":
    main()
