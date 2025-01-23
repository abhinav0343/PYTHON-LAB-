list = []
for i in range (1,11) :
    num1 = float(input(f"enter x co-ordinate for point {i}:"))
    num2 = float(input(f"enter y co-ordinate for point {i}:"))
    num3 = float(input(f"enter z co-ordinate for point {i}:"))
    a = [num1,num2,num3]
    list.append(a)
new_list=[]
for i in range (1,11):
    target = list[i-1]
    min_dist = float('inf')  #it takes min_dist to very very large value
    for point in list:
      if point == target :
         continue  # skip the point if it equals to target
      distance = ((point[0] - target[0])**2 + (point[1] - target[1])**2 + (point[2] - target[2])**2) ** 0.5
      if distance < min_dist :
         min_dist = distance
         near_point = point
    new_list.append((target,near_point))
print(new_list)       
