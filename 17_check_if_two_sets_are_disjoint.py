# Write a program to check if two sets are disjoint
# The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False.


set1 = {5, 7, 11, 45, 15}
set2 = {3,23,44,55,66,77}
print("====>",set1.isdisjoint(set2))
if set1.isdisjoint(set2):
    print("Sets are disjoint")
else:
    print("no")
    
print()    
    
set1 = {5, 7, 11, 45, 23,44}
set2 = {3,23,44,55,66,77}
print("====>",set1.isdisjoint(set2))
if set1.isdisjoint(set2):
    print("Sets are disjoint")
else:
    print("no")
    
    
set1={"vjhbf",3232,32324}
print(set1)
