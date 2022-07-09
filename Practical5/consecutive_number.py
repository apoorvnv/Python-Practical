# Program to check if number is consecutive 3 times in list

a=[3,2,3,4,5,3,8,9,0,0,4,4,4,9,1]
z=len(a)
for i in range(z-2):
    if(a[i]==a[i+1] and a[i+1]==a[i+2]):
        print("Consecutive number is: ",end='')
        print(a[i])