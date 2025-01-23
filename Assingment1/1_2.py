import random                 # in built function to get random integers.
ran_num = [random.randint(0,1) for _ in range (100)]
count = 0 
max_num = 0
for num in ran_num :
    if num == 0 :
        count += 1
        max_num = max(max_num,count)
    else :
        count = 0    
print(f'randomly generated numbers are  ')
print(f'N{ran_num}')  
print(f"maximum number of conequtive 0's are : {max_num}")      