from typing import List
import pandas as pd

def basic_checks(df: pd.DataFrame) -> List[str]:
    """
    Devuelve lista de errores básicos:
    - Columnas canónicas presentes
    - amount es numérico y >= 0
    - date es datetime
    """
    errors = []
    required_cols = ['date', 'partner', 'amount']
    
    # Columnas presentes
    for col in required_cols:
        if col not in df.columns:
            errors.append(f"Falta columna requerida: {col}")
    
    # amount numérico y >=0
    if 'amount' in df.columns:
        if not pd.api.types.is_numeric_dtype(df['amount']):
            errors.append("amount no es numérico")
        if (df['amount'] < 0).any():
            errors.append("amount tiene valores negativos")
    
    # date en datetime
    if 'date' in df.columns:
        if not pd.api.types.is_datetime64_any_dtype(df['date']):
            errors.append("date no es tipo datetime")
    
    return errors
