num1 = int(input("enter the first value : "))
num2 = int(input("enter the second value : ")) + 1
xor_max = []
for i in range (num1,num2) :
    for j in range (i,num2) :
        val = i ^ j
        xor_max.append(val)
print(f"{max(xor_max)}")
