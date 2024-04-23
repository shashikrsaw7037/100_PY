# How can you add an element to a set in Python?
# Define an empty set
my_set = set()

# Add a single element to the set
my_set.add(5)
print(my_set)  # Output: {5}

# Add another element to the set
my_set.add(10)
print(my_set)  # Output: {10, 5}


# Define a set with some initial elements
my_set = {1, 2, 3}

# Update the set by adding one or more elements
my_set.update([4, 5])
print(my_set)  # Output: {1, 2, 3, 4, 5}

# You can also update the set with elements from another set
another_set = {6, 7, 8}
my_set.update(another_set)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}
