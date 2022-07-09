# Apoorv Varkute
# find length of string using recurssion

def av(t):
    if(t == ''):
        return 0
    else:
        return 1 + av(t[1:])

t=(input("Enter string: "))
print("length of string is ")
x = av(t)
print(x)