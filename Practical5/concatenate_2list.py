# Program to concatenate 2 list

l1 = ['0','2','8']
l2 = ['p', 'z', 'd']
print("The original list 1 is : " + str(l1))
print("The original list 2 is : " + str(l2))
s = [i + j for i, j in zip(l1,l2)]
print("The list after element concatenation is : " + str(s))
