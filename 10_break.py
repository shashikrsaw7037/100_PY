# How do you break out of a loop in Python?

# In Python, you can use the break statement to exit or break out of a loop prematurely, regardless of whether it's a for loop or a while loop. The break statement terminates the loop it is inside, and the program continues with the next statement after the loop. Here's how you use break:

# Example with a for loop
for i in range(10):
    if i == 5:
        break
    print(i)

# Example with a while loop
i = 0
while i < 10:
    if i == 5:
        break
    print(i)
    i += 1
