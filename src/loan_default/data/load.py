import pandas as pd

from loan_default.config import ID_COL, RAW_PATH, RANDOM_SEED, TARGET


def load_raw(path=RAW_PATH, nrows=None) -> pd.DataFrame:
    """Read the raw application_train CSV and check it is what we expect."""

    if not path.exists():
        raise FileNotFoundError(
            f"Raw data file not found at {path}. Download the kaggle dataset first (see README)"
        )  # noqa: E501

    df = pd.read_csv(path, nrows=nrows)

    missing = {ID_COL, TARGET} - set(df.columns)

    if missing:
        raise ValueError(f"Raw data file at {path} is missing expected columns: {missing}")
    if df[ID_COL].duplicated().any():
        raise ValueError(f"Raw data file at {path} has duplicated IDs in column {ID_COL}")
    return df


def split_xy(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    """Separate feature from target, dropping the ID column."""
    return df.drop(columns=[ID_COL, TARGET]), df[TARGET]


def train_test_stratified(df: pd.DataFrame, test_size=0.2):
    """Split the data into train and test sets, stratified by the target column."""
    from sklearn.model_selection import train_test_split

    return train_test_split(df, test_size=test_size, stratify=df[TARGET], random_state=RANDOM_SEED)
