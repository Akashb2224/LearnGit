import csv

# Path to your CSV file
file_path = r'C:\Users\akash\OneDrive\Desktop\csvfile.csv'

# Writing to a CSV file
with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Writing the header
    writer.writerow(["Name", "Age", "City"])
    
    # Writing multiple rows of data
    writer.writerow(["Alice", 30, "New York"])
    writer.writerow(["Bob", 25, "Los Angeles"])
    writer.writerow(["Charlie", 35, "Chicago"])

print("CSV file created and data written successfully.")

