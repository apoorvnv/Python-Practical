# Program to remove the ith occurrence

def returnword(x, y, N):
   ct = 0

   for i in range(0, len(x)):
      if (x[i] == y):
         ct += 1

      if(ct == N):
         del(x[i])
         return True
   return False

x = ['Eleven', 'Jane', 'Will', 'Dustin', 'Jane']
print("The list is:",x)
y = 'Jane'
N = 2

flag_val = returnword(x, y, N)

if (flag_val == True):
   print("The updated list is: ",x)
else:
   print("List is not updated")