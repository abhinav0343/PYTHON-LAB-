import random 
import numpy as np
n = 14
points = [(random.randint(0,30),random.randint(0,30)) for _ in range (14)]
print(points)
coord_arr = np.array(points)
polar_arr = []
for point in points : 
    x,y = point
    r = np.hypot(x,y)
    theta = np.arctan2(y,x)
    theta_deg = np.degrees(theta)
    polar_arr.append([r,theta_deg])
polar_arr = np.array(polar_arr)
print(f"polar coordinates (r,theta(deg))")
print(polar_arr)