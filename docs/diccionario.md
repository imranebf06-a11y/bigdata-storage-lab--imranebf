# Diccionario de Datos - Esquema Canónico

## Esquema Canónico

| Campo    | Tipo        | Formato / Ejemplo | Descripción                          |
|----------|------------|-----------------|--------------------------------------|
| date     | date       | YYYY-MM-DD      | Fecha de la transacción o registro.  |
| partner  | string     | ACME Corp       | Nombre del socio / partner.          |
| amount   | float (EUR)| 1234.56         | Importe de la transacción en euros.  |

---

## Mapeos Origen → Canónico

| Campo Origen           | Fuente / Sistema      | Campo Canónico | Transformación / Notas                 |
|------------------------|--------------------|----------------|---------------------------------------|
| transaction_date       | CSV pagos           | date           | Convertir a YYYY-MM-DD                |
| partner_name           | Excel socios        | partner        | Limpiar espacios y normalizar texto  |
| total_amount           | ERP                 | amount         | Convertir a float, redondear a 2 dec |
| fecha                  | CSV internacional   | date           | Formato DD/MM/YYYY → YYYY-MM-DD       |
| cliente                | API externa         | partner        | Mapear abreviaturas a nombres completos |
| importe_total          | Base legada         | amount         | Separador decimal , → .               |
