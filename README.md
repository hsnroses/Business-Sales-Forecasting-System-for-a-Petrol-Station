# Business Sales Forecasting System for a Petrol Station

> This project aims to analyse historical petrol station sales data, identify monthly sales patterns, and develop machine learning models to forecast future sales for fuel products and Kedai Mesra categories.

## Problem Statement

Petrol stations generate sales data from different sources, including fuel sales and convenience store products. However, analysing historical sales records and predicting future sales can be challenging when information is stored across different records and categories.

Without proper analysis, business operators may find it difficult to identify sales trends, compare monthly performance, and estimate future sales. This project explores the use of data processing and machine learning techniques to analyse historical sales data and forecast future monthly sales.

## Evidence of the Problem

- The [UCI Online Retail Dataset](https://archive.ics.uci.edu/dataset/352/online+retail) provides transaction records that can be analysed to identify sales patterns and customer purchasing behaviour.
- The [Sample Superstore Dataset](https://www.kaggle.com/datasets?search=sample+superstore) provides business sales information for analysing sales performance and trends.
- Time-series forecasting methods use historical observations to estimate future values and support business planning ([Scikit-learn Documentation](https://scikit-learn.org/stable/)).

## Initial Related Work / Existing Approaches

- **Microsoft Power BI:** Provides business intelligence features for analysing historical data and presenting sales trends through dashboards.
- **Tableau:** Supports business data exploration and visualisation to identify patterns and trends.
- **Machine learning-based sales forecasting:** Uses historical sales observations to predict future sales and estimate business demand.

## Engineering Gap / Limitation

Existing business intelligence tools provide useful features for analysing historical sales data, but analysing past performance and forecasting future sales are different tasks. Businesses may require additional data preparation and forecasting models to estimate future sales based on their historical records.

This project focuses on developing a sales forecasting system that processes historical petrol station sales data, identifies monthly sales patterns, and predicts future sales for fuel types and Kedai Mesra categories. This is a practical engineering application, not a claim of scientific novelty.

## Project Objectives

- **O1:** To analyse historical petrol station sales data and identify monthly sales trends and patterns.
- **O2:** To develop machine learning-based forecasting models for predicting future monthly sales.
- **O3:** To evaluate forecasting model performance using appropriate evaluation metrics.

## Target Users

Petrol station operators and management, with a focus on understanding historical sales performance and estimating future sales.

## Application Scope

**Supported tasks:** process Excel and CSV sales records, inspect and prepare historical sales data, analyse fuel sales by fuel type, analyse Kedai Mesra sales by available product categories, aggregate sales records into monthly data, forecast future monthly sales, evaluate forecasting performance, and present historical trends and forecast results.

**Out of scope:** automated purchasing and stock replenishment, individual product-level inventory optimisation without SKU-level data, profit prediction without cost and margin information, automated business decision-making, and general-purpose AI chatbot functionality.

## Main Features

- Excel and CSV sales data processing
- Historical sales data inspection and cleaning
- Fuel sales analysis by fuel type
- Kedai Mesra sales analysis by product category
- Monthly sales aggregation
- Machine learning-based sales forecasting
- Forecasting performance evaluation
- Sales trend and forecast visualisation

## Data Sources

The primary data source is a petrol station sales dataset, subject to appropriate access permission.

The Excel workbook contains the following sheets:

- `Fuel_Product` — Fuel product sales records
- `Fuel_Pump` — Fuel pump sales records
- `Royalty_Category` — Kedai Mesra category-level records
- `Royalty_Summary` — Royalty-related summary records
- `Check_Fuel` — Supporting fuel data checks
- `Check_Royalty` — Supporting royalty data checks

Additional public datasets may be used for supplementary testing:

- [UCI Online Retail Dataset](https://archive.ics.uci.edu/dataset/352/online+retail)
- [Sample Superstore Dataset](https://www.kaggle.com/datasets?search=sample+superstore)

The actual workbook structure, available attributes, data quality, and relationships between sheets will be verified during data inspection before implementation.

## Requirements Summary

Full details are documented in `docs/week2_requirements.md`.

| **Type** | **IDs** | **Focus** |
|---|---|---|
| Functional | FR1–FR3 | Historical sales analysis, monthly sales forecasting, and forecasting result presentation |
| Non-functional | NFR1–NFR3 | Forecast accuracy, data quality, and system usability |
| Responsible AI | RAI1–RAI3 | Data privacy, data provenance, and communicating forecasting limitations |

*Note: Requirement IDs and descriptions should match the final versions in `week2_requirements.md`.*

## Evaluation Plan

The forecasting models will be evaluated using historical sales data and a suitable time-based validation approach. Full criteria will be documented in `docs/week2_evaluation_criteria.md`.

| **Criterion** | **Metric** | **Purpose** |
|---|---|---|
| Forecasting error | MAE | Measures average absolute prediction error |
| Large prediction errors | RMSE | Gives greater weight to larger prediction errors |
| Percentage error | MAPE | Measures prediction error relative to actual sales |

**Evaluation approach:** Compare suitable forecasting models using the same test period and historical sales data. The final model will be selected based on forecasting performance and dataset characteristics.

## V1 Architecture

The V1 architecture will show the main data processing and forecasting workflow:

**Sales Data → Data Ingestion → Data Inspection → Data Preparation → Data Validation → Prepared Monthly Sales Data → Forecasting Model → Forecast Results**

The system will process fuel and Kedai Mesra sales data separately where their structures and meanings differ. Architecture decisions, trade-offs, and requirements traceability will be documented in `docs/week2_architecture_decisions.md`.

## Technology Stack (Provisional)

Specific technologies will be selected and refined during implementation. Current candidates:

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Google Colab
- Excel / CSV
- Streamlit (for dashboard development, if included)

## Responsible AI

- Protect confidential business information and use data only with appropriate permission.
- Record data sources, versions, and preparation steps to maintain data provenance.
- Check missing, inconsistent, and invalid records before model development.
- Present forecasts as estimates rather than guaranteed future sales.
- Explain model limitations and avoid making unsupported business claims.
- Use appropriate evaluation methods to assess forecasting performance.

## Documentation

| **File** | **Description** |
|---|---|
| `docs/week1_project_scope.md` | Week 1 project scope and problem definition |
| `docs/week2_requirements.md` | Project framing, application scope, functional, non-functional, and Responsible AI requirements |
| `docs/week2_evaluation_criteria.md` | Forecasting evaluation criteria and metrics |
| `docs/week2_architecture_decisions.md` | Architecture decisions, trade-offs, and requirements traceability |
| `docs/week2_architecture_v1.png` | Initial V1 conceptual architecture diagram |
| `docs/week3_data_inventory.md` | Data sources, structure, access, and inspection evidence |
| `docs/week3_pipeline_diagram.png` | Week 3 data pipeline architecture |
| `docs/week3_pipeline_decisions.md` | Data pipeline decisions and justifications |
| `notebooks/week3_pipeline.ipynb` | Executable data ingestion and preparation pipeline |

## Weekly Progress

| **Week** | **Focus** | **Deliverable** | **Status** |
|---|---|---|---|
| W1 | Project scoping and GitHub setup | README and project scope | Complete |
| W2 | Requirements, evaluation planning, and V1 architecture | Requirements, evaluation criteria, V1 architecture, ADR, and traceability matrix | Complete |
| W3 | Data source selection, inspection, preparation, and pipeline implementation | Data inventory, prepared datasets, executable pipeline, manifest, and pipeline documentation | In progress |
