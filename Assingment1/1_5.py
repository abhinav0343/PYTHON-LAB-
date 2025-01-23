list = []
num = int(input("enter the total number of students : "))
print('enter the name of the students ')
print("students name must be with in 15 characters ")
for i in range (0,num) :
     name = input()
     list.append(name)
students = [names[:15] for names in list ]
rev_students = [num[::-1] for num in students]
print(rev_students)
