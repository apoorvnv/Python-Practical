# Pogram to find difference between two lists

y=[2,3,51,9,8]
z=[3,6,1]
re=[]

for i in y + z:
    if i not in y or i not in z:
        re.append(i)

print("list 1 is :",y)
print("list 2 is :",z)
print("The resultant list is :",re)
