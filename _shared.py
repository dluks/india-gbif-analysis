"""Shared constants and reference data for India GBIF analysis notebooks."""

from pathlib import Path

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import pandas as pd
import seaborn as sns

# --- Paths ---
PARQUET_PATH = "../../data/raw/all_tracheophyta_non-cult_2026-02-17.parquet/[0-9]*"
SPLOT_PATH = "../../data/interim/splot/filtered_surveys/try6/splot_filtered.parquet"
FILTERED_GBIF_PATH = (
    "../../data/interim/gbif/filtered_occurrences/try6/gbif_filtered.parquet"
)
CACHE_DIR = Path("_cache")

# iNaturalist Research-grade Observations dataset key
INAT_DATASET_KEY = "50c9509d-22c7-4a22-a47d-8c48425ef4a7"

# --- Reference data ---
# Sources: World Bank 2023 (population, area), Kew State of the World's Plants / national floras (species richness)
COUNTRY_REF = pd.DataFrame(
    {
        "countrycode": [
            "FR",
            "GB",
            "DE",
            "NL",
            "US",
            "AU",
            "SE",
            "ES",
            "DK",
            "CH",
            "IN",
            "CN",
            "BR",
            "ZA",
            "MX",
            "CO",
            "JP",
            "NZ",
            "NO",
            "FI",
            "PK",
            "BD",
            "LK",
            "NP",
            "BT",
            "MM",
        ],
        "country_name": [
            "France",
            "UK",
            "Germany",
            "Netherlands",
            "USA",
            "Australia",
            "Sweden",
            "Spain",
            "Denmark",
            "Switzerland",
            "India",
            "China",
            "Brazil",
            "South Africa",
            "Mexico",
            "Colombia",
            "Japan",
            "New Zealand",
            "Norway",
            "Finland",
            "Pakistan",
            "Bangladesh",
            "Sri Lanka",
            "Nepal",
            "Bhutan",
            "Myanmar",
        ],
        "population_m": [
            68.2,
            67.7,
            84.5,
            17.9,
            339.9,
            26.6,
            10.5,
            48.1,
            5.9,
            8.8,
            1428.6,
            1425.7,
            216.4,
            60.4,
            128.9,
            52.1,
            125.1,
            5.2,
            5.5,
            5.6,
            240.5,
            172.9,
            22.2,
            30.9,
            0.8,
            54.8,
        ],
        "area_mkm2": [
            0.640,
            0.244,
            0.357,
            0.042,
            9.834,
            7.692,
            0.450,
            0.506,
            0.043,
            0.041,
            3.287,
            9.597,
            8.516,
            1.221,
            1.964,
            1.142,
            0.378,
            0.268,
            0.385,
            0.338,
            0.881,
            0.148,
            0.066,
            0.147,
            0.038,
            0.677,
        ],
        "est_plant_species": [
            6000,
            3300,
            4100,
            2200,
            19500,
            21000,
            2600,
            7500,
            1900,
            3600,
            18000,
            33000,
            33000,
            21000,
            26000,
            27000,
            7000,
            2400,
            3200,
            1600,
            6000,
            5000,
            3500,
            7000,
            5600,
            11000,
        ],
    }
).set_index("countrycode")

# Major Indian cities for spatial proximity analysis
INDIA_CITIES = pd.DataFrame(
    {
        "city": [
            "Mumbai",
            "Delhi",
            "Bengaluru",
            "Chennai",
            "Kolkata",
            "Hyderabad",
            "Pune",
            "Ahmedabad",
            "Jaipur",
            "Lucknow",
            "Kochi",
            "Guwahati",
            "Chandigarh",
            "Bhopal",
            "Dehradun",
            "Thiruvananthapuram",
        ],
        "lat": [
            19.08,
            28.61,
            12.97,
            13.08,
            22.57,
            17.39,
            18.52,
            23.02,
            26.91,
            26.85,
            9.93,
            26.14,
            30.73,
            23.26,
            30.32,
            8.52,
        ],
        "lon": [
            72.88,
            77.21,
            77.59,
            80.27,
            88.36,
            78.49,
            73.86,
            72.57,
            75.79,
            80.95,
            76.27,
            91.74,
            76.78,
            77.41,
            78.03,
            76.94,
        ],
    }
)


def setup_plotting():
    """Configure matplotlib/seaborn for consistent style across notebooks."""
    sns.set_theme(context="paper", style="ticks", font_scale=1.4)
    plt.rcParams["figure.dpi"] = 150
