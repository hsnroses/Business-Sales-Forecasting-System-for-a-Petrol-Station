# Week 2: Evaluation Criteria

## Business Sales Forecasting System for a Petrol Station

## 1. Evaluation Overview

This document defines how the Business Sales Forecasting System for a Petrol Station will be evaluated.

The evaluation criteria are mapped to the project objectives, functional requirements (FR), non-functional requirements (NFR), and Responsible AI requirements (RAI).

The main purpose is to ensure that the system can analyse historical sales records, generate monthly sales forecasts, present forecasting results clearly, and handle business data responsibly.

## 2. Evaluation Criteria Mapping

| Objective / Requirement | Evaluation Criteria | Architecture Component | Evidence of Implementation |
|---|---|---|---|
| O1 / FR1: Analyse historical sales records and identify sales trends and patterns. | EC1: Sales calculation and analysis correctness. | Data Input, Data Validation, and Sales Analysis | Test results show that sales totals, quantities, and selected indicators match independently calculated expected values. |
| O2 / FR2: Develop and evaluate monthly sales forecasting models. | EC2: Forecasting performance compared with a simple baseline. | Data Preparation, Forecasting Component, and Evaluation Process | Evaluation results report MAE, RMSE, and applicable MAPE values using held-out historical data, together with baseline comparisons. |
| O3 / FR3: Present historical sales analysis and forecasting results clearly. | EC3: Result presentation correctness and clarity. | Analysis and Forecasting Results Dashboard | Test results confirm that displayed historical values, forecast values, sales categories, and time periods match the generated results. |
| NFR1: Ensure measurable forecasting accuracy. | EC2: Forecasting performance. | Forecasting Component and Evaluation Process | Forecasting errors and baseline comparisons are recorded and reported. |
| NFR2: Maintain data quality before analysis and forecasting. | EC4: Data validation effectiveness. | Data Input and Data Validation | Validation tests identify missing dates, invalid sales values, duplicate records, and inconsistent formats where applicable. |
| NFR3: Provide a clear and usable system interface. | EC5: System usability. | User Interface and Dashboard | Usability testing records task completion rates and user feedback. |
| RAI1: Protect confidential business sales data. | EC6: Data privacy and access protection. | Data Storage and Access Controls | Evidence shows that confidential data is protected and access or sharing follows the defined permissions. |
| RAI2: Maintain data provenance and processing traceability. | EC7: Data provenance and traceability. | Data Processing Pipeline and Data Manifest | Source information, processing records, dataset versions, and output information are documented. |
| RAI3: Communicate forecasting limitations clearly. | EC8: Forecast transparency. | Forecasting Results and Reporting Component | Forecast displays and reports identify predictions as estimates and communicate relevant errors and limitations. |

## 3. Detailed Evaluation Methods

### EC1: Sales Calculation and Analysis Correctness

**Related requirements:** O1 and FR1

**Purpose:** To verify that the system correctly analyses historical sales records.

**Evaluation method:**
1. Select representative historical sales records.
2. Calculate expected sales totals and selected indicators independently.
3. Compare the independently calculated values with the system outputs.
4. Investigate any differences.

**Metric:** Calculation correctness rate.

**Initial threshold:** 100% of predefined valid-data calculation test cases, allowing documented rounding differences.

**Evidence:**
- Sample input records.
- Independently calculated expected values.
- System-generated results.
- Comparison and test results.

### EC2: Forecasting Performance

**Related requirements:** O2, FR2 and NFR1

**Purpose:** To evaluate how accurately the forecasting model predicts future monthly sales revenue.

**Evaluation method:**
1. Prepare suitable historical sales data and aggregate it into monthly observations.
2. Divide the data into training and testing periods based on time order.
3. Train suitable forecasting models using the training data.
4. Generate predictions for the held-out testing period.
5. Compare predictions against actual sales values.
6. Compare model performance against a simple forecasting baseline.

**Metrics:**

- **MAE (Mean Absolute Error):** Measures the average absolute difference between actual and predicted sales values.
- **RMSE (Root Mean Squared Error):** Measures forecasting errors while giving greater weight to larger errors.
- **MAPE (Mean Absolute Percentage Error):** Measures forecasting errors as percentages when actual values are suitable for percentage-based calculation.

**Initial threshold:** Aim for at least 5% lower MAE than the baseline where meaningful and feasible. All applicable evaluation metrics and baseline results must be reported.

**Evidence:**
- Training and testing data periods.
- Actual and predicted monthly sales.
- MAE, RMSE, and applicable MAPE results.
- Baseline forecasting results.
- Forecast comparison charts.

**Important:** Random train-test splitting should be avoided for time-series forecasting because it can introduce information from future periods into model training. The testing period must remain separate from the training period.

### EC3: Result Presentation Correctness and Clarity

**Related requirements:** O3 and FR3

**Purpose:** To ensure that historical sales analysis and forecasting results are presented correctly and understandably.

**Evaluation method:**
1. Check the displayed historical sales values against the analysis results.
2. Check that forecast values match the forecasting model outputs.
3. Verify that charts and tables display the correct sales categories and time periods.
4. Review whether the displayed information is understandable to intended users.

**Metric:** Correct result presentation rate.

**Initial threshold:** 100% of predefined result-presentation test cases.

**Evidence:**
- Dashboard screenshots.
- Historical sales charts.
- Forecast visualisations.
- Comparison between displayed values and generated results.

