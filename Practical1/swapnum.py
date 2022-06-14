# Program to swap two numbers

a=int(input("Enter value of a: "))
b=int(input("Enter value of b: "))
print("Before swapping",a,b)
a=a+b
b=a-b
a=a-b
print("After swapping",a,b)