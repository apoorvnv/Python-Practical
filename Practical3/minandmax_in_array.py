# Apoorv Varkute
# find min and max element in array

r=list(map(int,input("Enter array elements: ").split()))
r.sort()
mi=r[0]
mx=r[-1]
print("Minimum element of array is: ",mi)
print("Maximum element of array is: ",mx)