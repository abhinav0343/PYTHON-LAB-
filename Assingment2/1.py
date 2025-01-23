name=[]
x = list(input("enter the name "))
for i in range (len(x)) :
    if i%2 != 0:
        name.append(x[i].capitalize()) 
    else :
        name.append(x[i])      
result = ''.join(name)   
print(result)
