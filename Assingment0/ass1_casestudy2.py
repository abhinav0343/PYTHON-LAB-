n = int(input("enter total number of employees "))
list = []
print("enter the heights of each employee ")
for i in range (n) :
    height = float(input())
    list.append(height)
count = 0
#selection sort
for i in range (n) :
    min = i 
    for j in range (i+1,n):
        if list[j] < list[min] :
            min = j
    list[i],list[min] = list[min],list[i]   
    if min != i :
        count += 1
print("heights of the employees ") 
print(list)  
print(f"minimum number of swaps is {count} ")