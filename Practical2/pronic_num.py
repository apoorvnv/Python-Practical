# Apoorv Varkute
# Program to print pronic number
# eg : 42 = 6*7 

print("Enter a number: ")
n=int(input())
flag=0
for i in range(1,n):
    if( (n%i==0 and n%(i+1)==0) and i*(i+1)==n ):
        flag=1
        break
    else:
        continue
if(flag==1):
    print(n,"is a Pronic number")
else:
    print(n,"is not a Pronic number")