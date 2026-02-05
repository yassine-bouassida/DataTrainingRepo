import io
import os
from typing import Optional

import numpy as np
import pandas as pd
import streamlit as st

# Optional dependency for more realistic synthetic data.
# If Faker is not installed, we fall back to simple random generation.
try:
    from faker import Faker  # type: ignore

    _FAKER_AVAILABLE = True
    _fake = Faker()
except Exception:
    _FAKER_AVAILABLE = False
    _fake = None


@st.cache_data
def generate_synthetic_data(
    rows: int,
    seed: int,
    noise: float,
    include_text: bool,
    categories: int,
) -> pd.DataFrame:
    """
    Generate synthetic data for demos.

    Notes:
    - Cached with st.cache_data to avoid regeneration on every rerun.
    - Use a random seed for reproducibility.
    """
    rng = np.random.default_rng(seed)

    base = rng.normal(loc=50, scale=15, size=rows)
    noise_vec = rng.normal(loc=0, scale=noise, size=rows)

    values = base + noise_vec
    values_b = values * rng.uniform(0.5, 1.5, size=rows)

    # Categorical groups to support group-by and color encoding.
    group_ids = rng.integers(1, categories + 1, size=rows)
    groups = [f"Group {g}" for g in group_ids]

    df = pd.DataFrame(
        {
            "id": np.arange(1, rows + 1),
            "value": values.round(2),
            "value_b": values_b.round(2),
            "group": groups,
        }
    )

    if include_text:
        if _FAKER_AVAILABLE and _fake:
            df["label"] = [_fake.word() for _ in range(rows)]
        else:
            # Fallback text if Faker is unavailable.
            df["label"] = [f"item_{i}" for i in range(1, rows + 1)]

    # Example of derived column (feature engineering).
    df["value_bin"] = pd.cut(df["value"], bins=5, labels=False)

    return df


def df_to_csv_bytes(df: pd.DataFrame) -> bytes:
    """
    Convert DataFrame to CSV bytes for download.

    Note: Using bytes avoids issues with encoding when sending to download_button.
    """
    return df.to_csv(index=False).encode("utf-8")


def get_sqlite_path() -> str:
    """
    Return the local SQLite file path.

    Option: swap this for a path from environment variables or secrets.
    """
    return os.path.join(os.getcwd(), "streamlit_intro.db")




EXPECTED_COLUMNS = ["id", "value", "value_b", "group", "value_bin"]


def validate_schema(df: pd.DataFrame) -> tuple[bool, list[str]]:
    """
    Validate that a DataFrame matches the expected schema.

    Returns:
        (is_valid, missing_columns)
    """
    missing = [c for c in EXPECTED_COLUMNS if c not in df.columns]
    return (len(missing) == 0, missing)
