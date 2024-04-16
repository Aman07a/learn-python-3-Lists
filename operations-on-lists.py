# Create lists for subjects and grades
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

# Combine subjects and grades into a two-dimensional list (gradebook)
gradebook = [
    [subjects[0], grades[0]],
    [subjects[1], grades[1]],
    [subjects[2], grades[2]],
    [subjects[3], grades[3]]
]

# Add computer science and visual arts grades using append
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

# Modify the grade for visual arts by adding 5 points
gradebook[-2][1] += 5

# Switch poetry grade to "Pass" and remove the numerical grade
poetry_index = subjects.index("poetry")
gradebook[poetry_index][1] = "Pass"

# Combine with last semester's gradebook
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]
full_gradebook = gradebook + last_semester_gradebook

# Print the full gradebook directly without using a loop
print(full_gradebook)
