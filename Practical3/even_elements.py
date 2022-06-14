# Apoorv Varkute
# Print even position elements

a=list(map(int,input("Enter a list: ").split()))
l_a=len(a)
print("Array elements at even position are: ")
for i in range(1,l_a,2):
    print(a[i],end=' ')