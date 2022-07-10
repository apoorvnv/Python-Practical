# Program to Sort Dictionary by ket and value

dict = {'damon': 34,'vansh': 85,'ankush':23,'stefan': 45,'karthik': 63}

print("Sorted by key:")
print(sorted(dict.items(), key=lambda kv: (kv[0], kv[1])))

print("\nSorted by value:")
print(sorted(dict.items(), key=lambda kv: (kv[1], kv[0])))