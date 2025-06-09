import pandas as pd
from datasources.ingest import DataIngestor

class CompetitionJob:
    def __init__(self, config_class):
        # Initialize DataIngestor with the given config class
        self.ingestor = DataIngestor(config_class)

    def run(self, csv_path="test\competitions.csv"):
        try:
            # Fetch data from the API
            data = self.ingestor.fetch_competitions()
            if not data or "competitions" not in data:
                print("No competition data found.")
                return

            # Transform data: extract relevant fields from each competition
            competitions = data["competitions"]
            records = []
            for comp in competitions:
                records.append({
                    "id": comp.get("id"),
                    "name": comp.get("name"),
                    "area": comp.get("area", {}).get("name"),
                    "code": comp.get("code"),
                    "plan": comp.get("plan"),
                    "currentSeasonStartDate": comp.get("currentSeason", {}).get("startDate"),
                    "currentSeasonEndDate": comp.get("currentSeason", {}).get("endDate"),
                })

            # Convert to DataFrame and save as CSV
            df = pd.DataFrame(records)
            df.to_csv(csv_path, index=False)
            print(f"Competitions data saved to {csv_path}")
        except pd.errors.EmptyDataError:
            print("Error: No data to write to CSV.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")