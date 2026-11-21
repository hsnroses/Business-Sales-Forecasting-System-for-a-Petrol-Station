
import os
import pandas as pd

def run_pipeline(input_file, output_folder):

    os.makedirs(output_folder, exist_ok=True)

    # Read required Excel sheets
    fuel = pd.read_excel(
        input_file,
        sheet_name="Fuel_Product"
    )

    kedai = pd.read_excel(
        input_file,
        sheet_name="Royalty_Summary"
    )

    # Prepare fuel data
    fuel["Month"] = pd.to_datetime(fuel["Month"])
    fuel = fuel.sort_values(
        ["Month", "Fuel"]
    ).reset_index(drop=True)

    # Prepare Kedai Mesra data
    kedai["Month"] = pd.to_datetime(kedai["Month"])
    kedai = kedai.sort_values(
        "Month"
    ).reset_index(drop=True)

    # Aggregate monthly fuel sales
    monthly_fuel = (
        fuel.groupby("Month")["Amount_RM"]
        .sum(min_count=1)
        .reset_index()
    )

    monthly_fuel.rename(
        columns={"Amount_RM": "Fuel_Sales_RM"},
        inplace=True
    )

    # Extract monthly Kedai Mesra sales
    monthly_kedai = kedai[
        ["Month", "Total_Sales_RM"]
    ].copy()

    monthly_kedai.rename(
        columns={
            "Total_Sales_RM": "Kedai_Mesra_Sales_RM"
        },
        inplace=True
    )

    # Save all four datasets
    outputs = {
        "prepared_fuel_sales.csv": fuel,
        "prepared_kedai_mesra_sales.csv": kedai,
        "monthly_fuel_sales.csv": monthly_fuel,
        "monthly_kedai_mesra_sales.csv": monthly_kedai
    }

    for filename, dataframe in outputs.items():
        dataframe.to_csv(
            os.path.join(output_folder, filename),
            index=False
        )

    print("Pipeline completed successfully!")
    print("\nGenerated files:")

    for filename in outputs:
        print(filename)


print("Pipeline script created.")
