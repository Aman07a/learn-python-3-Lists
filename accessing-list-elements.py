# Define the list of employees
employees = ["Michael", "Dwight", "Jim", "Pam", "Ryan", "Andy", "Robert"]

# Step 1: Access the 4th employee from the list (index 3) and save it to employee_four
employee_four = employees[3]
print("4th Employee:", employee_four)

# Step 2: Demonstrate the IndexError when accessing an out-of-range index (index 8)
# print(employees[8])  # This line will raise an IndexError

# Step 3: Access an existing index (index 2) to avoid IndexError
print("3rd Employee:", employees[2])
