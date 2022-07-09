# Program to count elements divisible by k

m=[]
n=int(input("Enter the value of n: "))
for i in range(0,50):
    if(i%n==0):
        m.append(i)

m=tuple(m)
print("Tuple of elements divisible by",n)
print(m)