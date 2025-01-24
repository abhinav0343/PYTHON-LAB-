items = {} # intializing a dictionary 
num = 1
while num == 1 :
    name = input("enter the name of the item : ")
    price = input("enter the price of the item : ")
    items[name] = price 
    num = int(input("enter the choice (1,0) continue and end respectively = "))
num = 1    
while num == 1 :
    names = input("enter the item name you want to access : ")
    if names in items :
      print(f"{names} price is",items[names])
    else :
        print("name of the item is invalid ")
    num = int(input("enter the choice (1,0) continue and end respectively "))