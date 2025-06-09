import json
import unittest
import pandas as pd

# Sample test for loading and validating sample.json structure
def test_sample_json_structure():
    with open("data/sample.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    assert "competitions" in data
    assert isinstance(data["competitions"], list)
    for comp in data["competitions"]:
        assert "id" in comp
        assert "name" in comp
        assert "area" in comp
        assert isinstance(comp["area"], dict)
        assert "name" in comp["area"]

# Sample test for transforming sample.json to DataFrame
def test_transform_sample_json_to_dataframe():
    with open("data/sample.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    competitions = data.get("competitions", [])
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
    df = pd.DataFrame(records)
    assert not df.empty
    assert "id" in df.columns
    assert "name" in df.columns
    assert "area" in df.columns

if __name__ == '__main__':
    unittest.main()