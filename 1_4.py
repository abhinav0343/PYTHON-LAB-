list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
for i in range(1,10001) :
    if( i % 5 == 0) : 
        list1.append(i)   # append(i) function used to add numbers to the list 
    elif( i % 5 == 1 ) : 
        list2.append(i)
    elif( i % 5 == 2 ) : 
        list3.append(i) 
    elif( i % 5 == 3 ) : 
        list4.append(i)
    elif( i % 5 == 4 ) : 
        list5.append(i)
set1 = set(list1)
set2 = set(list2)
set3 = set(list3)
set4 = set(list4)
set5 = set(list5)
union_set = set1 | set2 | set3 | set4 | set5 
full_set = set(range(1,10001))
if union_set == full_set :
   print("union of all sets covers the entire set range from 1 to 10,000 ")
else :
   print("union of all sets did not covers entire set range from 1 to 10,000 ")