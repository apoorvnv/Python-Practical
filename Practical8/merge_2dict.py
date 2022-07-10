# two lists are given, one has keys and other has values, merge them two

combine = {}

keys = ["apple","guava","mango"] 
values = ["red","green","yellow"]

for k,v in zip(keys,values):
    combine[k] = v
print(combine)
