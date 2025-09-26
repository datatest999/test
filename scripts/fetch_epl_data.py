# extract_epl_data.py

import os
import requests
import pandas as pd

# It's better practice to use environment variables for credentials,
# but for this assignment, we'll define it here.
API_KEY = '12abfbaacdab48bc8948ed6061925e1f'
BASE_URL = 'https://api.football-data.org/v4/'
EPL_CODE = 'PL' # English Premier League

def fetch_epl_standings(season: int) -> pd.DataFrame:
    """
    Fetches the EPL standings for a specific season from the football-data.org API.

    Args:
        season (int): The year the season started (e.g., 2022 for the 2022-23 season).

    Returns:
        pd.DataFrame: A DataFrame containing the standings, or an empty DataFrame on failure.
    """
    endpoint = f"competitions/{EPL_CODE}/standings"
    url = BASE_URL + endpoint
    headers = {'X-Auth-Token': API_KEY}
    params = {'season': season}

    print(f"Fetching data for the {season}-{season+1} season...")

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # This will raise an HTTPError for bad responses (4xx or 5xx)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for season {season}: {e}")
        return pd.DataFrame() # Return an empty DataFrame on error

    # The API returns a JSON object; the actual table is nested inside
    data = response.json()
    standings_data = data.get('standings', [])
    
    if not standings_data or 'table' not in standings_data[0]:
        print(f"Could not find standings table for season {season}")
        return pd.DataFrame()

    # Convert the list of team stats into a DataFrame
    teams_df = pd.DataFrame(standings_data[0]['table'])

    # The 'team' column is a dictionary, so we need to extract the name
    teams_df['team_name'] = teams_df['team'].apply(lambda x: x.get('name'))
    
    return teams_df

def main():
    """
    Main function to extract, transform, and save EPL data for multiple seasons.
    """
    seasons = [2020, 2021, 2022, 2023] # The seasons we need data for
    all_seasons_data = []

    for year in seasons:
        season_df = fetch_epl_standings(year)
        if not season_df.empty:
            season_df['season'] = f"{year}/{year+1}" # Add a season column for context
            all_seasons_data.append(season_df)

    if not all_seasons_data:
        print("No data was fetched. Exiting.")
        return

    # Combine all DataFrames into one
    final_df = pd.concat(all_seasons_data, ignore_index=True)

    # Select and rename the columns to match the KPIs required [cite: 4]
    kpi_df = final_df[[
        'season',
        'position',
        'team_name',
        'playedGames',
        'won',
        'draw',
        'lost',
        'goalsFor',
        'goalsAgainst',
        'goalDifference',
        'points'
    ]]
    
    # Save the final data to a CSV file [cite: 7, 17]
    output_filename = 'epl_standings_2020-2023.csv'
    kpi_df.to_csv(output_filename, index=False)
    print(f"\nSuccessfully saved data to {output_filename}")


if __name__ == "__main__":
    main()