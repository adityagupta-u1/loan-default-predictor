import zipfile

from dotenv import load_dotenv

from loan_default.config import KAGGLE_DATASET, RAW_DIR, RAW_PATH


def download_raw(force: bool = False) -> None:
    """Download and unzip the Home Credit competition files into data/raw."""
    if RAW_PATH.exists() and not force:
        print(f"{RAW_PATH.name} already exists, skipping download (use force=True to redo).")
        return

    # Reads KAGGLE_USERNAME / KAGGLE_KEY from .env (which is gitignored).
    load_dotenv()

    # Imported here because the kaggle package authenticates on import.
    from kaggle.api.kaggle_api_extended import KaggleApi

    api = KaggleApi()
    api.authenticate()

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    api.competition_download_files(KAGGLE_DATASET, path=str(RAW_DIR), quiet=False)

    zip_path = RAW_DIR / f"{KAGGLE_DATASET}.zip"
    with zipfile.ZipFile(zip_path) as zf:
        zf.extractall(RAW_DIR)
    zip_path.unlink()


if __name__ == "__main__":
    download_raw()
