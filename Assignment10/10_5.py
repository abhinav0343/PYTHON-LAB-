import numpy as np
pad_arr = np.array(["hello","abhinav","98271789","1","ABHINAVKUMARGOLLA"])
for string in pad_arr  : 
    if len(string) < 15 : 
       sub = 15 - len(string)
       left_pad = sub//2
       right_pad = sub-left_pad
       centered_string = "_"*left_pad + string + "_"*right_pad
       left_string = string + "_"*sub
       right_string = "_"*sub+string
       print(f"centered : {centered_string}")
       print(f"left justified : {left_string}")
       print(f"right justified : {right_string}")
    else : 
        cut_string = string[:15]
        print(f"after removing excess 15 : {cut_string}")
    print()