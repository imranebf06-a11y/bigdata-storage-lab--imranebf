# Gobernanza de Datos

## 1. Origen y Linaje de Datos
- Datos provienen de múltiples sistemas: CSVs locales, Excel de partners, ERP corporativo y APIs externas.
- Cada dato debe tener **trazabilidad** hacia su fuente original.
- Linaje registrado en metadatos para cada capa:
  - Bronze: datos crudos validados.
  - Silver: datos normalizados.
  - Gold: agregados y KPIs.

## 2. Validaciones Mínimas
- Comprobación de tipos de datos (date, string, float).
- Formato de fechas correcto (YYYY-MM-DD).
- Valores numéricos no negativos.
- Detección de duplicados por clave primaria (date + partner).
- Campos obligatorios no vacíos.

## 3. Política de Mínimos Privilegios
- Acceso a datos según rol:
  - Data Engineer: lectura/escritura Bronze/Silver.
  - Analista: lectura Silver/Gold.
  - Auditor/Reviewer: lectura completa + metadatos.
- Ningún usuario puede modificar directamente datos críticos sin autorización.

## 4. Trazabilidad y Roles
- Cada transformación debe registrar:
  - Origen del dato.
  - Transformación aplicada.
  - Timestamp y usuario que ejecutó el proceso.
- Roles principales:
  - **Owner**: responsable de calidad de datos.
  - **ETL Developer**: implementa y mantiene pipeline.
  - **Data Analyst**: consume datos para reporting.
  - **Auditor**: revisa trazabilidad y cumplimiento.

