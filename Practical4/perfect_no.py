n=int(input("Enter a number: "))
ct=0
for i in range(1,n):
    if(n%i==0):
        ct+=i
if(n==ct):
    print("Yes, It is a Perfect number")
else:
    print("No, It is not a Perfect number")