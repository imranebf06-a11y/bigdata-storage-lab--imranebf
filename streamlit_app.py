import streamlit as st
import pandas as pd
from io import BytesIO
from typing import List

# Importar funciones propias
from src.transform import normalize_columns, to_silver
from src.ingest import tag_lineage, concat_bronze
from src.validate import basic_checks

st.set_page_config(page_title="Big Data Storage Lab", layout="wide")
st.title("Big Data Storage Lab - Pipeline Bronze → Silver")

st.sidebar.header("Mapeo de columnas origen")
date_col = st.sidebar.text_input("Columna fecha (date)", "transaction_date")
partner_col = st.sidebar.text_input("Columna partner (partner)", "partner_name")
amount_col = st.sidebar.text_input("Columna importe (amount)", "total_amount")

mapping = {
    date_col: "date",
    partner_col: "partner",
    amount_col: "amount"
}

# Subida de múltiples CSV
uploaded_files = st.file_uploader(
    "Sube uno o más CSV", type=["csv"], accept_multiple_files=True
)

def safe_read_csv(file) -> pd.DataFrame:
    """Intenta leer CSV con UTF-8 y fallback a Latin-1"""
    try:
        return pd.read_csv(file)
    except UnicodeDecodeError:
        return pd.read_csv(file, encoding="latin-1")

if uploaded_files:
    bronze_frames: List[pd.DataFrame] = []
    for f in uploaded_files:
        df = safe_read_csv(f)

        # Validación columnas de origen
        missing_cols = [col for col in [date_col, partner_col, amount_col] if col not in df.columns]
        if missing_cols:
            st.warning(f"Columnas de origen faltantes en {f.name}: {missing_cols}")
            continue

        # Normalizar columnas
        df = normalize_columns(df, mapping)

        # Verificar que columnas canónicas existen
        missing_canon = [c for c in ['date', 'partner', 'amount'] if c not in df.columns]
        if missing_canon:
            st.warning(f"Columnas canónicas faltantes en {f.name} después de normalizar: {missing_canon}")
            continue

        # Añadir linaje
        df = tag_lineage(df, f.name)
        bronze_frames.append(df)

    if bronze_frames:
        # Concatenar bronze con manejo de columnas faltantes
        bronze = concat_bronze(bronze_frames)

        st.subheader("🌑 Bronze - Datos unificados")
        st.dataframe(bronze)

        # Validaciones
        errors = basic_checks(bronze)
        if errors:
            st.warning("⚠️ Validaciones fallidas:")
            for e in errors:
                st.write("-", e)
        else:
            st.success("✅ Bronze OK - Todas las validaciones pasan")

            # Derivar silver (agregado partner x mes)
            silver = to_silver(bronze)

            st.subheader("🟢 Silver - Agregado por partner y mes")
            st.dataframe(silver)

            # KPIs simples
            total_amount = silver['amount'].sum()
            n_partners = silver['partner'].nunique()
            st.markdown(f"**Total amount:** €{total_amount:,.2f}")
            st.markdown(f"**Número de partners:** {n_partners}")

            # Bar chart mes vs amount
            st.bar_chart(silver.groupby('month')['amount'].sum())

            # Botones para descargar CSVs
            def convert_df(df: pd.DataFrame) -> bytes:
                return df.to_csv(index=False).encode('utf-8')

            bronze_csv = convert_df(bronze)
            silver_csv = convert_df(silver)

            st.download_button(
                label="📥 Descargar Bronze CSV",
                data=bronze_csv,
                file_name="bronze.csv",
                mime="text/csv"
            )

            st.download_button(
                label="📥 Descargar Silver CSV",
                data=silver_csv,
                file_name="silver.csv",
                mime="text/csv"
            )
    else:
        st.warning("No se pudieron procesar archivos. Verifique columnas de origen y codificación.")

