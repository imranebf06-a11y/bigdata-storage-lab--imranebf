from typing import List
import pandas as pd
from datetime import datetime, timezone

def tag_lineage(df: pd.DataFrame, source_name: str) -> pd.DataFrame:
    """
    Añade columnas de linaje:
    - source_file
    - ingested_at (UTC ISO)
    """
    df = df.copy()
    df['source_file'] = source_name
    df['ingested_at'] = datetime.now(timezone.utc).isoformat()
    return df


def concat_bronze(frames: List[pd.DataFrame]) -> pd.DataFrame:
    """
    Concatena lista de DataFrames a esquema canónico + linaje:
    date, partner, amount, source_file, ingested_at
    """
    cols = ['date', 'partner', 'amount', 'source_file', 'ingested_at']
    df_concat = pd.concat(frames, ignore_index=True)
    df_concat = df_concat[cols]
    return df_concat
