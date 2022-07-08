# Prpgram to print Centre Align Pyramid

n = int(input("Enter number of rows: "))
for r in range(1,n+1):
    s=1

    while s<=n-r:
        print(" ",end='')
        s+=1
    c=1
    
    while c<=2*r-1:
        print("*",end='')
        c+=1
    print()