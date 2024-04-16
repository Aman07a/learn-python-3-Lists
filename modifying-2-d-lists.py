# Create a two-dimensional list representing incoming students
incoming_class = [
    ["Kenny", "American", 9],
    ["Tanya", "Ukrainian", 9],
    ["Madison", "Indian", 7]
]

# Print the initial incoming_class list
print(incoming_class)

# Modify Madison's grade from 7 to 8 using positive indices
incoming_class[2][2] = 8

# Print incoming_class after modifying Madison's grade
print(incoming_class)

# Modify Kenny's name to "Ken" using negative indices
incoming_class[-3][-3] = "Ken"

# Print incoming_class after modifying Kenny's name
print(incoming_class)
