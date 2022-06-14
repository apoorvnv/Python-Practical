# Apoorv Varkute 
# ascending and descending in array

h=list(map(int,input("Enter array elements: ").split()))
print("Array elements in Ascending order: ")
h.sort()
print(*h)
h.sort(reverse=True)
print("Array elements in Descending order: ")
print(*h)
