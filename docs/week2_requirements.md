# Week 2: Project Framing and Requirements

## Business Sales Forecasting System for a Petrol Station

# Section 0 — Project Framing and Application Scope

## 0.1 Project Name

**Business Sales Forecasting System for a Petrol Station**

## 0.2 Problem Statement

Petrol stations manage different sales categories, such as Mogas, Diesel, and Kedai Mesra PETRONAS. Historical sales records contain useful information about sales performance, but analysing these records manually can make it difficult to identify trends and estimate future sales.

Without a systematic approach to analysing historical sales data, business users may find it challenging to understand monthly sales patterns and prepare for future business needs.

This project aims to develop a sales forecasting system that analyses historical sales records, identifies sales trends, predicts future monthly sales revenue, and presents forecasting results through clear visualisations.

## 0.3 Evidence of the Problem

**Evidence 1: Microsoft Power BI**

Microsoft Power BI provides business intelligence tools for analysing data, creating visualisations, and monitoring key performance indicators.

Source: https://www.microsoft.com/en-us/power-platform/products/power-bi

**Evidence 2: Microsoft Excel**

Microsoft Excel provides spreadsheet functions for organising sales records, performing calculations, and creating charts.

Source: https://www.microsoft.com/en-us/microsoft-365/excel

These tools demonstrate existing approaches to business data analysis. However, the effectiveness of sales analysis and forecasting depends on the quality of the available data and the methods used.

The project will focus on preparing historical sales records and applying suitable forecasting methods to estimate future monthly sales.

## 0.4 Existing Approaches

### 1. Business Intelligence Dashboards

**Example:** Microsoft Power BI  
**Source:** https://www.microsoft.com/en-us/power-platform/products/power-bi

Power BI supports interactive dashboards, data visualisation, and business reporting.

**Potential gap for this project:** A dashboard can display historical sales information, but forecasting future sales requires an appropriate forecasting method and evaluation process.

### 2. Spreadsheet-Based Analysis

**Example:** Microsoft Excel  
**Source:** https://www.microsoft.com/en-us/microsoft-365/excel

Excel supports data organisation, calculations, comparisons, and charts.

**Potential gap for this project:** Repeated sales analysis and forecasting may require users to prepare calculations and perform additional analysis manually.

### 3. Time-Series Forecasting

**Example:** Statistical forecasting methods  
**Source:** https://otexts.com/fpp3/

Time-series forecasting methods use historical observations to estimate future values. Their performance can be evaluated by comparing predicted values against actual historical values.

**Potential gap for this project:** Forecasting methods need to be selected, tested, and evaluated based on the available petrol station sales data.

## 0.5 Engineering Gap

Existing tools support sales reporting, spreadsheet calculations, data visualisation, and forecasting.

However, this project focuses on developing a specific workflow that prepares historical petrol station sales data, analyses monthly sales patterns, develops forecasting models, and presents the results in an understandable format.

The system will focus on forecasting sales revenue using available historical records from Mogas, Diesel, and Kedai Mesra PETRONAS, depending on the availability and suitability of the data.

The forecasting approach will be evaluated against a simple baseline to determine whether it provides useful predictions.

## 0.6 Project Objectives

- **O1:** To analyse historical sales records and identify monthly sales trends and patterns.
- **O2:** To develop and evaluate machine learning-based forecasting models for predicting future monthly sales revenue.
- **O3:** To develop a system that presents historical sales analysis and forecasting results through clear visualisations.

## 0.7 Application Scope

### Intended Users

The intended users are petrol station owners, managers, or authorised staff who need to review historical sales performance and estimated future sales.

### Supported Tasks

The system is intended to support the following tasks:

1. Import available historical sales records from supported file formats.
2. Inspect and prepare historical sales data for analysis.
3. Analyse sales performance across available sales categories, such as Mogas, Diesel, and Kedai Mesra PETRONAS.
4. Calculate and display historical sales totals and monthly trends.
5. Aggregate suitable historical sales records into monthly data.
6. Develop forecasting models to estimate future monthly sales revenue.
7. Evaluate forecasting performance using suitable evaluation metrics and a simple baseline.
8. Present historical sales trends and forecasting results through charts and summaries.

