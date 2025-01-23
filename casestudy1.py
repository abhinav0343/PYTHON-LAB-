test_cases=int(input("enter no.of test cases :"))
N=int(input("enter total number of boxes :"))
for j in range(test_cases):
    S=int(input("enter total no.of swaps "))
    X=int(input("enter the current position of the gold coin :"))
    for i in range(S):
       a=int(input("enter the box number of gold coin:"))
       b=int(input("enter the box number to swap :"))
       if X==a :
           X=b
       elif X==b :
           X=a

    print(f"the final position of the coin is {X}")