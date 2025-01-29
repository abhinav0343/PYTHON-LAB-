import sys
result = []
input_str = input("enter the string :")
print(f"length of the string is {len(input_str)}")
input_list = list(input_str)
find = input("enter the value/letter to find :")
start = int(input("enter the position to start :")) - 1
if start >= len(input_str) or start < 0:
    print('start position is invalid ')
    sys.exit() #used to exit the code when there are no loops 
end = int(input('enter the position to end : '))
if end > len(input_str) or end <= start:
    print("end position is invalid ")
    sys.exit() #used to exit the code when there are no loops
count = 0   
for i in range (start,end) :
    if input_list[i] == find :
       result.append(i)
       count += 1
if count == 0 :
    print("no such letter/value is found ")   
else :       
    print(result[count-1])       