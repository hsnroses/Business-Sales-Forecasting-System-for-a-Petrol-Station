# Data Inventory — Business Sales Forecasting System for a Petrol Station

## 1. Required Data (from Topic 2 Requirements and V1 Architecture)

| Requirement ID | Needed Information / Feature | Candidate Source | Why Usable / Constraint |
|---|---|---|---|
| FR1: Historical sales analysis | Historical fuel sales, including fuel type, quantity sold and revenue | `sales_dataset.xlsx` — `Fuel_Product` and `Fuel_Pump` sheets | Provides historical fuel sales information for analysing sales trends. Actual column names and data coverage must be verified. |
| FR2: Kedai Mesra sales analysis | Historical sales by product category, including sales amount and transaction information where available | `sales_dataset.xlsx` — `Royalty_Category` sheet | Provides category-level sales information for analysing Kedai Mesra performance. Does not necessarily provide individual product or SKU-level information. |
| FR3: Sales forecasting | Historical sales aggregated by month and sales category | Prepared dataset generated from the Excel workbook | Monthly aggregation can be used to develop forecasting models. The number of available months may limit the complexity of suitable models. |
| NFR1: Forecasting accuracy | Actual sales values and corresponding predicted values | Prepared monthly sales dataset and model predictions | Required to evaluate forecasting performance using MAE, RMSE and MAPE. |
| NFR2: Data quality and reliability | Valid dates, numerical sales values, quantities and consistent categories | Original Excel sheets and prepared CSV files | Data must be checked for missing values, duplicate records, invalid dates and inconsistent values before forecasting. |
| RAI1: Data provenance | Original source, dataset version, access rights and processing history | Original Excel workbook and `week3_manifest.json` | Records where the data came from and how it was processed. |
| NFR3: Reproducibility | Source file checksum, prepared file checksum and pipeline execution details | `week3_manifest.json` and pipeline manifest | Allows the original and prepared data files to be identified and their integrity checked. |

## 2. Source Records

| Field | D1 — Fuel Sales Data | D2 — Kedai Mesra Sales Data |
|---|---|---|
| Source identity | Petrol station sales records | Petrol station Kedai Mesra sales records |
| File name | `sales_dataset.xlsx` | `sales_dataset.xlsx` |
| Sheet name | `Fuel_Product`, `Fuel_Pump` | `Royalty_Category`, `Royalty_Summary` |
| Data type | Structured tabular data; historical time-series records | Structured tabular data; historical time-series records |
| Purpose | Analyse fuel sales trends and forecast future fuel sales and revenue | Analyse category-level sales trends and forecast future Kedai Mesra sales and revenue |
| Main information | Date/month, fuel type, quantity sold and revenue (RM), depending on the available columns | Date/month, category, sales or royalty amount and transaction information, depending on the available columns |
| Version / date | Original Excel workbook; version and reporting period to confirm | Original Excel workbook; version and reporting period to confirm |
| Access rights | To confirm with the data provider. Use only for the approved academic project. | To confirm with the data provider. Use only for the approved academic project. |
| Inspected | Sheet structure and available fields to be verified from the actual workbook | Sheet structure and available fields to be verified from the actual workbook |
| Local file details | File size, sheet count, row count, date coverage and SHA-256: To confirm | File size, sheet count, row count, date coverage and SHA-256: To confirm |

**Additional workbook sheets**

| Sheet | Purpose |
|---|---|
| `Royalty_Summary` | Additional summary information for Kedai Mesra sales; inspect its relationship with `Royalty_Category` before combining them. |
| `Check_Fuel` | Reference or checking information for fuel records. Inspect to understand its purpose before using it in the pipeline. |
| `Check_Royalty` | Reference or checking information for royalty records. Inspect to understand its purpose before using it in the pipeline. |

## 3. Inspection Evidence

### Inspection 1 — Fuel Sales Data

