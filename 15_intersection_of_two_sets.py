# Write a Python program to find the intersection of two sets
set1 = {3,4,5}
set2 = {7,8,9,5}
intersection_set =set1.intersection(set2)
print(intersection_set)#{5}

set1 = {3,4,5,7,11,12,15,45}
set2 = {7,8,9,5,11,45,15}
intersection_set =set1 & set2
print(intersection_set)#{5, 7, 11, 45, 15}