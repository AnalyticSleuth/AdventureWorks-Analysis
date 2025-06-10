import pandas as pd
import matplotlib.pyplot as plt
# File path to your CSV
file_path = r"D:\\Generation Course\\CW1\\CSV data\\sick leave and work shifts.csv"

# Load the CSV data
data = pd.read_csv(file_path)

# Check if the data loaded correctly
print(data.head())  # Displays the first 5 rows of your data

shift_labels = data['Shift']
sick_leave_hours = data['SickLeavehours']

# Create custom labels with actual hours and percentages
custom_labels = [f"{shift} ({hour} hrs)" for shift, hour in zip(shift_labels, sick_leave_hours)]

# Create the pie chart
plt.figure(figsize=(8, 8))
plt.pie(sick_leave_hours, labels=custom_labels, autopct='%1.1f%%', startangle=90)

# Add a title
plt.title("Sick Leave Hours by Work Shifts")

# Show the plot
plt.show()
plt.show(block=True)