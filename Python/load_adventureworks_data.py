import pandas as pd
import pyodbc

# Define the connection parameters
server = 'GYE-5CG94112YP\SERVER1'  # Replace with your SQL Server name
database = 'AdventureWorks2019'  # Replace with your restored database name
username = 'GYE-5CG94112YP\SERVER1'  # Replace with your SQL Server username
password = 'Hola@2024!'  # Replace with your SQL Server password

# Create the connection string
connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"

# Establish the connection
try:
    connection = pyodbc.connect(connection_string)
    print("Connection successful!")
except Exception as e:
    print(f"Error connecting to database: {e}")
    exit()

# Query the database and load data into a dataframe
query = "SELECT TOP 10 * FROM [Sales.Customer] ORDER BY CustomerID"  # Sort by CustomerID
try:
    dataframe = pd.read_sql(query, connection)
    print(dataframe)
except Exception as e:
    print(f"Error executing query: {e}")

# Close the connection
connection.close()
