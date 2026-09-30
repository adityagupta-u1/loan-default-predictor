from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
MODELS_DIR = ROOT / "models"
FIGURES_DIR = ROOT / "reports" / "figures"

KAGGLE_DATASET = "home-credit-default-risk"
RAW_FILENAME = "application_train.csv"
RAW_PATH = RAW_DIR / RAW_FILENAME

RANDOM_SEED = 42
TARGET = "TARGET"
CV_FOLDS = 5
ID_COL = "SK_ID_CURR"
