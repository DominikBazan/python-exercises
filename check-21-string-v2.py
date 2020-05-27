# Checking if "21" is a part of specified string from table

A = [21, 215, 321, 123, 11, 121, 541, 12, 2187, 542173383]
n = len(A)
chosen = []
for i in range(0,n):
   item = str(A[i])
   n_item = len(item)
   a = False
   for j in range(n_item - 1):
       if item[j] == '2':
           if item[j+1] == '1':
               chosen.append(A[i])
print(chosen)