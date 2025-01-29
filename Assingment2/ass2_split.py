input_string = input("enter the string : ")
split_str = input("enter the character so that splitting will be done : ")
max_split = int(input("enter number of splits : "))
i = 0
result = ""
split_len = len(split_str)
split_count = 0
n = len(input_string)
while i < n :
    if split_count < max_split and input_string[i:i+split_len] == split_str :
        result += ","
        i += split_len
        split_count += 1
    else :
        result += input_string[i]
        i += 1
print(result)       