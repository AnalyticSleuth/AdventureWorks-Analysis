import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# File paths
path = "D:/Generation Course/CW1/CSV data/"

# Load the datasets
hr_employee = pd.read_csv(path + "HR Employee.csv")
sick_leave_location = pd.read_csv(path + "Sick Leave by Location.csv")
sick_leave_department = pd.read_csv(path + "Sick leave Department and job titles.csv")

# Preview the datasets
print("HR Employee Data:")
print(hr_employee.head())

print("\nSick Leave by Location Data:")
print(sick_leave_location.head())

print("\nSick Leave Department and Job Titles Data:")
print(sick_leave_department.head())

# Standardize column names
hr_employee.rename(columns={"Job Title": "JobTitle"}, inplace=True)
sick_leave_location.rename(columns={"Job Title": "JobTitle"}, inplace=True)

# Strip whitespace from JobTitle
hr_employee['JobTitle'] = hr_employee['JobTitle'].str.strip()
sick_leave_location['JobTitle'] = sick_leave_location['JobTitle'].str.strip()
sick_leave_department['JobTitle'] = sick_leave_department['JobTitle'].str.strip()

# Verify the changes
print("\nColumn Names in HR Employee:")
print(hr_employee.columns)

print("\nColumn Names in Sick Leave Location:")
print(sick_leave_location.columns)

print("\nColumn Names in Sick Leave Department:")
print(sick_leave_department.columns)

hr_location_merge = pd.merge(
    hr_employee,
    sick_leave_location,
    on="JobTitle",
    how="inner"
)

print("\nPreview of HR + Location Merge:")
print(hr_location_merge.head())

merged_data = pd.merge(
    hr_location_merge,
    sick_leave_department,
    on="JobTitle",
    how="inner"
)

print("\nPreview of Fully Merged Data:")
print(merged_data.head())

# Check for missing values
print("\nMissing Values in Merged Data:")
print(merged_data.isnull().sum())

# Drop rows with missing values in critical columns
merged_data.dropna(subset=["Gender", "MaritalStatus", "Department", "SickLeaveHours_y"], inplace=True)

# Verify cleaned data
print("\nCleaned Merged Data:")
print(merged_data.head())

# Apply logarithm transformation to sick leave hours
merged_data['Log_SickLeaveHours'] = np.log1p(merged_data['SickLeaveHours_y'])

# Verify the transformation
print("\nPreview of Transformed Data:")
print(merged_data[['JobTitle', 'Department', 'SickLeaveHours_y', 'Log_SickLeaveHours']].head())

# Print column names to verify the correct column name for sick leave hours
print("\nColumn Names in Merged Data:")
print(merged_data.columns)

# Update the pivot table to use the correct column name
heatmap_data = merged_data.pivot_table(
    values="SickLeaveHours_y",  # Use the correct column name
    index="Department",
    columns=["Gender", "MaritalStatus"],
    aggfunc="mean"
)



# Bar plot
plt.figure(figsize=(12, 6))
sns.barplot(
    data=grouped_data,
    x="MaritalStatus",
    y="SickLeaveHours",
    hue="Gender",
    palette=["#FFA500", "#1E90FF"]  # Orange and Blue color theme
)
plt.title("Average Sick Leave Hours by Gender and Marital Status (Grouped by Department)", fontsize=14)
plt.xlabel("Marital Status", fontsize=12)
plt.ylabel("Average Sick Leave Hours", fontsize=12)
plt.legend(title="Gender")
plt.tight_layout()
plt.show()
