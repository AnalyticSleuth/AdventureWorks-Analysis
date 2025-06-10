import pandas as pd

# Load the CSV file
file_path = r"D:\Generation Course\CW1\CSV data\Sick leave by gender and geo.csv"
data = pd.read_csv(file_path)

print(data.head())  # Shows the first 5 rows
print(data.columns)  # Lists all column names

grouped_data = data.groupby(['Sex', 'City'])['SickLeaveHours'].sum().reset_index()
print(grouped_data)


import seaborn as sns
import matplotlib.pyplot as plt

# Create a bar plot
plt.figure(figsize=(10, 6))
sns.barplot(data=grouped_data, x='City', y='SickLeaveHours', hue='Sex')
plt.title("Sick Leave Hours by Sex and City")
plt.xlabel("City")
plt.ylabel("Sick Leave Hours")
plt.legend(title="Sex")
plt.xticks(rotation=45)  # Rotate city names for better readability
plt.tight_layout()
plt.show()