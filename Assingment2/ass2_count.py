input_string = input("enter the string : ")
count_string = input("enter the sub-string that you want to count : ")
i=0
count = 0
n = len(input_string)
m = len(count_string)
while i <= n - m :
    if input_string[i:i+m] == count_string :
        count += 1
        i += 1  # here we are incrementing by m because to avoid overlap mistakes
    # if you increment by 1 it cause overlap , just check for ababab
    else :
        i += 1
print(count)    