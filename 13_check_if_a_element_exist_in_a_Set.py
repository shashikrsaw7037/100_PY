# Write a program to check if a given element exists in a set.
Element =  {1, 2, 3, 4, 5}
n=int(input("Enter number:"))

if n in Element:
    print("Element already exist")
else:
    print("Element is not there")