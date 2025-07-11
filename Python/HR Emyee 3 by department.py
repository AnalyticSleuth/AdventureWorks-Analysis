import pandas as pd

# Load the HR Employee file
hr_employee = pd.read_csv("D:/Generation Course/CW1/CSV data/HR Employee.csv")

# Load the Sick Leave by Department file
sick_leave_by_department = pd.read_csv("D:/Generation Course/CW1/CSV data/sick leave by department.csv")

# Set the department names as the index
sick_leave_by_department.set_index('Department', inplace=True)

# Preview the data
print(hr_employee.head())
print(sick_leave_by_department.head())

import matplotlib.pyplot as plt

# Assume 'dept_job_sick_leave' contains job title distribution within departments


# Assuming sick_leave_by_department contains the data
import matplotlib.pyplot as plt

# Plot the bar chart with blue and orange colors
plt.figure(figsize=(12, 6))
sick_leave_by_department.plot(kind='bar', color=['blue', 'orange'], logy=True)  # logy=True applies logarithmic scale to y-axis
plt.title('Total Sick Leave Hours by Department (Log Scale)')
plt.xlabel('Department')  # Display department names
plt.ylabel('Total Sick Leave Hours (Logarithmic Scale)')
plt.xticks(rotation=45)  # Rotate department names for readability
plt.tight_layout()  # Adjust layout to prevent label cutoff
plt.show()



