# Program to print elements whose whose frequncy is greater than K


t=[4,5,7,4,4,3,7,7,2,3,7,1,9]
print("The list is : "+str(t))
k=int(input("Enter value of K: "))
r=[]

for i in t:
    fq = t.count(i)
    if(fq>k and i not in r):
        r.append(i)

        print("The required elements are: "+str(r))