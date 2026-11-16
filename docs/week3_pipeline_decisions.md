# Pipeline Decisions — Business Sales Forecasting System for a Petrol Station (Week 3)

Version: 1.0

**Pipeline diagram:** `docs/week3_pipeline_diagram.png`

## 1. Requirements and Source

| Item | Record |
|---|---|
| Topic 2 requirements | FR1: Analyse historical sales records. FR2: Prepare sales data for forecasting. FR3: Generate monthly sales forecasts. NFR1: Forecasting accuracy. NFR2: Data quality and reliability. NFR3: Data processing and reproducibility. RAI1: Data provenance and responsible data handling. |
| Architecture component | Sales Data Source → Data Ingestion → Data Inspection → Data Preparation → Data Validation → Prepared Sales Dataset → Forecasting Component (V1 architecture, `week2_architecture_v1.png`). |
| Selected source (S01) | Original petrol station sales Excel workbook, stored in `data/raw/`. Exact filename: To confirm. |
| Selected sheets | `Fuel_Product`, `Fuel_Pump`, `Royalty_Category` and `Royalty_Summary`. |
| Pathways | B: CSV / Excel and F: Time-Series. |
| Not used | `Check_Fuel` and `Check_Royalty` are not automatically included as forecasting inputs. They will only be used for reference or validation after their purposes are confirmed. |

The selected workbook contains historical fuel sales and Kedai Mesra category-level sales information. These records are relevant to the project because they provide historical sales values that can be analysed and used to develop monthly forecasting models.

## 2. Part B Comparison and Evidence

Two preparation approaches will be considered for the historical sales data.

| | Approach A: Keep original records | Approach B: Monthly aggregation |
|---|---|---|
| Configuration | Retain the available original transaction or reporting records with minimal transformation. | Group sales records by month and relevant sales category. |
| Data structure | Original date, fuel type/category, quantity and revenue fields, depending on the source. | Month, sales category, total quantity (where available) and total revenue. |
| Purpose | Preserve detailed historical information for inspection and further analysis. | Prepare consistent monthly observations for time-series forecasting. |
| Benefit | Retains more information from the original workbook. | Simplifies trend analysis and provides a suitable structure for monthly forecasting. |
| Limitation | May contain irregular dates, inconsistent categories or multiple records within the same month. | Loses daily or transaction-level detail and may hide short-term sales fluctuations. |

**Selected approach:** Monthly aggregation, while retaining the original records as a separate prepared dataset where appropriate.

**Reason for selection:**

The main objective of the project is to forecast future monthly sales. Therefore, monthly aggregation is more appropriate for the initial forecasting dataset. It also makes it easier to compare actual monthly sales with predicted sales.

However, the original records should be preserved so that the preparation process can be checked and repeated.

**Important data handling decisions:**

- Fuel sales and Kedai Mesra sales will be prepared separately where their structures differ.
- Fuel quantity and revenue should be aggregated using appropriate numerical fields.
- Kedai Mesra records should be grouped by category if the source contains reliable category information.
- Missing revenue values must be investigated rather than automatically replaced with zero.
- Duplicate-looking records must be checked before removal to avoid deleting legitimate transactions.
- The relationship between `Royalty_Category` and `Royalty_Summary` must be verified before combining their records.

**Observed evidence:** To be completed after running the notebook. Record the number of original rows, prepared rows, available months, missing values and duplicate records for each selected sheet.

## 3. Preparation Configuration

| Setting | Value |
|---|---|
| Source format | Excel workbook (`.xlsx`) |
| Data loading | Python Pandas with `read_excel()` |
| Selected sheets | `Fuel_Product`, `Fuel_Pump`, `Royalty_Category`, `Royalty_Summary` |
| Inspection | Display column names, sample records, data types, missing values and duplicate records. |
| Date preparation | Convert available date fields into a consistent date format. |
| Numerical preparation | Validate quantity, volume and revenue fields. |
| Category preparation | Standardise category names where necessary and preserve the original values for reference. |
| Aggregation | Monthly aggregation by relevant sales category. |
| Output format | CSV (`.csv`) |
| Part B output | `data/processed/` |
| Part C output | `data/pipeline_v1/` |
| Pipeline version | `week3-v1` |

