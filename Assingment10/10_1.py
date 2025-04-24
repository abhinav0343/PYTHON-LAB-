import random
import numpy as np

num_queens = 8
currentsolution = np.zeros(num_queens, dtype=int) 
solution = []

# this code is position based index

def issafe(test_rows,test_cols) : 
    for row in range (1,test_rows) :
        #check vertical
        if test_cols == currentsolution[row-1] :
            return False
        #check diagonal
        if abs(test_rows-row) == abs(test_cols-currentsolution[row-1]) :  
            return False
    return True

def place_queens(row) :
    global currentsolution,solution,num_queens
    for col in range (1,num_queens+1) :
        if not issafe(row,col) :
            continue
        else :
            currentsolution[row-1] = col
            if row == num_queens :
                solution.append(currentsolution.copy())
            else :
                place_queens(row+1)

place_queens(1)
print(f"total possible solutions : {len(solution)}")
random_number = random.choice(solution)
print()
print(f"random solution : {random_number}")
j=0
for i in range (1,num_queens+1) :
    for k in range (1,num_queens+1) :
       if random_number[j] == k :
           print("*",end=' ')
       else :
           print("_",end=' ')
    j += 1
    print('\n')
