# Program to find quadratic equation 

import math as m

a=int(input("Enter coefficient of a term: "))
b=int(input("Enter coefficient of b term: "))
c=int(input("Enter coefficient of c term: "))
d=(b**2)-4*a*c
r1=(-b + int(m.sqrt(d) )) // (2*a)
r2=(-b - int(m.sqrt(d) )) // (2*a)
print(r1,r2)