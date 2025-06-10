import unittest
from fetch_epl_data import process_matches

class TestTeamStatsProcessing(unittest.TestCase):

    def test_basic_stats_for_arsenal(self):
        print("\n✅ Running: test_basic_stats_for_arsenal")
        matches = [
            {
                "status": "FINISHED",
                "homeTeam": {"name": "Arsenal FC"},
                "awayTeam": {"name": "Chelsea FC"},
                "score": {
                    "fullTime": {"home": 2, "away": 1},
                    "winner": "HOME_TEAM"
                }
            },
            {
                "status": "FINISHED",
                "homeTeam": {"name": "Arsenal FC"},
                "awayTeam": {"name": "Liverpool FC"},
                "score": {
                    "fullTime": {"home": 1, "away": 1},
                    "winner": "DRAW"
                }
            }
        ]
        stats = process_matches(matches)
        print("→ Arsenal Stats:", stats["Arsenal FC"])
        self.assertEqual(stats["Arsenal FC"]["Wins"], 1)
        self.assertEqual(stats["Arsenal FC"]["Draws"], 1)
        self.assertEqual(stats["Arsenal FC"]["Goals For"], 3)
        self.assertEqual(stats["Arsenal FC"]["Goals Against"], 2)

    def test_skips_unfinished_matches(self):
        print("\n✅ Running: test_skips_unfinished_matches")
        matches = [
            {
                "status": "SCHEDULED",
                "homeTeam": {"name": "Leeds United"},
                "awayTeam": {"name": "Everton FC"},
                "score": {
                    "fullTime": {"home": 0, "away": 0},
                    "winner": None
                }
            }
        ]
        stats = process_matches(matches)
        print("→ Stats (should be empty):", stats)
        self.assertNotIn("Leeds United", stats)
        self.assertNotIn("Everton FC", stats)

    def test_draw_match_processing(self):
        print("\n✅ Running: test_draw_match_processing")
        matches = [
            {
                "status": "FINISHED",
                "homeTeam": {"name": "Brighton FC"},
                "awayTeam": {"name": "Wolves FC"},
                "score": {
                    "fullTime": {"home": 2, "away": 2},
                    "winner": "DRAW"
                }
            }
        ]
        stats = process_matches(matches)
        print("→ Draw Stats:", stats)
        self.assertEqual(stats["Brighton FC"]["Draws"], 1)
        self.assertEqual(stats["Wolves FC"]["Draws"], 1)

    def test_goals_are_cumulative(self):
        print("\n✅ Running: test_goals_are_cumulative")
        matches = [
            {
                "status": "FINISHED",
                "homeTeam": {"name": "Man United"},
                "awayTeam": {"name": "West Ham"},
                "score": {
                    "fullTime": {"home": 2, "away": 1},
                    "winner": "HOME_TEAM"
                }
            },
            {
                "status": "FINISHED",
                "homeTeam": {"name": "Man United"},
                "awayTeam": {"name": "West Ham"},
                "score": {
                    "fullTime": {"home": 3, "away": 2},
                    "winner": "HOME_TEAM"
                }
            }
        ]
        stats = process_matches(matches)
        print("→ Cumulative goals: Man United", stats["Man United"])
        self.assertEqual(stats["Man United"]["Goals For"], 5)
        self.assertEqual(stats["Man United"]["Wins"], 2)

    def test_teams_with_no_wins(self):
        print("\n✅ Running: test_teams_with_no_wins")
        matches = [
            {
                "status": "FINISHED",
                "homeTeam": {"name": "Brentford"},
                "awayTeam": {"name": "Leeds"},
                "score": {
                    "fullTime": {"home": 0, "away": 1},
                    "winner": "AWAY_TEAM"
                }
            }
        ]
        stats = process_matches(matches)
        print("→ Brentford Stats:", stats["Brentford"])
        self.assertEqual(stats["Brentford"]["Wins"], 0)
        self.assertEqual(stats["Brentford"]["Losses"], 1)

if __name__ == "__main__":
    unittest.main()