| # | Observation | Evidence to Record | Implication |
|---|---|---|---|
| 1 | Fuel sales are stored in separate workbook sheets. | Inspect `Fuel_Product` and `Fuel_Pump` and record their columns and row counts. | Determine whether the sheets contain different types of fuel sales records or overlapping information. |
| 2 | Date information is required for forecasting. | Check date formats, missing dates and the earliest and latest records. | Dates must be converted into a consistent format before monthly aggregation. |
| 3 | Fuel sales contain numerical information. | Inspect available quantity, volume and revenue columns. | Numerical fields must be validated before calculating monthly sales totals. |
| 4 | Some sales records may contain missing values. | Calculate missing-value counts for important columns such as date, quantity and revenue. | Missing values must be investigated rather than automatically replaced with zero. |
| 5 | Sales data may contain repeated records. | Check for duplicate rows and compare records with matching dates and fuel categories. | Duplicate records must be investigated before aggregation to avoid double-counting sales. |

### Inspection 2 — Kedai Mesra Sales Data

| # | Observation | Evidence to Record | Implication |
|---|---|---|---|
| 1 | Kedai Mesra sales information is organised by category. | Inspect `Royalty_Category` and record the available category fields. | Category-level forecasting is possible if sufficient historical records are available. |
| 2 | A separate summary sheet is available. | Inspect `Royalty_Summary` and compare its information with `Royalty_Category`. | Determine whether the summary sheet can be used for validation or additional analysis. |
| 3 | Sales amounts are required for forecasting. | Identify the relevant sales or royalty amount columns and their meanings. | Confirm which field represents actual sales revenue before using it as the forecasting target. |
| 4 | Some records may contain missing or inconsistent values. | Check missing values, numerical formats and category names. | Data cleaning and validation are required before preparing the forecasting dataset. |
| 5 | Historical records must be suitable for time-series analysis. | Inspect the date range and number of available monthly observations. | A short historical period may limit model selection and forecasting reliability. |

## 4. Open Items

- [ ] Confirm the original Excel workbook name, file size and number of sheets.
- [ ] Record the row count, column names and date coverage for each relevant sheet.
- [ ] Inspect at least two representative sheets: `Fuel_Product` and `Royalty_Category`.
- [ ] Inspect `Fuel_Pump` and `Royalty_Summary` to understand whether they contain additional or overlapping information.
- [ ] Identify the correct revenue field for fuel sales and Kedai Mesra sales.
- [ ] Check missing values, duplicate records, invalid dates and inconsistent categories.
- [ ] Determine whether the available data supports daily or monthly forecasting.
- [ ] Prepare separate cleaned datasets for fuel sales and Kedai Mesra category sales, where applicable.
- [ ] Aggregate historical sales into monthly records for time-series forecasting.
- [ ] Record the original and prepared file sizes, row counts, page/sheet details where relevant, and SHA-256 checksums.
- [ ] Document data access rights and confirm that the data can be used for the academic project.
- [ ] Update `week3_manifest.json` with source and prepared dataset information.
- [ ] Complete the data preparation and validation pipeline in Google Colab.

## 5. Initial Data Processing Plan

The proposed data pipeline is:

**Original Excel Workbook → Data Ingestion → Data Inspection → Data Cleaning → Monthly Aggregation → Data Validation → Prepared CSV Files → Forecasting**

Expected prepared datasets:

1. `prepared_fuel_sales.csv` — cleaned fuel sales records.
2. `prepared_kedai_mesra_sales.csv` — cleaned Kedai Mesra category-level sales records, if supported by the source.
3. `prepared_monthly_sales.csv` — monthly aggregated sales data for forecasting.

The final forecasting dataset should contain the appropriate date/month, sales category, quantity (where available) and revenue fields.

**Important limitation:** The system forecasts sales and revenue based on available historical records. It does not directly forecast profit or individual product inventory requirements unless the required cost, margin or product-level data is available.
