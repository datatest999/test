
# --- Base Configuration ---
# This class holds common settings for all environments.
class DevConfig:
    competitions_url = "https://api.football-data.org/v4/competitions/"
    headers = {"X-Auth-Token": "12abfbaacdab48bc8948ed6061925e1f"}

class ProdConfig:
    competitions_url = "https://api.football-data.org/v4/competitions/"
    headers = {"X-Auth-Token": "PROD_API_KEY_HERE"}