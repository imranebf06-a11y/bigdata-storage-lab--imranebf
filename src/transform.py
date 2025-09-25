from typing import Dict
import pandas as pd

def normalize_columns(df: pd.DataFrame, mapping: Dict[str, str]) -> pd.DataFrame:
    """
    Renombra columnas según mapping y normaliza los datos:
    - date → datetime ISO
    - partner → trim espacios
    - amount → float EUR (quita €, comas)
    """
    df = df.rename(columns=mapping)
    
    # Normalizar fecha
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce', dayfirst=False)
    
    # Limpiar partner
    if 'partner' in df.columns:
        df['partner'] = df['partner'].astype(str).str.strip()
    
    # Normalizar amount
    if 'amount' in df.columns:
        df['amount'] = (
            df['amount']
            .astype(str)
            .str.replace('€', '', regex=False)
            .str.replace('.', '', regex=False)  # eliminar separador de miles europeo
            .str.replace(',', '.', regex=False)  # convertir decimal
            .astype(float)
        )
    return df


def to_silver(bronze: pd.DataFrame) -> pd.DataFrame:
    """
    Agrega amount por partner y mes.
    - Añade columna 'month' como timestamp (inicio de mes)
    """
    df = bronze.copy()
    df['month'] = df['date'].dt.to_period('M').dt.to_timestamp()
    silver = df.groupby(['partner', 'month'], as_index=False)['amount'].sum()
    return silver

