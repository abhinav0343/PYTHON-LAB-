def digital_root(num) :
    while num >= 10 :
        num = sum(int(digit) for digit in str(num)) # sum is inbuilt function for calculating sum of the digits 
    return num
num = int(input("enter the number : "))
print(digital_root(num))
