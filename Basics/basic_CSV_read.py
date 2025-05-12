import csv

# -----------------------
# Step 1: Create a sample CSV file
# -----------------------
with open('Sample.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # Writing header
    writer.writerow(['Name', 'Age', 'Department', 'Score', 'City'])
    # Writing 3 data rows
    writer.writerow(['Alice', 23, 'Engineering', 88, 'New York'])
    writer.writerow(['Bob', 27, 'Marketing', 76, 'Chicago'])
    writer.writerow(['Charlie', 22, 'Design', 91, 'Los Angeles'])

# -----------------------
# Step 2: Read and print all rows
# -----------------------
print("All Rows in CSV:")
with open('Sample.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # Each row is a list of strings

print("\n")

# -----------------------
# Step 3: Get the i-th row (e.g., 2nd row of data, i = 2)
# Note: Row index 0 is header, so i = 2 means 2nd data row = Bob
# -----------------------
i = 2
with open('Sample.csv', 'r') as file:
    rows = list(csv.reader(file))  # Convert to list for indexing
    if i < len(rows):
        print(f"Row {i}:", rows[i])
    else:
        print(f"Row {i} does not exist.")

print("\n")

# -----------------------
# Step 4: Get the j-th column (e.g., 3rd column = 'Department')
# -----------------------
j = 2  # Column index (0-based): 0=Name, 1=Age, 2=Department
with open('Sample.csv', 'r') as file:
    reader = csv.reader(file)
    column_data = []
    for row in reader:
        if j < len(row):
            column_data.append(row[j])
        else:
            column_data.append("N/A")  # In case the column is missing
    print(f"Column {j} values:", column_data)