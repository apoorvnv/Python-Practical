# Apoorv Varkute
# Program to print harshad number from 1 to 100 

for n in range(1,101):
    sum=0
    temp=n
    while(n>0):
        sum+=(n%10)
        n=n//10
    if(temp%sum == 0):
        print(temp,"is a Harshad Number")