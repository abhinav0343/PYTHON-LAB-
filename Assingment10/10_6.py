import numpy as np
import random
import matplotlib.pyplot as plt
def f(x) : 
    return x**3 - 6*x**2 + 11*x - 6 

def bisection(f,a,b,mini = 1e-6,iteration_max = 100) :
     if f(a)*f(b) >= 0 :
         print("ERROR OCCURRED ! points must be in opposite sign")
     else :
         iterations = []
         for i in range (iteration_max) : 
             mid = (a + b) / 2
             iterations.append([a,b,mid,f(mid)])
             if abs(f(mid)) <= mini : 
                 break
             if f(a)*f(mid) < 0 :
                 b = mid 
             elif f(b)*f(mid) < 0 :
                 a = mid
             
         return np.array(iterations),mid

a = np.random.uniform(-10,10)
b = np.random.uniform(-10,10)

# in BISECTION METHOD randomly choosen points must be in opposite signs

while f(a)*f(b) >= 0 :
    a = np.random.uniform(-10,10)
    b = np.random.uniform(-10,10)
updates,root = bisection(f,a,b)
print(updates)
print(root)
print()
print()

midpoints = updates[:, 2]  # The third column contains midpoint values (mid)
function_values = updates[:, 3]  # The fourth column contains f(mid)

# Plot the root-finding process
plt.figure(figsize=(8, 6))
plt.plot(midpoints, function_values, 'o-', label='Function value at midpoint (f(mid))')
plt.axhline(y=0, color='r', linestyle='--', label='Zero Line (Root)')
plt.xlabel('Midpoint')
plt.ylabel('f(Midpoint)')
plt.title('Root-Finding Process via Bisection Method')
plt.legend()
plt.grid(True)
plt.show()
