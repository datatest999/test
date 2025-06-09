import os
from config.config import DevConfig, ProdConfig
from jobs.jobs import CompetitionJob

def main():
    # Determine environment from environment variable
    env = os.getenv("APP_ENV", "dev")
    config_class = DevConfig if env == "dev" else ProdConfig

    # Run the competition job
    job = CompetitionJob(config_class)
    job.run(csv_path="competitions.csv")

if __name__ == "__main__":
    main()