Expected prepared datasets:

1. `prepared_fuel_sales.csv` — cleaned fuel sales records.
2. `prepared_kedai_mesra_sales.csv` — cleaned Kedai Mesra category-level records, if supported by the source.
3. `prepared_monthly_sales.csv` — monthly aggregated sales records for forecasting.

The exact column names and output structure will be finalised after inspecting the original workbook.

## 4. Differences Between Part B and Part C

| | Part B (CSV / Excel and Time-Series preparation) | Part C (Executable V1 pipeline) |
|---|---|---|
| Purpose | Experiment with and prepare the selected sales data. | Implement the selected preparation process as a repeatable pipeline. |
| Input | Original Excel workbook. | Same original Excel workbook. |
| Processing | Inspect, clean, validate and aggregate sales records. | Execute the selected CSV/Excel and time-series processing functions. |
| Output location | `data/processed/` | `data/pipeline_v1/` |
| Output format | Prepared CSV files. | Prepared CSV files and pipeline manifests. |
| Lineage | `data/week3_manifest.json` | Individual `pipeline_manifest.json` files for selected pathways. |
| Verification | Inspect prepared records and data quality. | Re-run the pipeline and compare source and output fingerprints. |

Part B is used to determine and test the appropriate data preparation approach. Part C converts the selected approach into an executable pipeline that can be run again using the same source workbook.

The outputs should be logically consistent when the same preparation configuration is used.

## 5. Stage Contracts

| Stage | Contract / Evidence | Failure Response |
|---|---|---|
| Ingest | `select_source()` locates the expected Excel workbook in `data/raw/`. The workbook opens successfully using Pandas. | Stop with an error if the source file is missing, inaccessible or cannot be opened. |
| Inspect | Required sheets are available and their column names, row counts, data types and sample records can be inspected. | Report missing sheets or unexpected column structures. Do not silently continue with missing required data. |
| Prepare | Relevant date, category, quantity and revenue fields are cleaned and transformed. Monthly aggregation is performed using the correct fields. | Stop or flag records with invalid dates or unusable numerical values. Document any excluded records. |
| Validate | Prepared CSV files exist, are non-empty and contain the expected columns. Check date validity, missing values and aggregation results. | Report validation failures and investigate the affected records before proceeding. |
| Record lineage | Source filename, source checksum, prepared output filenames, output checksums, processing method and configuration are recorded in `week3_manifest.json` and pipeline manifests. | Report missing metadata, incorrect file mappings or checksum mismatches. |
| Repeatability (Cell 9) | A second execution produces matching source fingerprints and prepared-output fingerprints when the input and processing configuration remain unchanged. | Report a failed comparison and investigate differences in source data or processing logic. |

**Validation evidence to record:**

- Original and prepared row counts.
- Number of missing values in important columns.
- Number of duplicate records identified.
- Earliest and latest dates.
- Number of available monthly observations.
- Confirmation that monthly revenue totals match the corresponding valid source records.
- Successful source and output checksum verification.
- Cell 9 repeatability result.

## 6. ETL or ELT

**Decision: ETL (Extract, Transform, Load).**

The project uses an ETL approach because the original Excel workbook must be extracted, cleaned, validated and transformed before the data can be used for forecasting.

The process consists of:

1. **Extract:** Load the original Excel workbook and selected worksheets into Python using Pandas.
2. **Transform:** Clean date fields, validate numerical values, standardise categories and aggregate sales records by month.
3. **Load:** Save the prepared sales datasets as CSV files in the processed data directory.

This approach is suitable because the forecasting models require structured and consistent numerical data. The original Excel workbook will remain unchanged in `data/raw/`, while the prepared datasets will be stored separately.

## 7. Batch or Streaming

**Decision: Batch processing.**

Batch processing is selected because the project uses historical sales records rather than a continuous real-time sales data stream.

The pipeline will process the available Excel records in batches. It can be executed again when new historical sales records become available or when the source workbook is updated.

Streaming is not required because the current project focuses on monthly sales forecasting rather than real-time sales monitoring.

