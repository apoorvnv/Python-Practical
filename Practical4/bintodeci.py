# Program to convert Binary to Decimal

n=int(input("Enter a number in Binary: "))

d=0
m=1
while(n>0):
    ld = n%10
    d = d + (ld*m)
    m = m*2
    n = int(n/10)

print(f"Decimal value : {d}")
