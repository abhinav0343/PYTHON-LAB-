import math
test = int(input("enter number of test cases : "))
for i in range (test) :
    a = int(input("enter the value of 'A' : "))
    b = int(input("enter the value of 'B' : ")) + 1
    count = 0
    for j in range(a,b) :
       mid = b/2 + 1
       mid = int(mid)
       for k in range(1,mid) :
           if pow(k,2) == j :
               count += 1
    print(count)               