### Information and Knowledge Domain

The project focuses on:

- Historical petrol station sales records.
- Sales categories and quantities, where available.
- Sales revenue in Malaysian Ringgit (RM).
- Monthly sales trends and patterns.
- Time-series forecasting.
- Forecasting evaluation and performance.

### Operating Context

The initial system will use historical sales records provided with appropriate permission.

The available dataset may contain separate records for fuel sales and Kedai Mesra sales. These datasets will be inspected and prepared according to their actual structures before analysis.

Monthly aggregation will be performed where the available dates and sales values support it.

### Important Constraints

- The completeness and quality of historical sales records may affect the analysis.
- Forecasting performance depends on the amount, consistency, and time coverage of historical data.
- Separate sales categories may require separate preparation and forecasting processes.
- Revenue does not represent profit unless reliable cost and expense information is available.
- Forecasting results are estimates and may not reflect unexpected changes in business conditions.
- The system does not guarantee accurate future predictions.
- Confidential business information must be protected.
- The system is intended for analysis and forecasting, not automatic business decision-making.

### Out-of-Scope Tasks

- Automatically changing fuel prices or business operations.
- Replacing existing accounting or point-of-sale systems.
- Predicting future sales with guaranteed accuracy.
- Calculating business profit without reliable cost and expense data.
- Automatically purchasing or managing stock.
- Integrating live sales systems unless access and project requirements justify it.
- Generating chatbot-based business explanations or recommendations.

## 0.8 Evaluation Focus

The evaluation will determine whether the system:

1. Analyses historical sales records and calculates sales information correctly.
2. Identifies and handles predefined data-quality issues.
3. Aggregates suitable sales records into monthly observations.
4. Produces monthly sales forecasts using suitable forecasting methods.
5. Evaluates forecasting performance using MAE, RMSE, and MAPE where applicable.
6. Compares forecasting performance against a simple baseline.
7. Presents historical sales analysis and forecasting results clearly.
8. Protects confidential sales information and maintains data provenance.
9. Communicates forecasting limitations appropriately.

The dataset must be inspected before finalising the forecasting methods, evaluation period, and performance thresholds.

---

# Section 1 — Functional Requirements (FR)

Functional requirements describe what the system must do. Each requirement must be observable and testable.

| ID | Functional Requirement | Measurement Method | Metric | Initial Threshold |
|---|---|---|---|---|
| FR1 | The system shall analyse historical sales records and identify sales trends and patterns using available dates, sales categories, quantities, and sales values. | Compare system-generated sales totals and selected indicators against independently calculated expected values. | Calculation correctness rate | 100% of predefined valid-data calculation test cases, allowing documented rounding differences. |
| FR2 | The system shall generate monthly sales revenue forecasts using suitable forecasting methods and available historical sales data. | Evaluate predictions against a held-out historical period and compare model performance against a simple baseline. | MAE, RMSE, and MAPE where applicable | Target at least 5% lower MAE than the baseline, where meaningful and feasible. |
| FR3 | The system shall present historical sales analysis and forecasting results through clear charts, tables, and summaries. | Test whether the system displays the correct historical values, forecast values, time periods, and sales categories. | Correct result presentation rate | 100% of predefined result-presentation test cases. |

**Notes:**

- FR1 focuses on understanding historical sales performance.
- FR2 focuses on predicting future monthly sales revenue.
- FR3 focuses on presenting the analysis and forecasting results.
- Forecasting methods will be selected based on the available dataset and its characteristics.
- A simple baseline may include the previous month's sales or another suitable naive forecasting method.
- MAE and RMSE measure forecasting errors. MAPE will only be used when actual values are suitable for percentage-based evaluation, particularly when actual sales values are not zero.
- The 5% improvement target is an initial evaluation goal, not a guarantee. If the model does not outperform the baseline, the findings and limitations must be reported honestly.
- The forecasting target may be adjusted after examining the actual data.

