# bigdata-storage-lab--imranebf

## 📝 Título  
**De CSVs heterogéneos a un almacén analítico confiable**

---

## 1️⃣ Objetivo  
Construir un flujo de trabajo completo para transformar **archivos CSV heterogéneos** en un **almacén analítico confiable**, siguiendo estas etapas:

- **Ingesta**: cargar múltiples CSV de distintas fuentes.  
- **Validación**: aplicar controles de calidad (tipos, rangos, duplicados).  
- **Normalización**: estandarizar nombres de columnas, formatos y codificación.  
- **Bronze / Silver**: diseñar capas de almacenamiento:  
  - *Bronze*: datos crudos validados.  
  - *Silver*: datos limpios y normalizados listos para analítica.  
- **KPIs / Reporting**: generar indicadores clave sobre los datos (Streamlit App).  

El objetivo es que al final se disponga de un **data warehouse (DW)** con trazabilidad clara y un front-end ligero para visualizar KPIs.

---

## 2️⃣ Entregables  
- **Repositorio público en GitHub**:
  - Código ETL/ELT en Python.
  - Notebooks o scripts de validación y normalización.
  - Esquemas de tablas y documentación técnica.
- **Aplicación Streamlit**:
  - Dashboard de KPIs.
  - Panel para explorar capas Bronze y Silver.
  - Visualización de métricas de calidad de datos.  

---

## 3️⃣ Criterios de Evaluación  
| Criterio | Descripción |
|----------|-------------|
| **Diseño & Justificación** | Calidad del diseño del pipeline, modelo DW y decisiones técnicas. |
| **Calidad de Datos** | Cumplimiento de validaciones, normalizaciones y control de errores. |
| **Trazabilidad / DW** | Capacidad para seguir el dato desde origen hasta KPIs (data lineage). |
| **Documentación** | Claridad del README, comentarios en código y diagramas. |
| **App Streamlit** | Funcionalidad, UX y claridad de visualización de KPIs. |

---

## 4️⃣ Qué **NO** subir al repositorio  
- **Datos sensibles o personales** (PII).  
- **Credenciales o tokens** de acceso.  
- **Archivos binarios grandes** no necesarios para reproducir el laboratorio.  
- En su lugar, usar **datos de ejemplo o mock**.  

---

## 5️⃣ Tiempo estimado por fase  

| Fase | Duración Estimada |
|-------|------------------|
| **Ingesta de CSVs** | 2 horas |
| **Validación de datos** | 3 horas |
| **Normalización** | 3 horas |
| **Diseño Bronze/Silver (DW)** | 3 horas |
| **KPIs + App Streamlit** | 3 horas |
| **Documentación y entrega final** | 2 horas |
| **Total estimado** | ~16 horas |

---

## 🗂 Estructura sugerida del repositorio  
