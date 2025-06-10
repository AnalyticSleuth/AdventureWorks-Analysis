import pandas as pd

# Load the HR Employee dataset
hr_employee_df = pd.read_csv("HR Employee.csv")

# View the first few rows to understand the data structure
print(hr_employee_df.head())

# Check for missing values in the dataset
print("Summary of missing values:")
print(hr_employee_df.isnull().sum())

# Drop rows with missing data (if applicable) or decide how to handle them
hr_employee_df.dropna(inplace=True)

# Additional inspection for null or missing data
print("Are there any null values remaining?")
print(hr_employee_df.isnull().any())

# Load additional dataset
hr_department_df = pd.read_csv("HR Department.csv")

# Merge HR Employee and HR Department datasets
merged_df = pd.merge(hr_employee_df, hr_department_df, how="inner", on="DepartmentID")

# View the merged data
print(merged_df.head())