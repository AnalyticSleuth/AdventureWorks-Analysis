import pandas as pd

# Load the HR Employee data
hr_employee = pd.read_csv("D:/Generation Course/CW1/CSV data/HR Employee.csv")

# Inspect columns
print(hr_employee.columns)

# Check for missing values in JobTitle and SickLeavehours
print(hr_employee[['JobTitle', 'SickLeavehours']].isnull().sum())

# Drop rows with missing values
hr_employee_cleaned = hr_employee.dropna(subset=['JobTitle', 'SickLeavehours'])

# Ensure JobTitle values have no leading/trailing spaces
hr_employee_cleaned['JobTitle'] = hr_employee_cleaned['JobTitle'].str.strip()

# Group data by Job Title without aggregation
job_title_sick_leave = hr_employee_cleaned[['JobTitle', 'SickLeavehours']]

# Display the data grouped by job title with individual values
print(job_title_sick_leave)

import matplotlib.pyplot as plt

# Group by Job Title and sum SickLeaveHours
sick_leave_by_job = hr_employee_cleaned.groupby('JobTitle')['SickLeavehours'].sum()

# Plot as a bar chart
plt.figure(figsize=(12, 6))
sick_leave_by_job.plot(kind='bar', color='skyblue')
plt.title('Total Sick Leave Hours by Job Title')
plt.xlabel('Job Title')
plt.ylabel('Total Sick Leave Hours')
plt.xticks(rotation=45)
plt.tight_layout()  # Adjusts layout to prevent label cutoff
plt.show()


import pandas as pd

# Load the HR Employee data
hr_employee = pd.read_csv("D:/Generation Course/CW1/CSV data/HR Employee.csv")

# Preview the first few rows
print(hr_employee.head())

