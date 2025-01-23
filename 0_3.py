num = int(input("enter the number :"))
if num < 0:
   print("factorial is not defined ,")
else:
   fact = 1
   i = 1 
   while i <= num :
    fact *= i
    i += 1
   print("factorial of the number",num,"is",fact)     