---

# Section 2 — Non-Functional Requirements (NFR)

Non-functional requirements describe the quality and usability of the system.

| ID | Quality Attribute | Requirement | Measurement Method | Metric | Initial Threshold |
|---|---|---|---|---|---|
| NFR1 | Forecast Accuracy | The system shall produce forecasting results with measurable errors and evaluate performance against a simple baseline. | Evaluate model predictions using a held-out historical period. | MAE, RMSE, and MAPE where applicable. | Report all applicable metrics and baseline comparisons. Aim for at least 5% lower MAE than the baseline where meaningful and feasible. |
| NFR2 | Data Quality | The system shall identify predefined data-quality issues before using historical sales records for analysis and forecasting. | Test datasets containing missing dates, invalid sales values, duplicate records, and inconsistent formats where applicable. | Data validation correctness rate. | 100% of predefined data-quality test cases handled according to documented rules. |
| NFR3 | Usability | The system shall present historical sales analysis and forecasting results in a clear and understandable interface. | Conduct predefined usability tasks and collect feedback from representative users. | Task completion rate. | At least 80% of predefined tasks completed successfully by participating users. |

The proposed thresholds are initial targets and may be reviewed during implementation and testing.

Forecast accuracy will depend on the available historical data, forecasting method, and evaluation period.

---

# Section 3 — Responsible AI Requirements (RAI)

Responsible AI requirements define practices to protect business information, maintain data traceability, and avoid misleading forecasting results.

| ID | Responsible AI Focus | Requirement | Measurement Method | Metric | Initial Threshold |
|---|---|---|---|---|---|
| RAI1 | Data Privacy | The system shall protect confidential sales records and ensure that data is only accessed or used for authorised project purposes. | Review data storage, repository contents, access permissions, and data-sharing practices. | Privacy and access-control checklist pass rate. | All defined privacy safeguards must be implemented and verified before confidential data is shared or deployed. |
| RAI2 | Data Provenance | The system shall maintain information about the source of historical sales data and the processing steps used to prepare forecasting datasets. | Inspect data manifests, source information, processing records, and dataset versions. | Provenance documentation completeness rate. | 100% of required provenance fields documented for the datasets used in the final evaluation. |
| RAI3 | Forecasting Transparency | The system shall communicate that forecasting results are estimates and identify relevant limitations, including insufficient historical data and forecasting errors. | Review forecast displays, labels, evaluation results, and documented limitations. | Forecast transparency checklist pass rate. | All predefined forecast-transparency checks must pass. |

## Reflection: Most Difficult Responsible AI Requirement

RAI3, which focuses on communicating forecasting limitations, may be challenging because forecasting models can produce numerical predictions that appear reliable even when the available historical data is limited.

For example, unexpected changes in fuel demand, business conditions, or customer behaviour may cause actual sales to differ from predicted values.

The system should therefore present forecasts as estimates rather than guaranteed future sales. Forecasting errors and relevant limitations should also be reported so that users can interpret the results appropriately.

---

## Requirement Review

Before implementation, the following checks should be completed:

- Confirm that all three project objectives are supported by the functional requirements.
- Ensure FR1 focuses on historical sales analysis, FR2 on monthly sales forecasting, and FR3 on presenting results.
- Inspect the available dataset and confirm its actual structure, fields, and time coverage.
- Confirm that each requirement has a measurable testing method and suitable evaluation criteria.
- Ensure the evaluation criteria use the same requirement IDs as this document.
- Verify that confidential business data is handled with appropriate permission and protection.
- Maintain data provenance through source records, processing information, and dataset manifests.
- Communicate forecasting errors, uncertainty, and limitations clearly.
- Review the requirements if the available dataset or implementation constraints make an initial target unsuitable.
- Refine the requirements if the available data or implementation constraints make a target unsuitable.
