# Define the initial list for the grocery store display
front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]

# Print the initial list
print("Initial display list:")
print(front_display_list)

# Jiho wants to add "Pineapple" to the front of the list
item_to_add = "Pineapple"
index_to_insert = 0  # Insert at the front of the list

# Use the .insert() method to add "Pineapple" at the specified index
front_display_list.insert(index_to_insert, item_to_add)

# Print the updated list after inserting "Pineapple"
print("\nUpdated display list after adding Pineapple:")
print(front_display_list)
