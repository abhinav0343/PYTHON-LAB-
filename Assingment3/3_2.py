def isfibo(num) :
  num1 = 0
  num2 = 1
  n = 0
  if num == 0 or num == 1 :
     return "ISFIBO"
  else :
    while n <= num :
      result = num1 + num2 
      num1 = num2 
      num2 = result
      n += 1 
      if result == num :
         return "ISFIBO"
    return "ISNOTFIBO"
test = int(input("enter the number of test cases : "))
for _ in range (test) : 
    num = int(input("enter the number : "))
    print(isfibo(num))