# Program to sort elements in tuple

def count_digits(v):
    for i in v:
        return sum([len(str(i))])
d = [(34,7,3,54), (3,7,5,25), (23,66,85,3), (33,65,43,23)]
print("Original list is:", d)
d.sort(key=count_digits)
print("Sorted list is:", d)