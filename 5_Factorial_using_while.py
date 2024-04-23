#Write a Python program to find the factorial of a number using a while loop.
i= 1
n =int(input("Enter number"))
fac = 1
while i<=n:
    fac *=i
    i+=1
print("Factorial",fac)