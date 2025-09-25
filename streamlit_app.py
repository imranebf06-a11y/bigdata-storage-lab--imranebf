import streamlit as st
import pandas as pd
from io import BytesIO

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

if uploaded_files:
    bronze_frames = []
    for f in uploaded_files:
        try:
            df = pd.read_csv(f)
        except UnicodeDecodeError:
            df = pd.read_csv(f, encoding="latin-1")

        # Normalizar columnas
        df = normalize_columns(df, mapping)

        # Añadir linaje
        df = tag_lineage(df, f.name)
        bronze_frames.append(df)

    # Concatenar todos los archivos en bronze unificado
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