Batch processing is also suitable for the academic project because it allows the same dataset to be processed repeatedly, making data validation and forecasting evaluation easier.

## 8. Output Location and Provenance / Access Caveats

| Item | Location |
|---|---|
| Original Excel workbook | `data/raw/sales_dataset.xlsx` (replace with the actual filename) |
| Part B prepared fuel data | `data/processed/prepared_fuel_sales.csv` |
| Part B prepared Kedai Mesra data | `data/processed/prepared_kedai_mesra_sales.csv` |
| Part B monthly dataset | `data/processed/prepared_monthly_sales.csv` |
| Part B lineage manifest | `data/week3_manifest.json` |
| Part C CSV/Excel output | `data/pipeline_v1/csv_excel/` |
| Part C time-series output | `data/pipeline_v1/timeseries/` |
| Part C pipeline manifest | `pipeline_manifest.json` inside each selected pathway output directory |
| Pipeline notebook | `notebooks/week3_pipeline.ipynb` |
| Data inventory | `docs/week3_data_inventory.md` |
| Pipeline decisions | `docs/week3_pipeline_decisions.md` |
| Pipeline diagram | `docs/week3_pipeline_diagram.png` |

**Caveats**

- **Data access rights:** Confirm that the sales workbook is authorised for use in the academic project. Document any restrictions on storing or sharing the data.
- **Sensitive business information:** Sales records may contain commercially sensitive information. Do not commit the original workbook or identifiable business records to a public GitHub repository without permission.
- **Manifest information:** Record the actual source filename, source version, access rights and processing configuration. Do not leave default values such as "Not verified" once the information has been confirmed.
- **Local paths:** Avoid storing personal computer paths or usernames in publicly shared manifests. Prefer project-relative paths.
- **Data integrity:** SHA-256 checksums can verify whether a file has changed. They do not prove that the data is accurate or that its use is authorised.
- **Revenue interpretation:** Revenue is not the same as profit. Profit forecasting would require additional cost and margin information.
- **Data availability:** The forecasting period and number of observations must be confirmed from the actual workbook before selecting forecasting models.
- **Data sharing:** If the workbook is restricted, keep it in approved storage and commit only permitted documentation, manifests and anonymised evidence.

## 9. Known Limitations Carried to Later Topics

| Limitation | Effect | Planned Response |
|---|---|---|
| Limited historical observations | A small number of monthly records may reduce forecasting reliability. | Evaluate simple baseline and suitable time-series models before considering more complex approaches. |
| Missing sales values | Missing revenue or quantity values may affect monthly totals and forecasting accuracy. | Investigate missing values and document the treatment applied. |
| Inconsistent date formats | Incorrect date parsing may result in records being assigned to the wrong month. | Standardise dates and validate the earliest and latest records. |
| Duplicate-looking records | Duplicate records may cause sales totals to be overstated. | Investigate duplicates against the original source before removing them. |
| Different workbook sheet structures | Fuel and Kedai Mesra data may contain different fields and reporting formats. | Prepare the two data sources separately before combining any compatible information. |
| Category-level Kedai Mesra data | Individual product or SKU-level sales forecasts may not be possible. | Limit forecasting to the available sales categories. |
| Monthly aggregation | Daily sales fluctuations are not represented in the monthly dataset. | Retain the original records for detailed analysis where necessary. |
| Revenue without cost information | The system cannot determine actual profit from revenue alone. | Keep the project focused on sales and revenue forecasting. |
| Changes to source workbook | Updated source data may produce different prepared outputs. | Record source and output fingerprints in the pipeline manifests and rerun validation. |

## 10. Summary

The selected V1 data pipeline uses the CSV/Excel and Time-Series pathways to prepare historical petrol station sales records for monthly forecasting.

The ETL and batch-processing approach is suitable because the project relies on historical Excel data that must be cleaned, validated and aggregated before it can be used by forecasting models.

The pipeline produces prepared fuel sales and Kedai Mesra category-level datasets, where supported by the source workbook, together with lineage manifests for tracking data preparation.

The next stage of the project will use the prepared data to develop and evaluate forecasting models using appropriate metrics such as MAE, RMSE and MAPE.
