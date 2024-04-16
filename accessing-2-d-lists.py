# Step 1: Create the class_name_test 2D list to represent student names and test scores
class_name_test = [
    ["Jenny", 90],
    ["Alexus", 85.5],
    ["Sam", 83],
    ["Ellie", 101.5]
]

# Print the class_name_test to see the result
print(class_name_test)

# Step 2: Access Sam's test score from class_name_test using double square brackets
sams_score = class_name_test[2][1]
print(sams_score)

# Step 3: Access Ellie's test score from class_name_test using negative indices
ellies_score = class_name_test[-1][1]
print(ellies_score)
