# Apoorv Varkute
# Program to print Disarium number
# the sum of its digit raised to the power of their respective positions is equal to the number itself.
# 89 = 8**1 + 9**2

print("Enter a number: ")
n=int(input())
temp=n
sum=0
ln=len(str(n))
n=int(n)
while(n>0):
    p=n%10
    sum = sum +(p**ln)
    ln=ln-1
    n=n//10
if(sum == temp):
    print(temp,"is a Disarium number")
else:
    print(temp,"is not a Disarium number")