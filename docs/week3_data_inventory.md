# Data Inventory — Business Sales Forecasting System for a Petrol Station

## 1. Required Data (from Topic 2 Requirements and V1 Architecture)

| Requirement ID | Needed Information / Feature | Candidate Source | Why Usable / Constraint |
|---|---|---|---|
| FR1: Historical sales analysis | Historical sales dates, fuel types, sales categories, quantities and sales values | `Fuel_Product`, `Fuel_Pump`, `Royalty_Category`, `Royalty_Summary` | Provides historical fuel and Kedai Mesra sales information. Some records contain missing values. |
| FR2: Monthly sales forecasting | Valid monthly dates and numerical sales values | `Fuel_Product` and `Royalty_Category` | Suitable for preparing monthly sales data. Missing periods and incomplete records must be handled. |
| FR3: Forecasting result presentation | Historical sales, predicted sales and monthly periods | Prepared monthly datasets and forecasting outputs | Supports charts, tables and forecasting result presentation. |
| NFR2: Data quality | Complete, valid and consistent sales records | Original Excel workbook and validation worksheets | Supports data inspection and validation before forecasting. |
| RAI1 / RAI2: Privacy and provenance | Data source, permissions and processing information | Original workbook, README and data manifests | Helps protect confidential information and maintain data traceability. |
| RAI3: Forecasting limitations | Historical coverage, forecasting errors and model limitations | Prepared datasets and evaluation results | Helps communicate that forecasts are estimates, not guaranteed sales. |

## 2. Source Records

| Field | D1 — Fuel Sales | D2 — Kedai Mesra Sales |
|---|---|---|
| Source identity | Petrol station fuel sales records | Petrol station royalty reports |
| Source files | `data_petrol.pdf` | `data_kedai_mesra.pdf` |
| Worksheet | `Fuel_Product`, `Fuel_Pump` | `Royalty_Category`, `Royalty_Summary` |
| Data type | Monthly fuel sales records | Monthly category sales records |
| Main attributes | Month, Fuel, Transactions, Volume_L, Amount_RM | Month, Category, Quantity, Sales_RM, Royalty_RM |
| Data coverage | November 2024 – October 2026, with May 2025 missing | November 2024 – October 2026 |
| Records | 69 Fuel_Product rows; 598 Fuel_Pump rows | 521 Royalty_Category rows; 24 Royalty_Summary rows |
| Purpose | Fuel sales analysis and forecasting | Kedai Mesra sales analysis and forecasting |
| Access rights | Permission to use and share must be confirmed | Permission to use and share must be confirmed |

**Supporting worksheets:**
- `Check_Fuel` — compares fuel sales totals.
- `Check_Royalty` — compares royalty summary and category totals.
- `README` — documents source information and known data limitations.

## 3. Inspection Evidence

### Inspection 1 — Fuel Sales

| # | Observation | Evidence | Implication |
|---|---|---|---|
| 1 | Fuel sales records are available by fuel type. | `Fuel_Product` contains Primax 95, Primax 97 and Diesel Euro (B10/B20). | Supports fuel sales analysis. |
| 2 | Pump-level records provide more detailed information. | `Fuel_Pump` contains pump and hose details. | Can support detailed analysis and validation. |
| 3 | May 2025 fuel records are missing. | No corresponding monthly fuel records are available. | Creates a gap in the monthly forecasting data. |
| 4 | Fuel sales amounts are missing for April 2026. | Three missing `Amount_RM` values in `Fuel_Product` and 26 in `Fuel_Pump`. | Requires investigation before revenue forecasting. |
| 5 | A small difference exists between fuel totals. | June 2025 has a RM0.20 difference between pump and product totals. | Requires documented validation. |

### Inspection 2 — Kedai Mesra Sales

| # | Observation | Evidence | Implication |
|---|---|---|---|
| 1 | Category-level sales records are available. | `Royalty_Category` contains 25 distinct categories. | Supports category-level sales analysis. |
| 2 | April 2026 royalty values are missing. | 21 missing `Royalty_RM` values. | Limits royalty analysis for that month. |
| 3 | July 2026 category details are unavailable. | No category-level records were extracted for July 2026. | Creates incomplete category-level coverage. |
| 4 | July 2026 summary information is partially available. | `Royalty_Summary` contains total sales information, but some breakdown fields are missing. | Summary-level analysis may still be possible. |
| 5 | Royalty and sales values represent different measures. | `Sales_RM` and `Royalty_RM` are separate columns. | Use sales values for revenue analysis, not royalty values. |

## 4. Open Items

- [ ] Confirm permission to use and share the original business dataset.
- [ ] Prepare separate fuel and Kedai Mesra datasets.
- [ ] Investigate missing values and incomplete reporting periods.
- [ ] Validate sales totals using `Check_Fuel` and `Check_Royalty`.
- [ ] Generate the prepared CSV files.
- [ ] Aggregate suitable records into monthly sales data.
- [ ] Record source details, processing information and file hashes in the data manifests.
- [ ] Confirm the final forecasting datasets and evaluation periods.

**Important limitation:** The system forecasts sales and revenue based on available historical records. It does not directly forecast profit or individual product inventory requirements unless the required cost, margin or product-level data is available.
