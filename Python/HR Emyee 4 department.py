import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

hr_data = pd.read_csv(r'D:\Generation Course\CW1\CSV data\HR Employee.csv')
sick_leave_data = pd.read_csv(r'D:\Generation Course\CW1\CSV data\Sick leave Department and job titles.csv')

merged_data = pd.merge(hr_data, sick_leave_data, left_on='JobTitle', right_on='Job Title')

department_sick_leave = merged_data.groupby('Department')['SickLeaveHours'].sum().reset_index()

department_sick_leave['Log_SickLeaveHours'] = np.log(department_sick_leave['SickLeaveHours'])


location_data = pd.read_csv(r'D:\Generation Course\CW1\CSV data\Sick Leave by Location.csv')
location_merged_data = pd.merge(hr_data, location_data, left_on='JobTitle', right_on='JobTitle')
sick_leave_by_city = location_merged_data.groupby('City')['SickLeaveHours'].sum().reset_index()

# Sort cities by sick leave hours
sick_leave_by_city = sick_leave_by_city.sort_values('SickLeaveHours', ascending=False)

colors = ['orange', 'blue'] * (len(sick_leave_by_city) // 2 + 1)  # Extend the colors to match data length
plt.figure(figsize=(12, 8))
sns.barplot(data=sick_leave_by_city, x='SickLeaveHours', y='City', palette=colors[:len(sick_leave_by_city)])
plt.title('Sick Leave Hours by City', fontsize=14)
plt.xlabel('Total Sick Leave Hours', fontsize=12)
plt.ylabel('City', fontsize=12)
plt.tight_layout()
plt.show()
