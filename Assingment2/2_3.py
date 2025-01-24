import sys
import math
test = int(input("enter the no:of test cases "))
if test > 15 or test < 0 :
    print("no:of test cases is invalid ")
    sys.exit()  # to exit the program , break should be used in only loops
nums = []
for i in range (test) :
    num = int(input("enter the number : "))
    if num <= pow(10,10) and num >= 0 :
        nums.append(num)
    else :
        print(" invalid number ")
        sys.exit()
newnums = list(map(int,nums) )       
for i in range (test) : 
    val = newnums[i]
    num = val
    count = 0
    while val != 0 :
        digit = val % 10     
        if digit != 0 and num % digit == 0 :
            count += 1
        val //= 10
    print(f"no:of digits in the number that are exactly dividing is : {count}")     