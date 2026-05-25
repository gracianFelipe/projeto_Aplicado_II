from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
MODELS_DIR = ROOT_DIR / "models"

PRIMARY_DATASET = RAW_DIR / "ifood-restaurants-february-2021.csv"

TEXT_COLUMNS = ["name", "category", "tags"]
TARGET_COLUMN = "rating"

RANDOM_STATE = 42
TEST_SIZE = 0.20
MIN_DF = 5
NGRAM_RANGE = (1, 2)
HIGH_RATING_THRESHOLD = 4.5
