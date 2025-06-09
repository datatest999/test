from setuptools import setup, find_packages

setup(
    name="football-data-pipeline",
    version="0.1.0",
    description="A pipeline to ingest, transform, and save football competition data.",
    author="emmanuel fred",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "requests",
        "pytest",
        "python-dotenv"
    ],
    python_requires=">=3.7",
)