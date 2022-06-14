# Apoorv Varkute
# code to find Armstrong number 

print("Enter number: ")
n=int(input())
dg=0
temp=n
c=0
sum=0
p=0
c=n
while(n>0):
    dg+=1
    n=n//10
while(c>0):
    p=c%10
    sum = sum + (p**dg)
    c=c//10
if(temp == sum):
    print(temp,"is a Armstrong number")
else:
    print(temp,"is not a Armstrong number")
