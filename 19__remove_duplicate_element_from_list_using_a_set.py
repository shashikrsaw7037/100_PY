# Write a Python program to remove duplicate elements from a list using a set.

listElement = ["aa",7,8,"aa",78,21,8,3,12,9,78]

Remove_duplicate = set(listElement)
print("Original LIST :",listElement)

print("After Removing:",list(Remove_duplicate))