import csv

# Path to your CSV file
file_path = r'C:\Users\akash\OneDrive\Desktop\fileme.csv'

# Writing to a CSV file
file = open(file_path, mode='w', newline='')  # Open the file in write mode
writer = csv.writer(file)

# Writing the header
writer.writerow(["Name", "Age", "City"])

# Writing multiple rows of data
writer.writerow(["Alice", 30, "New York"])
writer.writerow(["Bob", 25, "Los Angeles"])
writer.writerow(["Charlie", 35, "Chicago"])

# Close the file manually
file.close()
print("CSV file created and data written successfully.")

# Appending to the CSV file
file = open(file_path, mode='a', newline='')  # Open the file in append mode
writer = csv.writer(file)

# Appending more rows of data
writer.writerow(["David", 40, "Houston"])
writer.writerow(["Eve", 28, "Phoenix"])

# Close the file manually
file.close()
print("Data appended successfully.")