### EC4: Data Validation Effectiveness

**Related requirement:** NFR2

**Purpose:** To ensure that historical sales data is checked before being used for analysis and forecasting.

**Evaluation method:**
1. Inspect the available historical sales datasets.
2. Check for missing dates and sales values.
3. Identify invalid or negative sales values where they are not valid.
4. Check for duplicate records based on appropriate business keys.
5. Identify inconsistent date, category, or numerical formats.
6. Record how identified issues are handled.

**Metric:** Data validation correctness rate.

**Initial threshold:** 100% of predefined data-quality test cases must be handled according to documented validation rules.

**Evidence:**
- Data inventory.
- Missing-value summaries.
- Duplicate-record checks.
- Validation results.
- Data cleaning and preparation records.

### EC5: System Usability

**Related requirement:** NFR3

**Purpose:** To determine whether intended users can understand and use the system to review historical sales and forecasting results.

**Evaluation method:**
1. Ask representative users to perform predefined tasks.
2. Observe whether users can locate historical sales information.
3. Ask users to view monthly sales trends and forecasting results.
4. Record successful task completion and feedback.

**Metric:** Task completion rate.

**Initial threshold:** At least 80% of predefined tasks completed successfully by participating users.

**Evidence:**
- Usability test scenarios.
- Task completion records.
- User feedback.
- Screenshots of the interface.

### EC6: Data Privacy and Access Protection

**Related requirement:** RAI1

**Purpose:** To protect confidential business sales information from unauthorised access or disclosure.

**Evaluation method:**
1. Review the permissions for accessing the original sales dataset.
2. Check whether confidential raw data is exposed in the public GitHub repository.
3. Review data storage and sharing practices.
4. Confirm that only authorised data is used and shared.

**Metric:** Privacy and access-control checklist pass rate.

**Initial threshold:** All defined privacy safeguards must be implemented and verified before confidential data is shared or deployed.

**Evidence:**
- Data access and permission records.
- Repository inspection.
- Data protection checklist.
- Evidence of restricted access where applicable.

### EC7: Data Provenance and Traceability

**Related requirement:** RAI2

**Purpose:** To maintain information about where the sales data originated and how it was processed.

**Evaluation method:**
1. Identify the original data source.
2. Record the source file and relevant worksheet information.
3. Document the data preparation and transformation steps.
4. Record the processed dataset filenames and versions.
5. Maintain relevant processing manifests and data lineage information.

**Metric:** Provenance documentation completeness rate.

**Initial threshold:** 100% of required provenance fields documented for datasets used in the final evaluation.

**Evidence:**
- Data inventory.
- Source information.
- Processing pipeline documentation.
- Dataset manifests.
- Prepared dataset records.

### EC8: Forecast Transparency

**Related requirement:** RAI3

**Purpose:** To ensure users understand that forecasting results are estimates and may contain errors.

**Evaluation method:**
1. Review the forecast charts and result summaries.
2. Check whether forecasts are clearly labelled as predicted values.
3. Verify that forecasting errors are reported.
4. Check whether limitations related to historical data coverage and unexpected business changes are communicated.

**Metric:** Forecast transparency checklist pass rate.

**Initial threshold:** All predefined forecast-transparency checks must pass.

**Evidence:**
- Forecast result screenshots.
- Forecast evaluation metrics.
- Documented model limitations.
- Forecast reporting descriptions.

## 4. Overall Evaluation Summary

| Evaluation Criteria | Related Requirements | Main Evaluation Evidence |
|---|---|---|
| EC1: Sales Calculation and Analysis Correctness | O1 / FR1 | Independent calculation comparisons |
| EC2: Forecasting Performance | O2 / FR2 / NFR1 | MAE, RMSE, MAPE and baseline comparison |
| EC3: Result Presentation Correctness and Clarity | O3 / FR3 | Dashboard and result verification |
| EC4: Data Validation Effectiveness | NFR2 | Data-quality checks and validation results |
| EC5: System Usability | NFR3 | Usability testing and task completion records |
| EC6: Data Privacy and Access Protection | RAI1 | Privacy and access-control evidence |
| EC7: Data Provenance and Traceability | RAI2 | Data manifests and processing records |
| EC8: Forecast Transparency | RAI3 | Forecast labels, errors and limitations |

## 5. Evaluation Considerations

The evaluation will be conducted using the actual available sales dataset and implemented system.

The following considerations will be applied:

1. Forecasting methods will be selected based on the available data and its time coverage.
2. A time-based training and testing approach will be used to prevent data leakage.
3. Forecasting results will be compared against a simple baseline.
4. Missing, duplicate, invalid, or inconsistent records will be investigated and documented.
5. Forecasting metrics will be reported honestly without claiming performance that has not been demonstrated.
6. Confidential business data will not be published without appropriate permission.
7. Data sources and processing activities will be documented to maintain traceability.
8. Forecasting limitations will be communicated clearly to prevent users from treating predictions as guaranteed future sales.

**Note:** All initial thresholds in this document are evaluation targets. Actual results will be recorded after implementation and testing.
If the forecasting approach cannot provide better or otherwise useful results than a simple baseline, it may not provide enough value to justify its additional complexity. However, forecasting accuracy alone is not sufficient. The system must also calculate sales correctly, protect confidential information, and provide explanations that users can verify.
