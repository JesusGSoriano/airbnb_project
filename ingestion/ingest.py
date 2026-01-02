# Imports necesarios

from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine
import os

# Carga de los archivos a utilizar

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_RAW = PROJECT_ROOT / "data" / "raw"

LISTINGS_PATH = DATA_RAW / "listings.csv"
REVIEWS_PATH = DATA_RAW / "reviews.csv"

DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB", "airbnb")

DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# MAIN

def main():
    print("Cargando archivos CSV")

    listings = pd.read_csv(LISTINGS_PATH)
    reviews = pd.read_csv(REVIEWS_PATH)

    print(f"Listings shape: {listings.shape}")
    print(f"Reviews shape: {reviews.shape}")

    print("Conectando a Postgres")
    engine = create_engine(DB_URL)

    print("Cargando raw_listings")
    listings.to_sql(
        "raw_listings",
        engine,
        if_exists="replace",
        index=False
    )

    print("Cargando raw_reviews")
    reviews.to_sql(
        "raw_reviews",
        engine,
        if_exists="replace",
        index=False
    )

    print("Ingestión completada")


if __name__ == "__main__":
    main()
