# Program to find intersection of lists

def intersection(x,y):
    
    z = [value for value in x if value in y]
    return(z)
   
x = [2,3,7,5,3,2]
y = [4,6,8,9,3,2]
print(intersection(x,y))
