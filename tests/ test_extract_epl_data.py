import pytest
import pandas as pd
from extract_epl_data import fetch_epl_standings

# Sample JSON response that looks like football-data.org output
MOCK_API_RESPONSE = {
    "standings": [
        {
            "table": [
                {
                    "position": 1,
                    "team": {"id": 65, "name": "Manchester City FC"},
                    "playedGames": 38,
                    "won": 28,
                    "draw": 5,
                    "lost": 5,
                    "goalsFor": 94,
                    "goalsAgainst": 33,
                    "goalDifference": 61,
                    "points": 89
                }
            ]
        }
    ]
}

def test_fetch_epl_standings_success(mocker):
    """Test successful processing of mocked API response."""
    # Arrange: mock requests.get
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = MOCK_API_RESPONSE
    mocker.patch("requests.get", return_value=mock_response)

    # Act
    df = fetch_epl_standings(2023)

    # Assert
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert "team_name" in df.columns
    assert df.iloc[0]["team_name"] == "Manchester City FC"
    assert df.iloc[0]["points"] == 89
    assert df.iloc[0]["won"] == 28


def test_fetch_epl_standings_api_error(mocker):
    """Test handling of API failure (returns empty DataFrame)."""
    # Arrange: force requests.get to raise an HTTP error
    mocker.patch("requests.get", side_effect=Exception("API down"))

    # Act
    df = fetch_epl_standings(2023)

    # Assert
    assert isinstance(df, pd.DataFrame)
    assert df.empty
