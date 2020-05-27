# Checking if "21" is a part of specified string from table

A = [21, 215, 321, 123, 11, 121, 541, 12, 2187, 542173383]
n = len(A)
chosen = []
for i in range(n):
   k = A[i]
   while k > 1:
       rest1 = k%10
       k = int(k/10)
       rest2 = k%10
       if rest1 == 1:
           if rest2 == 2:
               chosen.append(A[i])
print(chosen)