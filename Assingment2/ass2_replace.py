input_string = input("enter the string : ")
replace_string = input("enter the string you want to change : ")
new_string = input("enter the string you want to place in orginal string : ")
i,j = 0,0
n = len(input_string)
m = len(replace_string)
result = ""
while i < n :
    if i <= n-m and input_string[i:i+m] == replace_string :
        result += new_string
        i += m
    else :
        result += input_string[i]
        i+=1
print(result)