def uttopian(num) :
    n = 1
    height = 1
    while n <= num : 
      if n % 2 == 0 :
         height += 1
      elif n % 2 != 0 :
         height = height * 2 
      n += 1
    return height  
test = int(input("enter the number of test cases : "))
for _ in range (test) :
    num = int(input("enter the number of growth cycles : "))
    print(f"height of the uttopian tree is : {uttopian(num)} ")